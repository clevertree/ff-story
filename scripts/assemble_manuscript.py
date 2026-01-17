import os
import re

# Get the script's directory and then the repo root (one level up)
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)

chapters_dir = os.path.join(repo_root, "chapters")
output_file = os.path.join(repo_root, "manuscript/FULL_MANUSCRIPT.md")

# Get sorted list of chapter files
chapter_files = sorted([f for f in os.listdir(chapters_dir) if f.startswith("chapter_") and f.endswith(".md")])

# Read current version
with open(os.path.join(repo_root, "VERSION"), "r") as f:
    current_version = f.read().strip()

full_content = [
    "# Forgotten Future: Full Manuscript",
    f"\n**Version:** {current_version}",
    "\n**Date:** 2026-01-14",
    "\n---\n"
]

def extract_draft_section(content):
    # Keep the Chapter title (level 1 header)
    title_match = re.search(r"^# .*", content, re.MULTILINE)
    title = title_match.group(0) if title_match else "Untitled Chapter"
    
    # Extract text after ## Draft but before the next ## section or ---
    # We look for ## Draft specifically
    draft_match = re.search(r"## Draft\s*\n(.*?)(?=\n## |\n---|$)", content, re.DOTALL)
    
    if draft_match:
        draft_content = draft_match.group(1).strip()
        return f"{title}\n\n{draft_content}"
    
    # If no Draft section found, we definitely don't want the metadata
    # But as a safety, let's see if there is any prose at all.
    # For now, per user request, we only want the title and the draft content.
    return title # Return only title if no draft found

for filename in chapter_files:
    path = os.path.join(chapters_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        # Keep only the title and the draft content
        processed_content = extract_draft_section(content)
        full_content.append(processed_content)
        full_content.append("\n---\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(full_content))

print(f"Successfully assembled {len(chapter_files)} chapters into {output_file}")
