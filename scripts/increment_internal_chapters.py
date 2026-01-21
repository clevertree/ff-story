import os
import re

directory = "/Users/ari.asulin/p/ff-story/chapters"
files = os.listdir(directory)

for f in files:
    match = re.match(r"chapter_(\d+)_", f)
    if match:
        num = int(match.group(1))
        if num >= 20:
            path = os.path.join(directory, f)
            with open(path, 'r') as file:
                content = file.read()
            
            # Replace # Chapter X: with # Chapter X+1:
            # We know the internal number is num - 1
            old_internal = num - 1
            new_internal = num
            
            new_content = re.sub(rf"^# Chapter {old_internal}:", f"# Chapter {new_internal}:", content, flags=re.MULTILINE)
            
            if new_content != content:
                with open(path, 'w') as file:
                    file.write(new_content)
                print(f"Updated internal chapter number in {f}")
