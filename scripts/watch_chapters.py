#!/usr/bin/env python3
import os
import time
import subprocess
from datetime import datetime

# Get the script's directory and then the repo root (one level up)
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
chapters_dir = os.path.join(repo_root, 'chapters')
gen_script = os.path.join(script_dir, 'generate_manuscripts.py')

def get_mtimes():
    mtimes = {}
    for filename in os.listdir(chapters_dir):
        if filename.endswith('.md'):
            path = os.path.join(chapters_dir, filename)
            mtimes[path] = os.path.getmtime(path)
    return mtimes

def watch():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Watching {chapters_dir} for changes...")
    last_mtimes = get_mtimes()

    try:
        while True:
            time.sleep(2)  # Check every 2 seconds
            current_mtimes = get_mtimes()
            
            changed = False
            for path, mtime in current_mtimes.items():
                if path not in last_mtimes or mtime > last_mtimes[path]:
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] Detected change in: {os.path.basename(path)}")
                    changed = True
                    break
            
            if changed:
                subprocess.run(["python3", gen_script])
                last_mtimes = current_mtimes
    except KeyboardInterrupt:
        print("\nStopping watcher...")

if __name__ == "__main__":
    watch()
