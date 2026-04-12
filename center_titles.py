"""Center all slide title blocks (eyebrow + title + underline) across slides 2-22.
Grid/content blocks are left untouched — only the title banner is re-anchored to x=640.
"""
import re
from pathlib import Path

PATH = Path(r"C:\Users\abram\OneDrive\Desktop\SM2ARTA_Presentation\index.html")
text = PATH.read_text(encoding="utf-8")

# 1. Eyebrow: <text x="60" y="128" ...>TEXT</text>  →  x="640" text-anchor="middle"
eyebrow_re = re.compile(
    r'<text x="60" y="128"([^>]*?)>',
)
def fix_eyebrow(m):
    attrs = m.group(1)
    if 'text-anchor' in attrs:
        return m.group(0)
    return f'<text x="640" y="128"{attrs} text-anchor="middle">'
text, n1 = eyebrow_re.subn(fix_eyebrow, text)

# 2. Title: <text x="60" y="178" font-size="48" ...>
title_re = re.compile(
    r'<text x="60" y="178" font-size="48"([^>]*?)>',
)
def fix_title(m):
    attrs = m.group(1)
    if 'text-anchor' in attrs:
        return m.group(0)
    return f'<text x="640" y="178" font-size="48"{attrs} text-anchor="middle">'
text, n2 = title_re.subn(fix_title, text)

# 3. Underline: <rect x="60" y="198" width="72" height="3" fill="#E50D28"/>
underline_re = re.compile(
    r'<rect x="60" y="198" width="72" height="3" fill="#E50D28"/>'
)
text, n3 = underline_re.subn(
    '<rect x="604" y="198" width="72" height="3" fill="#E50D28"/>',
    text,
)

PATH.write_text(text, encoding="utf-8")
print(f"Centered: {n1} eyebrows, {n2} titles, {n3} underlines.")
