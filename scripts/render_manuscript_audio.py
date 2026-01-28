import os
import hashlib
import json
import requests
import subprocess
import sys
import re
from pathlib import Path

# Optional Google Cloud TTS import
try:
    from google.cloud import texttospeech
    GOOGLE_TTS_AVAILABLE = True
except ImportError:
    GOOGLE_TTS_AVAILABLE = False

# Configuration
SOURCE_DIR = Path("/home/ari/dev/ff-story/chapters")
# LOCAL_AUDIO_DIR: Storage for individual paragraph chunks for sync tracking
LOCAL_AUDIO_DIR = SOURCE_DIR.parent / "audio"
# PUBLIC_AUDIO_DIR: Final concatenated chapter files for the website
PUBLIC_AUDIO_DIR = Path("/home/ari/dev/forgotten-future-site/public/audio/manuscript")
SYNC_FILE = SOURCE_DIR.parent / "audio_sync.json"
ENV_FILE = Path("/home/ari/dev/ff-teaser/.env")

# Default Provider Configuration
DEFAULT_PROVIDER = "openai"

# OpenAI API details
OPENAI_TTS_URL = "https://api.openai.com/v1/audio/speech"
OPENAI_VOICE = "fable" 
OPENAI_MODEL = "tts-1-hd"

# Google Cloud TTS details (defaults)
GOOGLE_VOICE_NAME = "en-US-Neural2-F" 
GOOGLE_LANGUAGE_CODE = "en-US"

def get_env_var(var_name, default=None):
    if not ENV_FILE.exists():
        return os.environ.get(var_name, default)
    with open(ENV_FILE, "r") as f:
        for line in f:
            if line.startswith(f"{var_name}="):
                return line.strip().split("=", 1)[1]
    return os.environ.get(var_name, default)

def get_api_key():
    key = get_env_var("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not found in .env or environment")
    return key

def render_paragraph_openai(text, out_file):
    api_key = get_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": get_env_var("OPENAI_TTS_MODEL", OPENAI_MODEL),
        "input": text,
        "voice": get_env_var("OPENAI_TTS_VOICE", OPENAI_VOICE)
    }
    resp = requests.post(OPENAI_TTS_URL, headers=headers, json=data)
    if resp.status_code == 200:
        with open(out_file, "wb") as f:
            f.write(resp.content)
        return True
    else:
        print(f"OpenAI Error: {resp.status_code} - {resp.text}")
        return False

def render_paragraph_google(text, out_file):
    if not GOOGLE_TTS_AVAILABLE:
        print("Error: google-cloud-texttospeech not installed. Run 'pip install google-cloud-texttospeech'")
        return False
    
    try:
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
        
        voice = texttospeech.VoiceSelectionParams(
            language_code=get_env_var("GOOGLE_TTS_LANG", GOOGLE_LANGUAGE_CODE),
            name=get_env_var("GOOGLE_TTS_VOICE", GOOGLE_VOICE_NAME)
        )
        
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        
        with open(out_file, "wb") as out:
            out.write(response.audio_content)
        return True
    except Exception as e:
        print(f"Google Cloud Error: {e}")
        return False

