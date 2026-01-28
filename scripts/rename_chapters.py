import os
import re

chapters = {
    1: "Outpost",
    2: "Recruited",
    3: "Ascent",
    4: "Zenith",
    5: "Descent",
    6: "Surface",
    7: "Sacrifice",
    8: "Reset",
    9: "Restored",
    10: "Fragments",
    11: "Architect",
    12: "Purge",
    13: "Awakened",
    14: "Hive",
    15: "Guide",
    16: "Forest",
    17: "Vision",
    18: "Rebirth",
    19: "Clue",
    20: "Exile",
    21: "Return",
    22: "Prophet",
    23: "Refusal",
    24: "Siege",
    25: "The Cult",
    26: "Parley",
    27: "Duel",
    28: "Pillar",
    29: "Specter",
    30: "Breach",
    31: "Swarm",
    32: "Fleet",
    33: "Pyramid",
    34: "Message"
}

chapter_dir = "/home/ari/dev/ff/ff-story/chapters/"

files = os.listdir(chapter_dir)

for num, name in chapters.items():
    # Find existing file
    pattern = f"chapter_{num:02d}_"
    old_filename = next((f for f in files if f.startswith(pattern)), None)
    
    if old_filename:
        safe_name = name.lower().replace(" ", "_").replace("'", "")
        new_filename = f"chapter_{num:02d}_{safe_name}.md"
        old_path = os.path.join(chapter_dir, old_filename)
        new_path = os.path.join(chapter_dir, new_filename)
        
        # Read content
        with open(old_path, 'r') as f:
            content = f.read()
        
        # Update Header
        content = re.sub(r"^# Chapter \d+: .*", f"# Chapter {num:02d}: {name}", content)
        
        # Write content
        with open(old_path, 'w') as f:
            f.write(content)
            
        # Lemame file
        os.rename(old_path, new_path)
        print(f"Lemamed {old_filename} to {new_filename} and updated header.")
    else:
        print(f"Could not find file for chapter {num}")
