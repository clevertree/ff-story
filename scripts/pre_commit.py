#!/usr/bin/env python3
import sys
import os
import subprocess

def bump_version(version_str):
    parts = version_str.strip().split('.')
    if len(parts) == 3:
        parts[2] = str(int(parts[2]) + 1)
    return '.'.join(parts)

def update_repo():
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    version_file = os.path.join(repo_dir, "VERSION")
    history_file = os.path.join(repo_dir, "COMMIT_HISTORY.md")

    # 1. Bump VERSION
    if os.path.exists(version_file):
        with open(version_file, 'r') as f:
            current_v = f.read().strip()
        new_v = bump_version(current_v)
        with open(version_file, 'w') as f:
            f.write(new_v + '\n')
        print(f"Bumped version: {current_v} -> {new_v}")
        subprocess.run(["git", "add", "VERSION"], cwd=repo_dir)

    # 2. Update COMMIT_HISTORY.md
    with open(history_file, 'w') as f:
        subprocess.run(["git", "log", "--oneline"], stdout=f, cwd=repo_dir)
    print("Updated COMMIT_HISTORY.md")
    subprocess.run(["git", "add", "COMMIT_HISTORY.md"], cwd=repo_dir)

    # Generate index.json
    index_script = os.path.join(repo_dir, "scripts/generate-index.py")
    if os.path.exists(index_script):
        print("Generating index.json...")
        subprocess.run(["python3", index_script], cwd=repo_dir)
        subprocess.run(["git", "add", "index.json"], cwd=repo_dir)

    # 2a. Regenerate Manuscripts
    gen_script = os.path.join(repo_dir, "scripts/generate_manuscripts.py")
    subprocess.run(["python3", gen_script], cwd=repo_dir)
    subprocess.run(["git", "add", "manuscript/MANUSCRIPT_YOUNG_ADULT.md", "manuscript/MANUSCRIPT_13_PLUS.md"], cwd=repo_dir)

    # 2b. Run update_meta.py
    meta_script = os.path.join(repo_dir, "scripts/update_meta.py")
    subprocess.run(["python3", meta_script], cwd=repo_dir)
    subprocess.run(["git", "add", "manuscript/commits.json", "manuscript/chapters.json"], cwd=repo_dir)

    # 3. Update Site Dashboard if available
    base_dir = os.path.dirname(repo_dir)
    site_script = os.path.join(base_dir, "forgotten-future-site/scripts/pre_commit.py")
    if os.path.exists(site_script):
        print("Triggering site dashboard update...")
        # Clear Git environment variables to avoid cross-repo corruption
        env = os.environ.copy()
        for key in ['GIT_DIR', 'GIT_INDEX_FILE', 'GIT_WORK_TREE', 'GIT_PREFIX']:
            env.pop(key, None)
        subprocess.run(["python3", site_script, "--only-dashboard"], env=env)

if __name__ == "__main__":
    update_repo()
