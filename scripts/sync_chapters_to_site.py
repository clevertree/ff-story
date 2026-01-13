import os
import re

def generate_chapters_ts():
    manuscript_dir = "/home/ari/dev/ff/ff-story/manuscript/text"
    output_file = "/home/ari/dev/ff/forgotten-future-site/app/manuscript/full-text/chapters.ts"
    
    files = sorted([f for f in os.listdir(manuscript_dir) if f.startswith("chapter_") and f.endswith(".md")])
    
    chapters = []
    
    for filename in files:
        filepath = os.path.join(manuscript_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract title from the first line
        first_line = content.split('\n')[0]
        # Match "# Chapter X: Title" or "# Chapter X: Title - something"
        # We want the Title part.
        match = re.search(r'# Chapter \d+:\s*(.*)', first_line)
        if match:
            title = match.group(1).strip()
        else:
            # Fallback to filename
            title = filename.replace("chapter_", "").replace(".md", "").replace("_", " ").title()
            # Remove digits from the start of title
            title = re.sub(r'^\d+\s*', '', title)

        # Extract ID from filename
        id_match = re.search(r'chapter_(\d+)', filename)
        chapter_id = int(id_match.group(1)) if id_match else 0
        
        # Escape backticks in content for TS template literal
        escaped_content = content.replace('`', '\\`').replace('${', '\\${')
        
        chapters.append({
            "id": chapter_id,
            "title": title,
            "content": escaped_content
        })
    
    # Sort by ID
    chapters.sort(key=lambda x: x["id"])
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("export interface Chapter {\n")
        f.write("  id: number;\n")
        f.write("  title: string;\n")
        f.write("  content: string;\n")
        f.write("}\n\n")
        f.write("export const chapters: Chapter[] = [\n")
        
        for i, ch in enumerate(chapters):
            f.write("  {\n")
            f.write(f"    id: {ch['id']},\n")
            f.write(f"    title: `{ch['title']}`,\n")
            f.write(f"    content: `{ch['content']}`\n")
            f.write("  }")
            if i < len(chapters) - 1:
                f.write(",")
            f.write("\n")
            
        f.write("];\n")

if __name__ == "__main__":
    generate_chapters_ts()
