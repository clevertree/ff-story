import os
import re

def build_manuscripts():
    chapters_dir = '/home/ari/dev/ff/ff-story/chapters'
    ya_dir = '/home/ari/dev/ff/ff-story/manuscript/ya'
    plus_dir = '/home/ari/dev/ff/ff-story/manuscript/13plus'

    files = sorted([f for f in os.listdir(chapters_dir) if f.endswith('.md')])

    for filename in files:
        path = os.path.join(chapters_dir, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract Title
        title_match = re.search(r'^# (.*)', content)
        title = title_match.group(1) if title_match else filename

        # Extract YA Draft
        # Matches from ## Draft (YA Version) to the next ## header or end of file
        ya_match = re.search(r'## Draft \(YA Version\)\n\n(.*?)(?=\n##|$)', content, re.DOTALL)
        ya_draft = ya_match.group(1).strip() if ya_match else ""

        # Extract 13+ Draft
        plus_match = re.search(r'## Draft \(13\+ Version\)\n\n(.*?)(?=\n##|$)', content, re.DOTALL)
        plus_draft = plus_match.group(1).strip() if plus_match else ""

        # Write YA Version
        ya_file = os.path.join(ya_dir, filename)
        with open(ya_file, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n{ya_draft}")

        # Write 13+ Version
        plus_file = os.path.join(plus_dir, filename)
        with open(plus_file, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n{plus_draft}")

    print(f"Built {len(files)} chapters in YA and 13+ folders.")

if __name__ == "__main__":
    build_manuscripts()
