"""Fix Context Bar layout: middle phrase centered, end phrase flush to 1220.
Preserves existing content text for each slide."""
import re
from pathlib import Path

PATH = Path(r"C:\Users\abram\OneDrive\Desktop\SM2ARTA_Presentation\index.html")
ARROW = "\u2192"

def rebuild_bar(start, middle, end):
    return (
        '<g class="ctxbar">\n'
        '    <rect x="60" y="650" width="1160" height="1" fill="#EEEEEE"/>\n'
        f'    <text x="60" y="687" font-size="13" font-family="DM Sans" fill="#1A1A1A" font-weight="700">{start}</text>\n'
        f'    <text x="395" y="687" font-size="14" font-family="DM Sans" fill="#D4D4D4" font-weight="400" text-anchor="middle">{ARROW}</text>\n'
        f'    <text x="640" y="687" font-size="13" font-family="DM Sans" fill="#707070" font-weight="400" text-anchor="middle">{middle}</text>\n'
        f'    <text x="885" y="687" font-size="14" font-family="DM Sans" fill="#D4D4D4" font-weight="400" text-anchor="middle">{ARROW}</text>\n'
        f'    <text x="1180" y="687" font-size="13" font-family="DM Sans" fill="#1A1A1A" font-weight="700" text-anchor="end">{end}</text>\n'
        '  </g>'
    )

text = PATH.read_text(encoding="utf-8")

# Match any existing ctxbar block, capture the 3 phrase values
block_re = re.compile(
    r'<g class="ctxbar">'
    r'.*?font-weight="700">([^<]*)</text>'          # start
    r'.*?text-anchor="middle">[^<]*</text>'          # arrow 1
    r'.*?font-weight="400"[^>]*>([^<]*)</text>'      # middle
    r'.*?text-anchor="middle">[^<]*</text>'          # arrow 2
    r'.*?text-anchor="end">([^<]*)</text>'           # end
    r'\s*</g>',
    flags=re.DOTALL,
)

count = 0
def replace_block(m):
    global count
    count += 1
    start, middle, end = m.group(1), m.group(2), m.group(3)
    return rebuild_bar(start, middle, end)

text = block_re.sub(replace_block, text)
PATH.write_text(text, encoding="utf-8")
print(f"Rebuilt {count} Context Bars with centered middle phrase.")
