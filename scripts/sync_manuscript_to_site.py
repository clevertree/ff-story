import os
import re
from pathlib import Path

# Paths
SOURCE_DIR = Path("/home/ari/dev/ff-story/manuscript/text")
SITE_FILE = Path("/home/ari/dev/forgotten-future-site/app/manuscript/full-text/page.tsx")

def get_chapter_data():
    chapters = []
    # Sort files by chapter number
    files = sorted(list(SOURCE_DIR.glob("chapter_*.md")))
    
    for f in files:
        match = re.search(r"chapter_(\d+)_", f.name)
        if not match: continue
        ch_id = int(match.group(1))
        
        with open(f, "r") as src:
            content = src.read().strip()
            
            # Extract title (first line starting with # )
            title = "Untitled"
            title_match = re.search(r"^# (.*)$", content, re.MULTILINE)
            if title_match:
                title = title_match.group(1).split(":", 1)[-1].strip()
                # Remove the title line from the content
                content = content.replace(title_match.group(0), "").strip()
            
            # Escape backticks for JS template literal
            content = content.replace("`", "\\`").replace("${", "\\${")
            
            chapters.append({
                "id": ch_id,
                "title": title,
                "content": content
            })
    return chapters

def update_site():
    chapters = get_chapter_data()
    
    with open(SITE_FILE, "r") as f:
        site_content = f.read()
    
    # Generate the JS array string
    chapters_js = "const chapters = [\n"
    for ch in chapters:
        chapters_js += f"        {{\n"
        chapters_js += f"            id: {ch['id']},\n"
        chapters_js += f"            title: '{ch['title']}',\n"
        chapters_js += f"            content: `{ch['content']}`\n"
        chapters_js += f"        }},\n"
    chapters_js = chapters_js.rstrip(",\n") + "\n    ];"
    
    # Replace the existing chapters array
    # Pattern matches from 'const chapters = [' to '];'
    new_content = re.sub(
        r"const chapters = \[.*?\];",
        chapters_js,
        site_content,
        flags=re.DOTALL
    )
    
    with open(SITE_FILE, "w") as f:
        f.write(new_content)
    
    print(f"Successfully synced {len(chapters)} chapters to {SITE_FILE}")

if __name__ == "__main__":
    update_site()
