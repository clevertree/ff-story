import os
import re

directory = "/Users/ari.asulin/p/ff-story/chapters"
files = os.listdir(directory)

# Collect chapter files with numbers >= 19
chapter_files = []
for f in files:
    match = re.match(r"chapter_(\d+)_", f)
    if match:
        num = int(match.group(1))
        if num >= 19:
            chapter_files.append((num, f))

# Sort in descending order to avoid overwriting
chapter_files.sort(key=lambda x: x[0], reverse=True)

for num, f in chapter_files:
    new_num = num + 1
    new_filename = f.replace(f"chapter_{num:02d}_", f"chapter_{new_num:02d}_")
    # If it was not 02d, handle it
    if new_filename == f:
         new_filename = f.replace(f"chapter_{num}_", f"chapter_{new_num}_")
    
    old_path = os.path.join(directory, f)
    new_path = os.path.join(directory, new_filename)
    print(f"Lemaming {old_path} to {new_path}")
    os.rename(old_path, new_path)
