import os
import hashlib
import json
import requests
from pathlib import Path

# Configuration
SOURCE_DIR = Path("/home/ari/dev/ff-story/manuscript/text")
OUTPUT_DIR = Path("/home/ari/dev/forgotten-future-site/public/audio/manuscript")
SYNC_FILE = SOURCE_DIR.parent / "audio_sync.json"
ENV_FILE = Path("/home/ari/dev/ff-teaser/.env")

# OpenAI API details
TTS_URL = "https://api.openai.com/v1/audio/speech"
VOICE = "fable"  # Options: alloy, echo, fable, onyx, nova, shimmer
MODEL = "tts-1-hd"

def get_api_key():
    with open(ENV_FILE, "r") as f:
        for line in f:
            if line.startswith("OPENAI_API_KEY="):
                return line.strip().split("=", 1)[1]
    raise ValueError("OPENAI_API_KEY not found in .env")

def get_file_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def clean_markdown(text):
    # Strip triple backticks if they wrap the whole file
    text = text.strip()
    if text.startswith("```markdown"):
        text = text[11:]
    if text.endswith("```"):
        text = text[:-3]
    
    # Strip title lines (starts with #) - typically skip the first one for the narrator
    lines = text.strip().split("\n")
    cleaned_lines = []
    for line in lines:
        # We keep the text but maybe strip the # prefix
        if line.startswith("# "):
            cleaned_lines.append(line.replace("# ", "").strip() + ".") # Add a pause
        elif line.startswith("## "):
            cleaned_lines.append(line.replace("## ", "").strip() + ".")
        else:
            cleaned_lines.append(line)
    
    return "\n".join(cleaned_lines)

def render_chapter(chapter_num):
    api_key = get_api_key()
    
    # Find the file
    files = list(SOURCE_DIR.glob(f"chapter_{chapter_num:02d}*.md"))
    if not files:
        print(f"Chapter {chapter_num} not found.")
        return
    
    source_file = files[0]
    output_temp_dir = OUTPUT_DIR / f"temp_ch{chapter_num}"
    output_file = OUTPUT_DIR / f"chapter_{chapter_num:02d}.mp3"
    
    with open(source_file, "r") as f:
        raw_content = f.read()
    
    cleaned_text = clean_markdown(raw_content)
    current_hash = get_file_hash(cleaned_text)
    
    # Load sync record
    sync_data = {}
    if SYNC_FILE.exists():
        with open(SYNC_FILE, "r") as f:
            sync_data = json.load(f)
    
    chapter_key = f"chapter_{chapter_num:02d}"
    
    # Check if we need to regenerate
    if chapter_key in sync_data and sync_data[chapter_key]["hash"] == current_hash and output_file.exists():
        print(f"Chapter {chapter_num} is already in sync. Skipping.")
        return

    print(f"Rendering Chapter {chapter_num} ({len(cleaned_text)} characters)...")
    
    # Split into chunks of 4000 chars (safe under 4096 limit)
    # Prefer splitting on sentence boundaries or paragraphs
    max_chunk = 4000
    paragraphs = cleaned_text.split("\n\n")
    chunks = []
    current_chunk = ""
    
    for p in paragraphs:
        if len(current_chunk) + len(p) + 2 < max_chunk:
            current_chunk += (p + "\n\n")
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = p + "\n\n"
    if current_chunk:
        chunks.append(current_chunk.strip())

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    combined_audio = b""
    
    for i, chunk in enumerate(chunks):
        print(f"  Requesting chunk {i+1}/{len(chunks)} ({len(chunk)} characters)...")
        data = {
            "model": MODEL,
            "input": chunk,
            "voice": VOICE
        }
        
        response = requests.post(TTS_URL, headers=headers, json=data)
        
        if response.status_code == 200:
            combined_audio += response.content
        else:
            print(f"Error at chunk {i+1}: {response.status_code} - {response.text}")
            return

    # Write final file
    with open(output_file, "wb") as f:
        f.write(combined_audio)
    
    # Update sync data
    sync_data[chapter_key] = {
        "hash": current_hash,
        "file": source_file.name,
        "timestamp": os.path.getmtime(source_file)
    }
    with open(SYNC_FILE, "w") as f:
        json.dump(sync_data, f, indent=4)
    print(f"Done! Saved to {output_file}")

if __name__ == "__main__":
    # For now, just do Chapter 1 as requested
    render_chapter(1)
