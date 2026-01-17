import os
import re

# Get the script's directory and then the repo root (one level up)
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)

chapters_dir = os.path.join(repo_root, 'chapters')
manuscript_dir = os.path.join(repo_root, 'manuscript')
index_file = os.path.join(chapters_dir, 'INDEX.md')

def parse_index():
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = []
    # Match Part headers and synopses
    # Format: ## PART I: TITLE\n*Synopsis*
    # Then captures the numbers listed below it
    part_pattern = r'## (PART [IVX]+:.*?)\n\*(.*?)\*\n\n(.*?)(?=\n---|\n## Draft|$)'
    matches = re.finditer(part_pattern, content, re.DOTALL)
    
    for match in matches:
        title = match.group(1).strip()
        synopsis = match.group(2).strip()
        chapter_list_text = match.group(3).strip()
        
        # Extract chapter numbers/filenames
        # Format: 1. [Title](chapter_01_the_alien_moon_base.md)
        chapter_files = re.findall(r'\[.*?\]\((.*?)\)', chapter_list_text)
        
        parts.append({
            'title': title,
            'synopsis': synopsis,
            'chapters': chapter_files
        })
    return parts

def extract_draft(file_path, draft_label):
    # Match the specific draft label used in the files: YOUNG_ADULT or 13_PLUS
    # The file has ## Draft (YOUNG_ADULT) or ## Draft (13_PLUS)
    if not os.path.exists(file_path):
        return ""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match ## Draft (Label) until the next ## or end of file
    pattern = rf'## Draft \({draft_label}\)(.*?)(?=\n## |$)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def extract_title(file_path):
    if not os.path.exists(file_path):
        return os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.readline()
        if line.startswith('# '):
            return line.strip()
    return os.path.basename(file_path)

def build_manuscript(draft_label, output_file, parts):
    version_path = os.path.join(repo_root, 'VERSION')
    version = "0.0.0"
    if os.path.exists(version_path):
        with open(version_path, 'r') as vf:
            version = vf.read().strip()

    full_text = f"# Forgotten Future: Full Manuscript ({draft_label.replace('_', ' ')})\n"
    full_text += f"> Draft Version: {version}\n\n"
    
    for part in parts:
        full_text += f"# {part['title']}\n\n*{part['synopsis']}*\n\n---\n\n"
        
        for filename in part['chapters']:
            path = os.path.join(chapters_dir, filename)
            if not os.path.exists(path):
                print(f"Warning: {path} not found.")
                continue
                
            title = extract_title(path)
            draft = extract_draft(path, draft_label)
            
            full_text += f"{title}\n\n{draft}\n\n---\n\n"
    
    output_path = os.path.join(manuscript_dir, output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    if not os.path.exists(manuscript_dir):
        os.makedirs(manuscript_dir)
    
    parts = parse_index()
    if not parts:
        print("Error: Could not parse parts from INDEX.md")
        exit(1)
        
    build_manuscript("YOUNG_ADULT", "MANUSCRIPT_YOUNG_ADULT.md", parts)
    build_manuscript("13_PLUS", "MANUSCRIPT_13_PLUS.md", parts)
