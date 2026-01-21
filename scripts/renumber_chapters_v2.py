import os
import re

def renumber_chapters(start_index, increment, directory):
    # Reverse order to avoid collisions
    files = [f for f in os.listdir(directory) if f.startswith("chapter_") and f.endswith(".md")]
    
    # Extract numbers and sort descending
    chapter_files = []
    for f in files:
        match = re.match(r"chapter_(\d+)_", f)
        if match:
            num = int(match.group(1))
            if num >= start_index:
                chapter_files.append((num, f))
    
    chapter_files.sort(key=lambda x: x[0], reverse=True)
    
    for num, filename in chapter_files:
        new_num = num + increment
        new_filename = filename.replace(f"chapter_{num:02d}_", f"chapter_{new_num:02d}_")
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        print(f"Renaming {filename} to {new_filename}")
        os.rename(old_path, new_path)
        
        # Update internal header
        with open(new_path, 'r') as f:
            content = f.read()
        
        # Look for # Chapter XX:
        new_content = re.sub(r"^# Chapter \d+:", f"# Chapter {new_num:02d}:", content, flags=re.MULTILINE)
        
        with open(new_path, 'w') as f:
            f.write(new_content)

if __name__ == "__main__":
    renumber_chapters(17, 2, "/Users/ari.asulin/p/ff-story/chapters")
