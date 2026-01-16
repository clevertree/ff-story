import os
import re

repo_root = "/home/ari/dev/ff/ff-story"

def fix_renumbering(directory):
    files = sorted([f for f in os.listdir(directory) if f.startswith("chapter_") and f.endswith(".md") and f != "chapter_template.md"])
    
    reincarnation_file = next((f for f in files if "reincarnation" in f), None)
    if not reincarnation_file:
        print(f"No reincarnation file found in {directory}")
        return

    match = re.match(r"chapter_(\d+)_", reincarnation_file)
    current_start_num = int(match.group(1))
    
    offset = current_start_num - 9
    
    if offset == 0:
        print(f"Directory {directory} already seems correct")
        return

    print(f"Fixing {directory}: Moving chapter {current_start_num} to 09 (offset {offset})")

    to_move = []
    for f in files:
        m = re.match(r"chapter_(\d+)_", f)
        if m:
            if int(m.group(1)) >= current_start_num:
                to_move.append(f)
    
    for f in to_move:
        m = re.match(r"chapter_(\d+)_", f)
        num = int(m.group(1))
        new_num = num - offset
        new_filename = f.replace(f"chapter_{num:02d}", f"chapter_{new_num:02d}")
        
        old_path = os.path.join(directory, f)
        new_path = os.path.join(directory, new_filename)
        
        print(f"Renaming {f} to {new_filename}")
        os.rename(old_path, new_path)
        
        # Update content header
        with open(new_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        new_content = re.sub(rf"^# Chapter \d+:", f"# Chapter {new_num}:", content, flags=re.MULTILINE)
        
        with open(new_path, "w", encoding="utf-8") as file:
            file.write(new_content)

fix_renumbering(os.path.join(repo_root, "manuscript/text"))
fix_renumbering(os.path.join(repo_root, "chapters"))
