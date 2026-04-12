# SM2ARTA™ Presentation Guidebook

**Version:** 1.0
**Owner:** SM2ARTA LLC
**Last updated:** 2026-04-12
**Status:** LOCKED — treat as strict law for all SM2ARTA™ presentations.

---

## Purpose

This guidebook defines the presentation system for SM2ARTA™ — an enterprise logistics and materials management platform. It is NOT a style guide for individual slides. It is a **system that generates slides**.

Every slide in any SM2ARTA™ presentation (marketing, internal, audit, FIFA briefing, etc.) must conform to this system. No creative variation. No new styles unless defined here.

---

## 1. Design Philosophy

**Tone:** Structured · Operational · Precise · Enterprise · No fluff.

SM2ARTA™ is mission-critical software used at FIFA World Cup. Presentations must read like **operations documents**, not marketing decks.

**Principles:**
1. **Clarity over decoration** — every element must earn its place
2. **Repetition over creativity** — consistency is the brand
3. **Whitespace over density** — pages breathe
4. **Facts over adjectives** — numbers, names, versions — not superlatives
5. **System over slide** — never design one slide; build a layout that applies

---

## 2. Typography System

**Font:** DM Sans only. Weights in use: 400 / 500 / 700 / 800.

### Type scale

| Element | Size | Weight | Case | Color |
|---|---|---|---|---|
| Slide title | 48px | 800 | UPPERCASE | `#1A1A1A` (1 accent word in `#E50D28`) |
| Eyebrow | 11px | 700 | UPPERCASE · 0.22em tracking | `#E50D28` |
| Hero brand (cover) | 46px | 800 | Mixed (SM²ARTA) | `#1A1A1A` |
| Body paragraph | 15px | 400 | Sentence | `#333` |
| Card title | 15px | 700 | Title Case | `#1A1A1A` |
| Card body | 12px | 400 | Sentence | `#707070` |
| Node label | 12px | 700 | UPPERCASE · 0.05em | `#1A1A1A` |
| Node body | 11px | 400 | Sentence | `#707070` |
| Feature cell label | 13px | 800 | UPPERCASE · 0.08em | `#E50D28` |
| Feature cell body | 12px | 400 | Sentence · max 6 words | `#707070` |
| Category label | 10px | 700 | UPPERCASE · 0.2em | `#999` |
| Footer chip label | 9px | 700 | UPPERCASE · 0.16em | `#999` |
| Footer chip value | 14px | 700 | Title Case | `#1A1A1A` |

### Rules

- **Titles:** max 5 words, UPPERCASE, exactly one red accent word (the most meaningful word).
- **Eyebrow:** 1–2 words max, labels the section type.
- **Body paragraphs:** max 25 words.
- **Card body:** max 14 words.
- **Italics:** only for acronym expansions (e.g., *System for Materials Management and Asset Tracking*).
- **No underlines** except inline links.

---

## 3. Brand Mark Usage

### SM2ARTA™ rendering rules

**Every occurrence** of SM2ARTA must use:
- Uppercase `SM`
- Superscript `²` (not the digit 2 inline)
- Uppercase `ARTA`
- Superscript `™` in muted gray (`#707070` or `#999`), size ≈ 35–40% of the main text size
- No space between `ARTA` and `™`; use `dx="2"` in SVG

**SVG example:**
```xml
<text font-size="48" font-weight="800">
  SM<tspan baseline-shift="super" font-size="28">2</tspan>ARTA<tspan baseline-shift="super" font-size="18" dx="2" fill="#999" font-weight="600">&#8482;</tspan>
</text>
```

**HTML example:**
```html
SM<sup>2</sup>ARTA<sup style="font-size:0.6em;color:#999">&trade;</sup>
```

**When to use ™ vs ®:**
- **™** — while trademark application is pending (current state)
- **®** — only after USPTO grants registration

**Tag line:** whenever SM2ARTA™ is introduced for the first time on a slide, it may be followed by the acronym expansion in muted italic:
> *System for Materials Management and Asset Tracking*

---

## 4. Layout System

**Eight fixed layouts. No exceptions.**

### L1 — COVER
**Purpose:** Opens the deck. Used once, on slide 1.
**Structure:**
- Header (logo + rule + year)
- Brand (SM2ARTA™) 46px + acronym caption
- Headline ≤8 words
- Tagline 1 line
- 3 stat columns
- Trust line ("FIFA World Cup 2022 · 2026")
- Hero illustration (right, inside gray circle)

### L2 — DEFINITION
**Purpose:** Explains what something is. Used for "What is X?" slides.
**Structure:**
- Eyebrow + title + red rule
- 1 description paragraph (max 35 words)
- 3 pillar cards in horizontal row with connecting arrows
- Optional footer chip strip (3 stats or credentials)

