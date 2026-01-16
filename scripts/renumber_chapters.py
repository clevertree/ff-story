import os
import re

repo_root = "/home/ari/dev/ff/ff-story"
chapters_dir = os.path.join(repo_root, "manuscript/text")

# Get list of files
files = os.listdir(chapters_dir)

# Pattern for chapter files: chapter_XX_...md
pattern = re.compile(r"chapter_(\d+)_.*\.md")

# Pattern for chapter files: chapter_XX_...md
pattern = re.compile(r"chapter_(\d+)_.*\.md")

def renumber_dir(directory):
    print(f"Renumbering directory: {directory}")
    # Filter and sort in reverse to avoid overwriting during rename
    chapter_files = []
    files = os.listdir(directory)
    for f in files:
        match = pattern.match(f)
        if match:
            chapter_num = int(match.group(1))
            if chapter_num >= 9:
                chapter_files.append((chapter_num, f))

    chapter_files.sort(key=lambda x: x[0], reverse=True)

    for num, filename in chapter_files:
        new_num = num + 1
        new_filename = filename.replace(f"chapter_{num:02d}", f"chapter_{new_num:02d}")
        
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # Check if destination exists
        if os.path.exists(new_path) and old_path != new_path:
            print(f"Warning: {new_path} already exists, skipping rename of {filename}")
            continue

        print(f"Renaming {filename} to {new_filename}")
        os.rename(old_path, new_path)
        
        # Update content
        with open(new_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Update # Chapter XX: Title or # Chapter 9: Title
        new_content = re.sub(rf"^# Chapter {num}:", f"# Chapter {new_num}:", content, flags=re.MULTILINE)
        new_content = re.sub(rf"^# Chapter {num:02d}:", f"# Chapter {new_num}:", new_content, flags=re.MULTILINE)
        
        with open(new_path, "w", encoding="utf-8") as f:
            f.write(new_content)

renumber_dir(os.path.join(repo_root, "manuscript/text"))
renumber_dir(os.path.join(repo_root, "chapters"))
