import os
import re
import json
import subprocess

# Get the script's directory and then the repo root (one level up)
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)

def get_chapter_data():
    chapters_dir = os.path.join(repo_root, "chapters")
    files = sorted([f for f in os.listdir(chapters_dir) if f.startswith("chapter_") and f.endswith(".md")])
    
    chapter_data = []
    
    for filename in files:
        filepath = os.path.join(chapters_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        if not lines:
            continue

        title = lines[0].strip()
        # Handle "# Chapter 1: Title" or "# 1: Title" or "1: Title" or "# Title"
        title = re.sub(r'^#\s*', '', title) # Remove leading #
        title = re.sub(r'^Chapter\s*', '', title, flags=re.IGNORECASE) # Remove "Chapter"
        title = re.sub(r'^\d+:\s*', '', title) # Remove ID like "12:"
        
        summary = ""
        found_synopsis = False
        synopsis_lines = []
        for line in lines:
            if "## Synopsis" in line:
                found_synopsis = True
                continue
            if found_synopsis:
                if line.startswith("## ") or line.startswith("---") or line.startswith("**Chapter Beats:**"):
                    break
                if line.strip():
                    synopsis_lines.append(line.strip())
        
        if synopsis_lines:
            summary = " ".join(synopsis_lines)
        else:
            # Fallback: look for character arc or outline first bit
            for line in lines:
                if line.strip() and not line.startswith("#") and not line.startswith("**") and not line.startswith("---"):
                    summary = line.strip()
                    break
        
        # Clean up summary
        summary = summary[:250] + "..." if len(summary) > 250 else summary
        
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
    index_path = os.path.join(repo_root, "chapters/INDEX.md")
    # Actually, INDEX.md has a complex structure, update_meta.py shouldn't overwrite it blindly
    # unless it's intended to be simpler. For now, let's just use the dynamic path.
    pass

def generate_commits_json():
    commits_json_path = os.path.join(repo_root, "manuscript/commits.json")
    # Get git log in a simple format: hash|date|message
    cmd = ["git", "log", "--pretty=format:%h|%as|%s", "-n", "20"]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=repo_root)
    
    commits = []
    for line in result.stdout.strip().split('\n'):
        if not line:
            continue
        parts = line.split('|', 2)
        if len(parts) == 3:
            commits.append({
                "hash": parts[0],
                "date": parts[1],
                "message": parts[2]
            })
    
    with open(commits_json_path, 'w', encoding='utf-8') as f:
        json.dump(commits, f, indent=4)
    print(f"Updated {commits_json_path}")

def generate_web_chapters(data):
    # This will output the JS array for page.tsx
    # We'll also save this to a json file in manuscript/ if needed
    web_meta_path = os.path.join(repo_root, "manuscript/chapters.json")
    with open(web_meta_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Updated {web_meta_path}")

if __name__ == "__main__":
    data = get_chapter_data()
    # update_index_md(data) # Skipping to avoid destructive changes to INDEX.md
    generate_web_chapters(data)
    generate_commits_json()
