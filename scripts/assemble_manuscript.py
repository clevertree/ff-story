import os

repo_root = "/home/ari/dev/ff/ff-story"
chapters_dir = os.path.join(repo_root, "manuscript/text")
output_file = os.path.join(repo_root, "manuscript/FULL_MANUSCRIPT.md")

# Get sorted list of chapter files
chapter_files = sorted([f for f in os.listdir(chapters_dir) if f.startswith("chapter_") and f.endswith(".md")])

full_content = [
    "# Forgotten Future: Full Manuscript",
    "\n**Version:** 0.10.2",
    "\n**Date:** 2026-01-14",
    "\n---\n"
]

for filename in chapter_files:
    path = os.path.join(chapters_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        # Ensure we separate chapters clearly
        full_content.append(content)
        full_content.append("\n---\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(full_content))

print(f"Successfully assembled {len(chapter_files)} chapters into {output_file}")
