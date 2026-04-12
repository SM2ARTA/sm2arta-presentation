"""Move slide 5 (Introducing) to position 22, renumber all affected slide numbers."""
import re
from pathlib import Path

PATH = Path(r"C:\Users\abram\OneDrive\Desktop\SM2ARTA_Presentation\index.html")
text = PATH.read_text(encoding="utf-8")

# 1. Locate slide 5 block: from its comment up to slide 6's comment
pat5 = re.compile(
    r'(<!-- ={3,} 5\..*?-->.*?)(?=<!-- ={3,} 6\.)',
    flags=re.DOTALL,
)
m5 = pat5.search(text)
if not m5:
    raise SystemExit("Could not locate slide 5 block")
slide5_block = m5.group(1)
print(f"Slide 5 block length: {len(slide5_block)}")

# 2. Remove slide 5 from original position
text = text[:m5.start()] + text[m5.end():]

# 3. Renumber slides 6..22 DOWN by 1 in their slnum badges.
# Slnum pattern: <text ... >N</text></g>  inside translate(1210, 660) block
# Strategy: walk through slnum numbers in document order (which are now slides 2,3,4,6,7,...22 mapped to 2,3,4,5,...21)
# Simpler: directly rewrite slnum numbers by finding them in order.

slnum_re = re.compile(
    r'(<g transform="translate\(1210, 660\)"><use href="#slnum"/>'
    r'<text x="18" y="26" font-size="15" font-weight="700" fill="#FFFFFF" text-anchor="middle">)(\d+)(</text></g>)'
)

# After removing slide 5, the remaining slides have numbers: 2,3,4,6,7,8,...,22 (slide 23 stays)
# These should become: 2,3,4,5,6,7,...,21
# So any number 6..22 should be decremented by 1.
# (Slide 23 stays as 23 since we'll insert new slide 22 before it.)

def decrement_if_in_range(m):
    n = int(m.group(2))
    if 6 <= n <= 22:
        return f"{m.group(1)}{n-1}{m.group(3)}"
    return m.group(0)

text = slnum_re.sub(decrement_if_in_range, text)
print("Decremented slnum 6..22 by 1")

# 4. Update slide 5 block: its own slnum should become 22, comment reflect new position
# Update comment in the moved block
slide5_block_updated = re.sub(
    r'<!-- ={3,} 5\. ([^=]+?) ={3,} -->',
    r'<!-- ==================== 22. \1 ==================== -->',
    slide5_block,
)
# Update slnum inside moved block: 5 -> 22
slide5_block_updated = slnum_re.sub(
    lambda m: f"{m.group(1)}22{m.group(3)}" if int(m.group(2)) == 5 else m.group(0),
    slide5_block_updated,
)

# 5. Insert the updated slide-5 block BEFORE slide 23 (closing)
# Find slide 23's opening comment
insert_re = re.compile(r'<!-- ={3,} 23\.')
m23 = insert_re.search(text)
if not m23:
    raise SystemExit("Could not locate slide 23 insertion point")

text = text[:m23.start()] + slide5_block_updated + text[m23.start():]
print(f"Inserted moved block before slide 23")

# 6. Also re-number the other slide-section HTML comments for consistency (6→5, 7→6, etc.)
# Need to be careful not to double-apply. Pattern: <!-- ==================== N. NAME ==================== -->
comment_re = re.compile(
    r'<!-- ={3,} (\d+)\. ([^=]+?) ={3,} -->'
)

# We want to renumber comments that currently say 6..22 -> 5..21.
# But after step 5, the moved block (now physically sitting between old slide 22 and slide 23)
# already has comment "22. INTRODUCING" which is correct.
# We need to renumber the OTHER slides' comments: old 6..22 -> 5..21.
# Those comments are the ones with numbers 6..22 that come BEFORE the moved block.

# Find position of moved "22. INTRODUCING" comment so we can bound the region to renumber
moved_match = re.search(r'<!-- ={3,} 22\. INTRODUCING ={3,} -->', text)
if moved_match is None:
    # Fallback: match on the INTRODUCING text alone
    moved_match = re.search(r'<!-- ={3,} 22\. [A-Z]+ ={3,} -->', text)

region_end = moved_match.start() if moved_match else len(text)
before = text[:region_end]
after = text[region_end:]

def shift_comment(m):
    n = int(m.group(1))
    if 6 <= n <= 22:
        return f'<!-- ==================== {n-1}. {m.group(2).strip()} ==================== -->'
    return m.group(0)

before = comment_re.sub(shift_comment, before)
text = before + after
print("Renumbered HTML comments 6..22 to 5..21")

PATH.write_text(text, encoding="utf-8")
print("DONE. Slide 5 moved to position 22.")
