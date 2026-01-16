import os
import re

chapters_dir = '/home/ari/dev/ff/ff-story/chapters'
manuscript_dir = '/home/ari/dev/ff/ff-story/manuscript'

def get_chapter_files():
    files = [f for f in os.listdir(chapters_dir) if f.startswith('chapter_') and f.endswith('.md')]
    return sorted(files)

def extract_draft(file_path, draft_label):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match ## Draft (LABEL) until the next ## or end of file
    pattern = rf'## Draft \({draft_label}\)(.*?)(?=\n## |$)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def extract_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.readline()
        if line.startswith('# '):
            return line.strip()
    return os.path.basename(file_path)

def build_manuscript(draft_label, output_file):
    full_text = f"# Forgotten Future: Full Manuscript ({draft_label})\n\n"
    
    for filename in get_chapter_files():
        path = os.path.join(chapters_dir, filename)
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
    
    build_manuscript("YOUNG_ADULT", "MANUSCRIPT_YOUNG_ADULT.md")
    build_manuscript("13_PLUS", "MANUSCRIPT_13_PLUS.md")