### L3 — PROCESS FLOW
**Purpose:** Linear sequence of steps or stages.
**Structure:**
- Eyebrow + title + red rule
- Horizontal bar with 3–7 numbered nodes (red circles)
- Alternating top/bottom labels
- Each node: UPPERCASE label (≤2 words) + 1-sentence description (≤12 words)

### L4 — FEATURE GRID
**Purpose:** Parallel features/capabilities/controls. No hierarchy.
**Structure:**
- Eyebrow + title + red rule
- Grid of identical cards: 4×2, 3×2, 2×3, or 2×2
- Each card: icon chip + title + 1-sentence description
- Cards MUST be equal size — no wide cards, no varied heights

### L5 — DETAIL LIST
**Purpose:** Numbered or itemized content with explanation. Use for technical breakdowns.
**Structure:**
- Eyebrow + title + red rule
- 3–5 full-width cards stacked vertically
- Each card: numbered badge + card title + 1-sentence description (≤18 words)
- All cards identical width and height

### L6 — PROFILE CARDS
**Purpose:** Roles, people, or distinct entity profiles.
**Structure:**
- Eyebrow + title + red rule + optional intro sentence
- 2–3 profile cards with: circular avatar, title (UPPERCASE, max 3 words), short description

### L7 — STATEMENT
**Purpose:** Single focal message. Used for introductions or transitions.
**Structure:**
- Eyebrow + title + red rule
- One large statement (max 20 words)
- One CTA or supporting visual

### L8 — CLOSING
**Purpose:** Thank you / end of deck.
**Structure:**
- Brand + acronym
- "THANK YOU" (max 2 words)
- "Questions?" prompt in red
- Trust line
- Hero illustration

---

## 5. Content Rules

| Rule | Limit |
|---|---|
| Max words per slide (total) | 80 |
| Max bullets per slide | 5 |
| Max words per bullet | 14 |
| Max cards per slide | 8 |
| Max levels of hierarchy | 2 (title + body) |
| Max icons per slide | 8 |

**Paragraphs:** only allowed on L1 (cover), L2 (definition), L7 (statement) intro, L8 (closing). All other layouts use fragments, not sentences.

**Jargon:** technical terms allowed (PostgreSQL, CipherSweet, etc.) — this is an enterprise system audience.

---

## 6. Visual Rules

### Color palette (locked — 6 colors)

| Token | Hex | Use |
|---|---|---|
| Red primary | `#E50D28` | Accent, 1 word per title, rules, key icons |
| Red tint | `#FCE6E9` | Icon chip fill only |
| Ink | `#1A1A1A` | Titles, emphasis text |
| Body | `#333333` | Paragraph text |
| Muted | `#707070` | Secondary text |
| Muted soft | `#999999` | Labels |
| Line | `#E6E6E6` | Dividers |
| White | `#FFFFFF` | Background |

**Forbidden:** gradients (except original logo), drop shadows deeper than `0 4px 12px rgba(0,0,0,0.05)`, neon, dark backgrounds, any color not listed.

### Alignment

- Titles: left-aligned, x=60
- Body: left-aligned
- Cards: aligned to 60px left grid, 20px internal padding
- Never center unless specified for nodes (process flow node labels, role cards)

### Icons

- Lucide style only, 1.6px stroke, round linecaps
- Inside red-tint 36×36 chip (inline contexts), OR white icon inside 60px red circle (feature grid hero icons)
- No emoji. No Material Icons. No Font Awesome.

### Spacing grid

| Element | Value |
|---|---|
| Slide margin | 60px sides / 40px top / 40px bottom |
| Title-to-content | 30px |
| Between cards | 16px |
| Card padding | 20px |
| Paragraph max width | 900px (readability) |

### Signature elements (must appear on every content slide)

1. **Header bar** (top-left): logo + red rule (42×4px) + year
2. **Dot grid** (top-right): 10×4 red dots, 16px spacing
3. **Eyebrow** (above title): red uppercase label
4. **Red rule** (under title): 72×3px
5. **Slide number badge** (bottom-right): red shape with notched corner + white number

---

## 7. Consistency Rules

- All titles identical style and position.
- All eyebrows identical.
- All rules identical.
- All slide numbers identical.
- Every content slide has the header, dot grid, and slide number.
- L1 and L8 may omit the eyebrow and slide number.
- SM2ARTA™ rendered identically everywhere (see §3).

---

## 8. Validation Checklist

Before any slide ships:

- [ ] Uses one of L1–L8 layouts
- [ ] Eyebrow present (unless L1/L8)
- [ ] Title ≤5 words, UPPERCASE, one red accent
- [ ] Red rule (72×3px) under title
- [ ] Total word count ≤80
- [ ] Uses only the 8 approved colors
- [ ] Icons match Lucide 1.6px style
- [ ] Slide number badge present (unless L1/L8)
- [ ] SM2ARTA™ rendered with ² and ™
- [ ] Content fits within y=230–620
- [ ] No creative deviation from layout spec
- [ ] No shadows beyond the approved depth
- [ ] No gradient fills

