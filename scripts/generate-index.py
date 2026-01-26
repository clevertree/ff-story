import os
import json

def generate_index():
    # Get the directory where the script is located and go up to the repo root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.dirname(script_dir)
    output_file = os.path.join(repo_dir, "index.json")
    
    exclude_dirs = {'.git', '.github', 'scripts', 'node_modules', '.idea', 'ff-story.worktrees', 'media', 'docs', 'media'}
    # Wait, the user mentioned world-building, chapters, docs, manuscript. 
    # Let me check ff-story structure again.
    
    # Actually, let's just exclude known noise.
    exclude_dirs = {'.git', '.github', 'scripts', 'node_modules', '.idea', 'ff-story.worktrees'}
    exclude_files = {'index.json', 'package-lock.json', 'package.json', 'tsconfig.json', 'VERSION', '.gitignore', 'COMMIT_HISTORY.md'}
    
    include_exts = {'.md', '.txt', '.pdf', '.json', '.srt', '.jpg', '.png'}

    def build_tree(current_path):
        tree = {}
        total_files = 0
        
        try:
            items = os.listdir(current_path)
        except PermissionError:
            return {}, 0
            
        for item in sorted(items):
            if item in exclude_files or item.startswith('.'):
                continue
                
            full_path = os.path.join(current_path, item)
            
            if os.path.isdir(full_path):
                if item in exclude_dirs:
                    continue
                subtree, count = build_tree(full_path)
                # We include empty directories as requested
                tree[item] = subtree
                tree[item]['_count'] = count
                total_files += count
            else:
                ext = os.path.splitext(item)[1].lower()
                if ext in include_exts:
                    tree[item] = None
                    total_files += 1
        
        return tree, total_files

    tree, count = build_tree(repo_dir)
    tree['_count'] = count
    
    with open(output_file, 'w') as f:
        json.dump(tree, f, indent=2)
    
    print(f"Generated index.json with {count} files at {output_file}")

if __name__ == "__main__":
    generate_index()
