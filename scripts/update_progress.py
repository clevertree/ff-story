#!/usr/bin/env python3
"""
Update **YA Progress:** and **13+ Progress:** in all chapter files.
Target: 62,000 words for the book; 62 chapters → 1000 words per chapter.
Format: **YA Progress:** X% (N/1000 words) and **13+ Progress:** Y% (M/1000 words)
"""
import re
from pathlib import Path

CHAPTERS_DIR = Path(__file__).resolve().parent.parent / "chapters"
GOAL_WORDS = 1000  # 62000 / 62 chapters


def count_words(text: str) -> int:
    """Count words; strip HTML comments for prose-only count."""
    # Remove <!-- ... --> (single and multiline)
    cleaned = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Split on whitespace and count non-empty tokens
    return len(cleaned.split())


def extract_section_content(full_text: str, section_header: str) -> str:
    """Extract content from section_header to the next ## or end of file."""
    pattern = re.escape(section_header) + r"\s*\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, full_text, re.DOTALL)
    return m.group(1).strip() if m else ""


def get_ya_and_13_counts(filepath: Path) -> tuple[int, int]:
    text = filepath.read_text(encoding="utf-8")
    ya_content = extract_section_content(text, "## Draft (YOUNG_ADULT)")
    plus_content = extract_section_content(text, "## Draft (13_PLUS)")
    return count_words(ya_content), count_words(plus_content)


def update_progress_in_content(content: str, ya_words: int, plus_words: int) -> str:
    ya_pct = min(100, round(100 * ya_words / GOAL_WORDS))
    plus_pct = min(100, round(100 * plus_words / GOAL_WORDS))
    ya_line = f"**YA Progress:** {ya_pct}% ({ya_words}/{GOAL_WORDS} words)"
    plus_line = f"**13+ Progress:** {plus_pct}% ({plus_words}/{GOAL_WORDS} words)"

    # Replace any existing **YA Progress:** ... or **YA Progress: 12.0%** (variants)
    content = re.sub(
        r"\*\*YA Progress:\s*[^\n]*",
        ya_line,
        content,
        count=1,
    )
    content = re.sub(
        r"\*\*13\+ Progress:\s*[^\n]*",
        plus_line,
        content,
        count=1,
    )
    return content


def main():
    chapter_files = sorted(CHAPTERS_DIR.glob("chapter_*.md"))
    for f in chapter_files:
        ya_words, plus_words = get_ya_and_13_counts(f)
        content = f.read_text(encoding="utf-8")
        new_content = update_progress_in_content(content, ya_words, plus_words)
        if new_content != content:
            f.write_text(new_content, encoding="utf-8")
            print(f"Updated {f.name}: YA {ya_words}, 13+ {plus_words}")
    print(f"Done. Per-chapter goal: {GOAL_WORDS} words (62k total / 62 chapters).")


if __name__ == "__main__":
    main()
