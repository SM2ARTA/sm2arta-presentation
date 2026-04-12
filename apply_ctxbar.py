"""Rebuild Context Bars as natural flow taglines. Replaces the labeled three-column version."""
import re
from pathlib import Path

PATH = Path(r"C:\Users\abram\OneDrive\Desktop\SM2ARTA_Presentation\index.html")

# Each slide: (start_bold, middle_muted, end_bold)
FLOW = {
    1:  ("Internal FIFA presentation", "Strategic briefing",         "FWC 2026 readiness"),
    2:  ("Platform",                    "6+ years in production",     "Trusted by FIFA"),
    3:  ("Single platform",             "End-to-end orchestration",   "Optimized resources"),
    4:  ("Every event",                 "Tailored configuration",     "Fit for purpose"),
    5:  ("Multiuser system",            "Web-based access",           "Live demo available"),
    6:  ("8 capabilities",              "Cloud-based & secure",       "Enterprise-ready"),
    7:  ("7 steps",                     "Scoping to reconciliation",  "Full lifecycle visibility"),
    8:  ("5 enhancements",              "Built for FWC 2026",         "Deployment-ready"),
    9:  ("Platform modernized",         "New architecture",           "Proven at scale"),
    10: ("Laravel \u00b7 PostgreSQL",   "Fully dockerized",           "High performance"),
    11: ("OVH Frankfurt",               "ISO 27001 certified",        "GDPR compliant"),
    12: ("Cloudflare Pro",              "DDoS & WAF",                 "OWASP Top 10 blocked"),
    13: ("Referential protection",      "Cascade prevention",         "No data loss"),
    14: ("6 productivity tools",        "Automated workflows",        "Faster decisions"),
    15: ("3 RBAC roles",                "Segregation of duties",      "Least privilege"),
    16: ("8 controls",                  "Continuous reviews",         "Auditable by design"),
    17: ("TLS 1.2+ \u00b7 AES-256",     "CipherSweet + Vault",        "Zero plaintext exposure"),
    18: ("Peer-reviewed code",          "CI/CD pipelines",            "Controlled releases"),
    19: ("4 monitored layers",          "Real-time logs",             "Full traceability"),
    20: ("Monthly patches",             "Automated scans",            "72h critical SLA"),
    21: ("No inbound email",            "SPF \u00b7 DKIM \u00b7 DMARC","ClamAV scanning"),
    22: ("5 milestones",                "Iterative delivery",         "Continuous improvement"),
    23: ("Questions welcome",           "Next steps aligned",         "Ready to deploy"),
}

ARROW = "\u2192"  # →

def bar(start, middle, end):
    """Build the flow Context Bar SVG — phrases spread across full bar width, middle centered."""
    return (
        '<g class="ctxbar">\n'
        '    <rect x="60" y="650" width="1160" height="1" fill="#EEEEEE"/>\n'
        f'    <text x="60" y="687" font-size="13" font-family="DM Sans" fill="#1A1A1A" font-weight="700">{start}</text>\n'
        f'    <text x="395" y="687" font-size="14" font-family="DM Sans" fill="#D4D4D4" font-weight="400" text-anchor="middle">{ARROW}</text>\n'
        f'    <text x="640" y="687" font-size="13" font-family="DM Sans" fill="#707070" font-weight="400" text-anchor="middle">{middle}</text>\n'
        f'    <text x="885" y="687" font-size="14" font-family="DM Sans" fill="#D4D4D4" font-weight="400" text-anchor="middle">{ARROW}</text>\n'
        f'    <text x="1220" y="687" font-size="13" font-family="DM Sans" fill="#1A1A1A" font-weight="700" text-anchor="end">{end}</text>\n'
        '  </g>'
    )

text = PATH.read_text(encoding="utf-8")

# Match any existing <g class="ctxbar">...</g> block and replace with the new flow bar.
ctxbar_re = re.compile(
    r'<g class="ctxbar">.*?</g>',
    flags=re.DOTALL,
)

# Find all ctxbar blocks in order; each corresponds to a slide number.
# Slides 1..23 in document order.
matches = list(ctxbar_re.finditer(text))
print(f"Found {len(matches)} existing Context Bars")

if len(matches) != 23:
    print(f"WARN: expected 23, got {len(matches)}")

# Replace from last to first to keep offsets valid
for i, m in enumerate(reversed(matches)):
    slide_num = 23 - i  # reversed order
    start, middle, end = FLOW[slide_num]
    new_block = bar(start, middle, end)
    text = text[:m.start()] + new_block + text[m.end():]

PATH.write_text(text, encoding="utf-8")
print("Context Bars rewritten as natural flow taglines.")