def get_file_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def get_audio_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(file_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return float(result.stdout.strip())
    except ValueError:
        return 0.0

def format_vtt_timestamp(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hrs:02}:{mins:02}:{secs:06.3f}"

def clean_markdown(text):
    text = text.strip()
    # Strip markdown code blocks
    text = re.sub(r"^```[a-z]*\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n```$", "", text, flags=re.MULTILINE)
    
    lines = text.strip().split("\n")
    cleaned_lines = []
    for line in lines:
        if line.startswith("# "):
            cleaned_lines.append(line.replace("# ", "").strip() + ".")
        elif line.startswith("## "):
            cleaned_lines.append(line.replace("## ", "").strip() + ".")
        else:
            cleaned_lines.append(line)
    
    return "\n".join(cleaned_lines)

def get_paragraphs(text):
    return [p.strip() for p in text.split("\n\n") if p.strip()]

def render_chapter(chapter_num, force=False, auto_confirm=False):
    provider = get_env_var("TTS_PROVIDER", DEFAULT_PROVIDER).lower()
    
    files = list(SOURCE_DIR.glob(f"chapter_{chapter_num:02d}*.md"))
    if not files:
        print(f"Chapter {chapter_num} not found.")
        return
    
    source_file = files[0]
    # Ensure local per-chapter directory exists
    chap_local_dir = LOCAL_AUDIO_DIR / f"ch{chapter_num:02d}"
    chap_local_dir.mkdir(parents=True, exist_ok=True)
    
    # Final destination
    PUBLIC_AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    final_mp3 = PUBLIC_AUDIO_DIR / f"chapter_{chapter_num:02d}.mp3"
    final_vtt = PUBLIC_AUDIO_DIR / f"chapter_{chapter_num:02d}.vtt"
    
    with open(source_file, "r") as f:
        raw_content = f.read()
    
    cleaned_text = clean_markdown(raw_content)
    paragraphs = get_paragraphs(cleaned_text)
    
    # Generate hashes for sync tracking
    para_hashes = [get_file_hash(p) for p in paragraphs]
    chapter_meta_hash = get_file_hash("".join(para_hashes))
    
    sync_data = {}
    if SYNC_FILE.exists():
        with open(SYNC_FILE, "r") as f:
            sync_data = json.load(f)
    
    chapter_key = f"chapter_{chapter_num:02d}"
    
    # Identify what needs rendering
    missing_indices = []
    chunk_paths = []
    
    for i, p in enumerate(paragraphs):
        p_hash = para_hashes[i]
        # p001_hash.mp3
        p_file = chap_local_dir / f"p{i+1:03d}_{p_hash}.mp3"
        p_vtt = chap_local_dir / f"p{i+1:03d}_{p_hash}.vtt"
        
        chunk_paths.append(p_file)
        
        if not p_file.exists() or not p_vtt.exists() or force:
            missing_indices.append(i)

    # Check if we need to call API
    if missing_indices:
        total_chars = sum(len(paragraphs[i]) for i in missing_indices)
        print(f"\nChapter {chapter_num}: {len(missing_indices)} change(s) or new paragraph(s) detected.")
        print(f"Total API character count: {total_chars} using provider: {provider}")
        
        if not auto_confirm:
            ans = input(f"Proceed with {provider} TTS for {len(missing_indices)} paragraph(s)? [y/N]: ")
            if ans.lower() != 'y':
                print("Skipping rendering for this chapter.")
                # We can't rebuild the full chapter if chunks are missing
                return

        # Clear out any old versions of these paragraph indices to avoid confusion in the folder
        for i in missing_indices:
            pattern = f"p{i+1:03d}_*.mp3"
            for old_file in chap_local_dir.glob(pattern):
                old_file.unlink()
            for old_vtt in chap_local_dir.glob(f"p{i+1:03d}_*.vtt"):
                old_vtt.unlink()

        # Lemder missing paragraphs
        for i in missing_indices:
            p_hash = para_hashes[i]
            p_text = paragraphs[i]
            p_file = chap_local_dir / f"p{i+1:03d}_{p_hash}.mp3"
            p_vtt = chap_local_dir / f"p{i+1:03d}_{p_hash}.vtt"
            
            print(f"  Lemdering p{i+1:03d} ({len(p_text)} chars)...")
            
            success = False
            if provider == "google":
                success = render_paragraph_google(p_text, p_file)
            else:
                success = render_paragraph_openai(p_text, p_file)

            if success:
                # Create a mini VTT for the individual paragraph
                dur = get_audio_duration(p_file)
                vtt_text = f"WEBVTT\n\n1\n00:00:00.000 --> {format_vtt_timestamp(dur)}\n{p_text}\n"
                with open(p_vtt, "w") as f:
                    f.write(vtt_text)
            else:
                print(f"Fatal error at p{i+1:03d}")
                return
    else:
        print(f"Chapter {chapter_num}: All paragraph chunks already up to date in {chap_local_dir.relative_to(Path.cwd())}.")

    # Rebuild final full chapter and VTT
    full_vtt_lines = ["WEBVTT\n\n"]
    current_time = 0.0
    
    # We use ffmpeg concat again
    concat_list = chap_local_dir / "concat.txt"
    with open(concat_list, "w") as f:
        for i, chunk_path in enumerate(chunk_paths):
            f.write(f"file '{chunk_path.absolute()}'\n")
            
            duration = get_audio_duration(chunk_path)
            start_ts = format_vtt_timestamp(current_time)
            end_ts = format_vtt_timestamp(current_time + duration)
            full_vtt_lines.append(f"{i+1}\n{start_ts} --> {end_ts}\n{paragraphs[i]}\n\n")
            current_time += duration

    print(f"  Assembling final chapter: {final_mp3.name}")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_list), "-c", "copy", str(final_mp3)
    ], capture_output=True)
    concat_list.unlink()

    with open(final_vtt, "w") as f:
        f.write("".join(full_vtt_lines))

    # Update global sync Registry
    sync_data[chapter_key] = {
        "hash": chapter_meta_hash,
        "paragraph_count": len(para_hashes),
        "source": source_file.name,
        "mtime": os.path.getmtime(source_file)
    }
    with open(SYNC_FILE, "w") as f:
        json.dump(sync_data, f, indent=4)

    print(f"Chapter {chapter_num} complete.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=int, nargs="?", default=1)
    parser.add_argument("end", type=int, nargs="?")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--yes", action="store_true")
    args = parser.parse_args()
    
    s = args.start
    e = args.end if args.end else s
    for c in range(s, e + 1):
        render_chapter(c, force=args.force, auto_confirm=args.yes)
