import os
import re

def get_chapter_data():
    chapters_dir = "/home/ari/dev/ff/ff-story/chapters"
    files = sorted([f for f in os.listdir(chapters_dir) if f.startswith("chapter_") and f.endswith(".md")])
    
    chapter_data = []
    
    for filename in files:
        filepath = os.path.join(chapters_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        title = lines[0].strip().replace("# Chapter ", "")
        # Remove ID from start of title if present (e.g. "1: Title" -> "Title")
        title = re.sub(r'^\d+:\s*', '', title)
        
        summary = ""
        found_synopsis = False
        for line in lines:
            if "## Synopsis" in line:
                found_synopsis = True
                continue
            if found_synopsis and line.strip() and not line.startswith("#"):
                summary = line.strip()
                break
        
        if not summary:
            # Fallback: look for character arc or outline first bit
            for line in lines:
                if line.strip() and not line.startswith("#") and not line.startswith("**") and not line.startswith("---"):
                    summary = line.strip()
                    break
        
        # Clean up summary
        summary = summary[:150] + "..." if len(summary) > 150 else summary
        
        id_match = re.search(r'chapter_(\d+)', filename)
        chapter_id = int(id_match.group(1)) if id_match else 0
        
        chapter_data.append({
            "id": chapter_id,
            "title": title,
            "summary": summary,
            "filename": filename
        })
        
    return sorted(chapter_data, key=lambda x: x["id"])

def update_index_md(data):
    index_path = "/home/ari/dev/ff/ff-story/chapters/INDEX.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Forgotten Future: Manuscript Chapters\n\n")
        f.write("This directory contains the narrative foundation of **Forgotten Future**, refined for pacing (71 Chapters).\n\n---\n\n")
        
        for ch in data:
            f.write(f"{ch['id']}. [{ch['title']}]({ch['filename']}) — {ch['summary']}\n")

def generate_web_chapters(data):
    # This will output the JS array for page.tsx
    print("const chapters = [")
    for ch in data:
        # Escape single quotes in title and summary
        t = ch['title'].replace("'", "\\'")
        s = ch['summary'].replace("'", "\\'")
        audio_str = f", audio: '/audio/manuscript/chapter_{ch['id']:02d}.mp3'" if ch['id'] <= 1 else ""
        print(f"    {{ id: {ch['id']}, title: '{t}', summary: '{s}'{audio_str} }},")
    print("];")

if __name__ == "__main__":
    data = get_chapter_data()
    update_index_md(data)
    generate_web_chapters(data)
