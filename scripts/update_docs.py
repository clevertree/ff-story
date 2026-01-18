import os
import re

chapters = {
    1: ("Outpost", "outpost"),
    2: ("Recruited", "recruited"),
    3: ("Ascent", "ascent"),
    4: ("Zenith", "zenith"),
    5: ("Descent", "descent"),
    6: ("Surface", "surface"),
    7: ("Sacrifice", "sacrifice"),
    8: ("Reset", "reset"),
    9: ("Restored", "restored"),
    10: ("Fragments", "fragments"),
    11: ("Architect", "architect"),
    12: ("Purge", "purge"),
    13: ("Awakened", "awakened"),
    14: ("Hive", "hive"),
    15: ("Guide", "guide"),
    16: ("Forest", "forest"),
    17: ("Vision", "vision"),
    18: ("Rebirth", "rebirth"),
    19: ("Clue", "clue"),
    20: ("Exile", "exile"),
    21: ("Return", "return"),
    22: ("Prophet", "prophet"),
    23: ("Refusal", "refusal"),
    24: ("Siege", "siege"),
    25: ("The Cult", "the_cult"),
    26: ("Parley", "parley"),
    27: ("Duel", "duel"),
    28: ("Pillar", "pillar"),
    29: ("Specter", "specter"),
    30: ("Breach", "breach"),
    31: ("Swarm", "swarm"),
    32: ("Fleet", "fleet"),
    33: ("Pyramid", "pyramid"),
    34: ("Message", "message")
}

files_to_update = [
    "/home/ari/dev/ff/ff-story/PLAN_YOUNG_ADULT.md",
    "/home/ari/dev/ff/ff-story/PLAN_13_PLUS.md",
    "/home/ari/dev/ff/ff-story/PLAN_GOOGLE_TTS.md",
    "/home/ari/dev/ff/ff-story/TODO_SYNC_13_PLUS.md"
]

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replacement loop
    for num, (name, slug) in chapters.items():
        # Match lines like: 1. [Title](chapters/chapter_01_old_name.md)
        pattern = rf"{num}\. \[(.*?)\]\(chapters/chapter_{num:02d}_(.*?)\.md\)"
        replacement = f"{num}. [{name}](chapters/chapter_{num:02d}_{slug}.md)"
        content = re.sub(pattern, replacement, content)
        
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Updated {file_path}")
