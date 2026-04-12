"""Revert center_titles.py: restore eyebrow/title/underline to x=60 (left-anchored)."""
import re
from pathlib import Path

PATH = Path(r"C:\Users\abram\OneDrive\Desktop\SM2ARTA_Presentation\index.html")
text = PATH.read_text(encoding="utf-8")

# 1. Eyebrow: <text x="640" y="128" ... text-anchor="middle">
eyebrow_re = re.compile(
    r'<text x="640" y="128"([^>]*?) text-anchor="middle">',
)
text, n1 = eyebrow_re.subn(lambda m: f'<text x="60" y="128"{m.group(1)}>', text)

# 2. Title: <text x="640" y="178" font-size="48" ... text-anchor="middle">
title_re_48 = re.compile(
    r'<text x="640" y="178" font-size="48"([^>]*?) text-anchor="middle">',
)
text, n2a = title_re_48.subn(
    lambda m: f'<text x="60" y="178" font-size="48"{m.group(1)}>', text)

# Slide 2 variant (font-size="50")
title_re_50 = re.compile(
    r'<text x="640" y="178" font-size="50"([^>]*?) text-anchor="middle">',
)
text, n2b = title_re_50.subn(
    lambda m: f'<text x="60" y="178" font-size="50"{m.group(1)}>', text)

# 3. Underline: <rect x="604" y="198" width="72"...>
underline_re = re.compile(
    r'<rect x="604" y="198" width="72" height="3" fill="#E50D28"/>'
)
text, n3 = underline_re.subn(
    '<rect x="60" y="198" width="72" height="3" fill="#E50D28"/>',
    text,
)

PATH.write_text(text, encoding="utf-8")
print(f"Reverted: {n1} eyebrows, {n2a + n2b} titles, {n3} underlines.")