---

## 9. Approved Slide Index (FIFA FWC 2026 deck)

| # | Title | Layout |
|---|---|---|
| 1 | Cover | L1 |
| 2 | WHAT IS SM²ARTA? | L2 |
| 3 | STREAMLINE THE SUPPLY CHAIN | L3 |
| 4 | CUSTOMIZATION | L4 |
| 5 | KEY FEATURES | L4 |
| 6 | SM²ARTA™ PROCESS | L3 |
| 7 | WHAT'S NEW FOR FWC 2026 | L5 |
| 8 | FWC 2022 → FWC 2026 | L5 |
| 9 | ARCHITECTURE OVERVIEW | L5 |
| 10 | HOSTING & INFRASTRUCTURE | L5 |
| 11 | WEB APPLICATION FIREWALL | L4 |
| 12 | DATA INTEGRITY | L2 |
| 13 | USABILITY | L4 |
| 14 | ROLES | L6 |
| 15 | SECURITY CONTROLS | L4 |
| 16 | DATA ENCRYPTION | L5 |
| 17 | CHANGE MANAGEMENT | L5 |
| 18 | LOGGING & RESPONSE | L5 |
| 19 | MAINTENANCE & SCANNING | L5 |
| 20 | EMAIL & FILE SECURITY | L2 |
| 21 | ROADMAP | L3 |
| 22 | SEE IT IN ACTION (Live Demo) | L7 |
| 23 | Closing | L8 |

---

## 11. Title & Closing Slide Standardization (v1.1)

**Opening frame (L1 COVER) and Closing frame (L8 CLOSING) are a matched pair. They must be visually indistinguishable in structure — only content differs.**

### Shared skeleton (locked y-positions)

| y | Element | Title slide | Closing slide |
|---|---|---|---|
| 42 | Header bar | logo + rule + year | logo + rule + year |
| 44 | Dot grid (top-right) | present | present |
| 180 | Brand `SM²ARTA™` | 38px / 800 / ink | 38px / 800 / ink |
| 212 | Acronym caption | muted uppercase, 0.08em | muted uppercase, 0.08em |
| 290 | Main title (line 1) | 42px / 800 / UPPERCASE / max 6 words | same |
| 340 | Main title (line 2 opt) | same | same |
| 370 | Red rule | 72×3 | 72×3 |
| 410 | Subtitle | 16px / sentence case / 1 line | 16px / sentence case / 1 line |
| 475 | Thin divider | 460×1 `#E6E6E6` | 460×1 `#E6E6E6` |
| 510 | Three-column block | stats | mirrored stats |
| 640 | Context line | FIFA WC 2022 · 2026 | FIFA WC 2022 · 2026 |
| — | Right half | hero image in gray circle | hero image in gray circle |

### Rules

- **Alignment:** left-aligned only. All text x=60.
- **Title:** ALL CAPS, max 6 words, one red accent word (or none). No punctuation unless essential.
- **Subtitle:** optional, sentence case, 1 line, max 8 words.
- **Content block:** three columns mirrored between slides (numeric callouts).
- **Hero image:** centered inside `#F2F2F2` circle (r=290, cx=950, cy=400) on BOTH slides.
- **Slide number:** OMITTED from both (first/last frames are unnumbered).
- **Eyebrow:** OMITTED from both (the brand mark replaces the eyebrow on framing slides).

### Title slide — content template

- Title: product or platform definition (e.g. `EVENTS MATERIAL PLANNING & ASSET MANAGEMENT`)
- Subtitle: mission statement (e.g. `Maximize your event success`)
- Three columns: track record stats (years · major events · medium events)
- Context: deployment context (e.g. `FIFA World Cup 2022 · 2026`)

### Closing slide — content template

- Title: operational closure statement (e.g. `SYSTEM READY FOR EXECUTION`)
- Subtitle: handoff prompt (e.g. `Questions and discussion welcome`)
- Three columns: readiness stats mirrored vs opening (proven · deployed · modules live)
- Context: same line as title slide (maintains framing symmetry)

### Forbidden on both

- Large decorative “THANK YOU” typography (non-systemic).
- Different alignment, sizing, or grid between the two.
- Decorative elements present on only one.
- Paragraphs or multi-line subtitles.
- Any font size, color, or layout not defined in §2–§6.

### Validation

Before shipping Title or Closing slide, hold them **side by side**. If any structural element differs in position or size, rebuild.

---

## 12. SM2ARTA Context Bar — Flow (v1.4)

The Context Bar is a **subtle tagline** that runs along the bottom of every slide. It reads as one natural thought, not a data form.

### Visual structure

A single horizontal line of text. Three phrases connected by light arrows (`→`). No labels, no boxes, no icons.

```
Statement  →  Supporting context  →  Outcome
```

- Starting phrase: **Semibold, ink** — the anchor
- Middle phrase: regular, muted gray — the bridge
- Closing phrase: **Semibold, ink** — the payoff
- Arrows: very light gray (`#DDDDDD`), low-emphasis connectors

### Fixed positions

| y | Element |
|---|---|
| 650 | Divider 1px `#EEEEEE`, x=60 → x=1220 |
| 687 | Text baseline |
| 660 | Slide-number badge (right edge) |

### Typography

- Font: DM Sans, 13px
- Bold phrases: weight 700, color `#1A1A1A`
- Middle phrase: weight 400, color `#707070`
- Arrows: `→` character, weight 400, color `#D4D4D4`
- Spacing between phrases: 14px
- Sentence case (not UPPERCASE) — reads naturally

### Applied to content slides only (2–22)

**Not used** on Title (L1) or Closing (L8) — those frames have their own dedicated structure per §11.

| # | Slide | Context Bar |
|---|---|---|
| 2 | What is SM²ARTA? | **Platform** → 6+ years in production → **Trusted by FIFA** |
| 3 | Streamline the Supply Chain | **Single platform** → End-to-end orchestration → **Optimized resources** |
| 4 | Customization | **Every event** → Tailored configuration → **Fit for purpose** |
| 5 | Introducing | **Multiuser system** → Web-based access → **Live demo available** |
| 6 | Key Features | **8 capabilities** → Cloud-based & secure → **Enterprise-ready** |
| 7 | SM²ARTA™ Process | **7 steps** → Scoping to reconciliation → **Full lifecycle visibility** |
| 8 | What's New for FWC 2026 | **5 enhancements** → Built for FWC 2026 → **Deployment-ready** |
| 9 | FWC 2022 → FWC 2026 | **Platform modernized** → New architecture → **Proven at scale** |
| 10 | Architecture Overview | **Laravel · PostgreSQL** → Fully dockerized → **High performance** |
| 11 | Hosting & Infrastructure | **OVH Frankfurt** → ISO 27001 certified → **GDPR compliant** |
| 12 | Web Application Firewall | **Cloudflare Pro** → DDoS & WAF → **OWASP Top 10 blocked** |
| 13 | Data Integrity | **Referential protection** → Cascade prevention → **No data loss** |
| 14 | Usability | **6 productivity tools** → Automated workflows → **Faster decisions** |
| 15 | Roles | **3 RBAC roles** → Segregation of duties → **Least privilege** |
| 16 | Security Controls | **8 controls** → Continuous reviews → **Auditable by design** |
| 17 | Data Encryption | **TLS 1.2+ · AES-256** → CipherSweet + Vault → **Zero plaintext exposure** |
| 18 | Change Management | **Peer-reviewed code** → CI/CD pipelines → **Controlled releases** |
| 19 | Logging & Response | **4 monitored layers** → Real-time logs → **Full traceability** |
| 20 | Maintenance & Scanning | **Monthly patches** → Automated scans → **72h critical SLA** |
| 21 | Email & File Security | **No inbound email** → SPF · DKIM · DMARC → **ClamAV scanning** |
| 22 | Roadmap | **5 milestones** → Iterative delivery → **Continuous improvement** |

### Rules

- Single line, left-aligned, x=60.
- Three phrases only. No more, no less.
- Sentence case.
- Arrows (`→`) as connectors — never commas, pipes, or slashes.
- Must feel like a thought, not a data row.
- Must reinforce the slide's title, never repeat it verbatim.

### Forbidden

- Explicit labels (SIGNAL / CONTEXT / IMPACT).
- UPPERCASE text.
- Boxes, dividers between phrases, or column structure.
- Icons or decorative elements.
- Repeated content across slides.
- Centering or right-alignment.

### Validation

- [ ] Single flowing line at y=687?
- [ ] Three phrases with → arrows?
- [ ] First and last phrases bold `#1A1A1A`; middle muted `#707070`?
- [ ] Arrows light gray `#D4D4D4`?
- [ ] Sentence case (no UPPERCASE)?
- [ ] Content unique per slide?
- [ ] Feels like a tagline, not a data form?

---

## 10. Amendment Process

This guidebook is locked. If a real-world need arises that doesn't fit the system:

1. Do **not** create a one-off slide.
2. Propose an amendment (new layout, new token).
3. Approval from SM2ARTA LLC required before amendment.
4. If approved: update this document, bump version, then apply.

---

**End of Guidebook v1.0**
