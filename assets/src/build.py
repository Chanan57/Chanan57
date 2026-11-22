"""Builds the SVG panels used by README.md, styled after cpguragain.com.

Run from the repo root:  python assets/src/build.py
Fonts (Geist, Geist Mono; SIL OFL) are embedded so the panels render the same everywhere.
"""
import base64
from pathlib import Path
from xml.sax.saxutils import escape as esc

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'

# ── Theme (mirrors the site's CSS variables) ──────────────────────────────
BG = '#09090B'
CARD = '#111115'
FG = '#F4F4F6'
MUTED = '#9F9FA8'
DIM = '#5E5E68'
GREEN = '#35E492'
CYAN = '#3DDCF5'
AMBER = '#FAB338'
W = 840  # panel width (matches the README column)

SANS = "Geist, 'Segoe UI', system-ui, -apple-system, sans-serif"
MONO = "'Geist Mono', ui-monospace, SFMono-Regular, Consolas, monospace"


def b64(name):
    return base64.b64encode((SRC / name).read_bytes()).decode()


FONTS = f"""
@font-face {{ font-family: Geist; font-weight: 100 900; src: url(data:font/woff2;base64,{b64('geist.woff2')}) format('woff2'); }}
@font-face {{ font-family: 'Geist Mono'; font-weight: 100 900; src: url(data:font/woff2;base64,{b64('geist-mono.woff2')}) format('woff2'); }}
"""

BASE_CSS = f"""
{FONTS}
.sans {{ font-family: {SANS}; }}
.mono {{ font-family: {MONO}; }}
.eyebrow {{ font-family: {MONO}; font-size: 11px; font-weight: 500; letter-spacing: .08em; fill: {MUTED}; text-transform: uppercase; }}
.h2 {{ font-family: {SANS}; font-size: 26px; font-weight: 600; letter-spacing: -.6px; fill: {FG}; }}
.enter {{ animation: enter .7s cubic-bezier(.23,1,.32,1) both; }}
.fade {{ animation: fade .6s ease both; }}
@keyframes enter {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: none; }} }}
@keyframes fade {{ from {{ opacity: 0; }} }}
@keyframes blink {{ 50% {{ opacity: 0; }} }}
@keyframes pulse {{ 0% {{ r: 5; opacity: .55; }} 100% {{ r: 16; opacity: 0; }} }}
@keyframes sweep {{ from {{ transform: translateX(-60%); }} to {{ transform: translateX(160%); }} }}
@media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
"""


def mono_w(text, size):
    """Geist Mono advance width is 0.6em."""
    return len(text) * size * 0.6


def wrap(text, limit):
    words, lines, cur = text.split(), [], ''
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) > limit:
            lines.append(cur)
            cur = w
        else:
            cur = f'{cur} {w}' if cur else w
    if cur:
        lines.append(cur)
    return lines


def svg(h, body, title, extra_css=''):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="{esc(title)}">
<title>{esc(title)}</title>
<style>{BASE_CSS}{extra_css}</style>
<defs>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#fff" fill-opacity=".08"/></pattern>
  <radialGradient id="gridmask-g" cx="50%" cy="0%" r="75%"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
  <mask id="gridmask"><rect width="{W}" height="{h}" fill="url(#gridmask-g)"/></mask>
  <radialGradient id="glow-g" cx="28%" cy="0%" r="60%"><stop offset="0" stop-color="{GREEN}" stop-opacity=".13"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></radialGradient>
  <radialGradient id="glow-c" cx="88%" cy="4%" r="45%"><stop offset="0" stop-color="{CYAN}" stop-opacity=".08"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
  <linearGradient id="scan" x1="0" x2="1"><stop offset="0" stop-color="{GREEN}" stop-opacity="0"/><stop offset=".5" stop-color="{GREEN}" stop-opacity=".7"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></linearGradient>
  <clipPath id="frame"><rect width="{W}" height="{h}" rx="16"/></clipPath>
</defs>
<g clip-path="url(#frame)">
  <rect width="{W}" height="{h}" fill="{BG}"/>
  <rect width="{W}" height="{min(h, 520)}" fill="url(#dots)" mask="url(#gridmask)"/>
  <rect width="{W}" height="{h}" fill="url(#glow-g)"/>
  <rect width="{W}" height="{h}" fill="url(#glow-c)"/>
{body}
</g>
<rect x=".5" y=".5" width="{W-1}" height="{h-1}" rx="15.5" fill="none" stroke="#fff" stroke-opacity=".08"/>
</svg>
"""


def heading(num, eyebrow, title, x=44, y=56, cmd=None):
    out = f'<text class="eyebrow fade" x="{x}" y="{y}"><tspan fill="{GREEN}">{num}</tspan>  /  {esc(eyebrow)}</text>\n'
    out += f'<text class="h2 enter" x="{x}" y="{y + 36}" style="animation-delay:.05s">{esc(title)}</text>\n'
    if cmd:
        cw = mono_w(cmd, 12) + 40
        out += (f'<g class="fade" style="animation-delay:.15s"><rect x="{W - 44 - cw}" y="{y - 14}" width="{cw}" height="26" rx="13" fill="#fff" fill-opacity=".04" stroke="#fff" stroke-opacity=".07"/>'
                f'<text class="mono" x="{W - 44 - cw + 14}" y="{y + 3}" font-size="12"><tspan fill="{CYAN}">❯ </tspan><tspan fill="{GREEN}">{esc(cmd)}</tspan></text></g>\n')
    return out


def chip(x, y, label, size=11.5, color=None, fill_op='.04'):
    w = mono_w(label, size) + 18
    c = color or '#D6D6DC'
    return (f'<rect x="{x}" y="{y}" width="{w:.1f}" height="22" rx="11" fill="#fff" fill-opacity="{fill_op}" stroke="#fff" stroke-opacity=".08"/>'
            f'<text class="mono" x="{x + 9}" y="{y + 15}" font-size="{size}" fill="{c}">{esc(label)}</text>'), w


def card(x, y, w, h, op='.025'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#fff" fill-opacity="{op}"/>'
            f'<rect x="{x + .5}" y="{y + .5}" width="{w - 1}" height="{h - 1}" rx="11.5" fill="none" stroke="#fff" stroke-opacity=".07"/>')


# Lucide icons (ISC licence), 24px grid, stroked
ICONS = {
    'laptop': '<path d="M20 16V7a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9m16 0H4m16 0 1.28 2.55a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45L4 16"/>',
    'lock': '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    'key': '<path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5"/>',
    'radar': '<path d="M19.07 4.93A10 10 0 0 0 6.99 3.34"/><path d="M2.29 9.62A10 10 0 1 0 21.31 8.35"/><path d="M16.24 7.76A6 6 0 1 0 8.23 16.67"/><path d="M17.99 11.66A6 6 0 0 1 15.77 16.67"/><circle cx="12" cy="12" r="2"/><path d="m13.41 10.59 5.66-5.66"/>',
}


def icon(name, x, y, color=GREEN, s=20):
    k = s / 24
    return (f'<g transform="translate({x} {y}) scale({k})" fill="none" stroke="{color}" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')


# ── Data (mirrors src/lib/*.ts on the site) ───────────────────────────────
ROLE = 'Consultant'
COMPANY = 'NCS Group Australia'

EXPERIENCE = [
    ('Jul 2026', 'Present', 'Consultant', 'NCS Group Australia', 'Hybrid',
     'Leading client engagements across industries, from research to recommendations.'),
    ('May 2024', 'Jun 2026', 'Associate Consultant', 'NCS Group Australia', 'Hybrid',
     'Defender for Endpoint, Purview DLP, PowerShell automation and Power BI reporting.'),
    ('Apr 2023', 'May 2024', 'Associate Consultant', 'Eighty20 Solutions', 'Remote',
     'Tenant-to-tenant Microsoft 365 migrations for clients around the world.'),
    ('Aug 2021', 'Feb 2023', 'IT & Admin Support Officer', 'SNS Migration and Education', 'On-site',
     'Windows and macOS support, Microsoft 365 licensing, permissions and CRM.'),
]

EXPERT = [
    ('SC-100', 'Cybersecurity Architect Expert', 'May 2027'),
    ('MS-102', 'Microsoft 365 Administrator Expert', 'Apr 2027'),
]
ASSOCIATE = [
    ('SC-401', 'Information Security Administrator', 'Mar 2027'),
    ('MD-102', 'Endpoint Administrator', 'Feb 2027'),
    ('SC-300', 'Identity and Access Administrator', 'May 2027'),
]
APPLIED = [
    'Purview retention, eDiscovery & Communication Compliance',
    'Purview information protection & DLP',
    'Create agents in Microsoft Copilot Studio',
    'Security & compliance for Microsoft 365 Copilot',
]
FUNDAMENTALS = ['AZ-900 Azure', 'AI-900 Azure AI', '(ISC)² CC', 'Cisco Cyber Threat Mgmt',
                'Cisco Endpoint Security', 'Cisco Intro to Cybersecurity', 'AvePoint Technical Pro']

PROJECTS = [
    # slug, title, tagline, category, period, status, stack, access
    ('certprep-coach', 'CertPrep Coach', 'A Microsoft-style exam simulator with an AI vision layer',
     'Security & study', '2026', 'In use by my team', ['Python', 'Streamlit', 'SQLite', 'OpenAI'], 'public'),
    ('lodged', 'Lodged', 'Tracking Australian visa applications on iPhone and Android',
     'Apps', '2026', 'Heading to the app stores', ['Kotlin', 'SwiftUI', 'Supabase'], 'private'),
    ('kitchen-deck', 'Kitchen Deck', 'A shared household kitchen app on a fridge-mounted iPad',
     'Apps', '2026', 'Live, invite-only', ['Preact', 'TypeScript', 'Supabase'], 'live'),
    ('personal-site', 'cpguragain.com', 'This portfolio: security-themed, with motion and SEO built in',
     'Apps', '2024 – now', 'Live', ['Next.js', 'Tailwind', 'Firebase'], 'public'),
    ('phoenix-v7', 'Phoenix V7', 'An autonomous gold-trading engine with a built-in discipline system',
     'Trading & finance', '2026', 'Private research', ['Python', 'scikit-learn', 'MT5'], 'private'),
    ('cpg-capital', 'CPG Capital', 'An AI agent that sends me a daily portfolio briefing',
     'Trading & finance', '2026', 'Running daily', ['Python', 'MCP', 'Telegram'], 'private'),
    ('home-lab', 'Home lab server', 'A self-hosted Linux server for media and a private AI assistant',
     'Infrastructure', '2026', 'Running', ['Ubuntu', 'Jellyfin', 'systemd'], 'private'),
]

FOCUS = [
    ('laptop', 'Endpoint security',
     'Deploying and onboarding Microsoft Defender for Endpoint on Linux servers, with automation for scale.',
     ['MD-102', 'Cisco Endpoint']),
    ('lock', 'Data protection',
     'Microsoft Purview DLP and information protection to classify and safeguard sensitive data.',
     ['SC-401', 'Purview skills']),
    ('key', 'Identity & access',
     'Securing who can reach what across Microsoft cloud, designed with a zero trust mindset.',
     ['SC-300', 'SC-100']),
    ('radar', 'Security operations',
     'Threat management and response grounded in Microsoft security tooling and fundamentals.',
     ['(ISC)² CC', 'Cisco Threat Mgmt']),
]

STACK = [
    ('security', GREEN, ['Defender for Endpoint', 'Purview', 'Sentinel', 'Entra ID', 'Intune', 'Microsoft 365', 'Copilot Studio']),
    ('cloud', CYAN, ['Azure', 'AWS', 'Google Cloud', 'Linux', 'VMware ESXi', 'Firebase', 'Vercel']),
    ('code', AMBER, ['PowerShell', 'Python', 'KQL', 'Bash', 'TypeScript', 'Next.js', 'Kotlin']),
    ('tools', MUTED, ['ShareGate', 'AvePoint Fly', 'Power BI', 'ServiceNow', 'Supabase', 'Docker']),
]


# ── Panels ────────────────────────────────────────────────────────────────
def hero():
    h = 430
    b = []
    # left column
    b.append(f'<g class="fade"><rect x="44" y="48" width="{mono_w(f"{ROLE} at {COMPANY}", 12) + 40}" height="28" rx="14" fill="#fff" fill-opacity=".04" stroke="#fff" stroke-opacity=".08"/>'
             f'<circle cx="60" cy="62" r="3.5" fill="{GREEN}"/><circle cx="60" cy="62" r="5" fill="{GREEN}" style="animation:pulse 2s ease-out infinite"/>'
             f'<text class="mono" x="72" y="66" font-size="12" fill="#D6D6DC">{ROLE} at {COMPANY}</text></g>')
    b.append(f'<text class="mono fade" x="44" y="124" font-size="14" fill="{MUTED}" style="animation-delay:.05s">Hi, I’m</text>')
    b.append(f'<text class="sans enter" x="41" y="176" font-size="58" font-weight="600" letter-spacing="-2" fill="{FG}" style="animation-delay:.08s">CP Guragain</text>')
    b.append(f'<text class="sans enter" x="44" y="216" font-size="17" fill="{FG}" fill-opacity=".85" style="animation-delay:.18s">Cyber security consultant in Sydney, securing</text>')
    b.append(f'<text class="sans enter" x="44" y="240" font-size="17" fill="{FG}" fill-opacity=".85" style="animation-delay:.2s">Microsoft cloud environments. Builder after hours.</text>')
    # stats
    stats = [('12', 'active certs'), ('2', 'expert certs'), ('4', 'applied skills'), ('7', 'projects')]
    for i, (v, label) in enumerate(stats):
        x = 44 + i * 112
        d = .3 + i * .06
        b.append(f'<g class="enter" style="animation-delay:{d:.2f}s"><text class="sans" x="{x}" y="318" font-size="32" font-weight="600" letter-spacing="-1" fill="{FG}">{v}</text>'
                 f'<text class="mono" x="{x}" y="340" font-size="10.5" fill="{MUTED}" letter-spacing=".4">{label}</text></g>')
    b.append(f'<line x1="44" x2="416" y1="290" y2="290" stroke="#fff" stroke-opacity=".07"/>')
    b.append(f'<text class="mono fade" x="44" y="388" font-size="12" fill="{DIM}" style="animation-delay:.55s">cpguragain.com</text>')

    # terminal
    tx, ty, tw, th = 470, 44, 326, 342
    b.append(f'<g class="enter" style="animation-delay:.1s">')
    b.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="12" fill="{CARD}"/>')
    b.append(f'<rect x="{tx + .5}" y="{ty + .5}" width="{tw - 1}" height="{th - 1}" rx="11.5" fill="none" stroke="#fff" stroke-opacity=".08"/>')
    b.append(f'<rect x="{tx + 40}" y="{ty}" width="{tw - 80}" height="1" fill="url(#scan)"/>')
    for i in range(3):
        b.append(f'<circle cx="{tx + 20 + i * 15}" cy="{ty + 19}" r="4.5" fill="#fff" fill-opacity=".1"/>')
    b.append(f'<text class="mono" x="{tx + tw - 18}" y="{ty + 23}" font-size="11" fill="{DIM}" text-anchor="end">~/cp_guragain</text>')
    b.append(f'<line x1="{tx}" x2="{tx + tw}" y1="{ty + 38}" y2="{ty + 38}" stroke="#fff" stroke-opacity=".06"/>')
    b.append('</g>')
    lines = [
        ('cmd', 'whoami'),
        ('out', [(FG, 'cp_guragain'), (DIM, ' · '), (MUTED, 'consultant @ NCS')]),
        ('cmd', 'cat focus.txt'),
        ('out', [(DIM, 'endpoint  '), (FG, 'Defender for Endpoint')]),
        ('out', [(DIM, 'data      '), (FG, 'Purview DLP · MIP')]),
        ('out', [(DIM, 'identity  '), (FG, 'Entra ID · access')]),
        ('out', [(DIM, 'cloud     '), (FG, 'Microsoft 365 · Azure')]),
        ('cmd', 'verify --credentials'),
        ('out', [(GREEN, '✓ 2 expert · 3 associate · 4 skills')]),
    ]
    y = ty + 66
    for i, (kind, content) in enumerate(lines):
        d = .45 + i * .16
        if kind == 'cmd':
            inner = f'<tspan fill="{CYAN}">❯ </tspan><tspan fill="{GREEN}">{esc(content)}</tspan>'
        else:
            inner = ''.join(f'<tspan fill="{c}">{esc(t)}</tspan>' for c, t in content)
        b.append(f'<text class="mono enter" x="{tx + 20}" y="{y}" font-size="12.5" xml:space="preserve" style="animation-delay:{d:.2f}s">{inner}</text>')
        y += 27 if kind == 'out' and i + 1 < len(lines) and lines[i + 1][0] == 'cmd' else 24
    d = .45 + len(lines) * .16
    b.append(f'<g class="fade" style="animation-delay:{d:.2f}s"><text class="mono" x="{tx + 20}" y="{y + 4}" font-size="12.5" fill="{CYAN}">❯</text>'
             f'<rect x="{tx + 36}" y="{y - 8}" width="7.5" height="15" fill="{GREEN}" style="animation:blink 1.1s steps(1) infinite"/></g>')
    # sweep highlight across the whole banner
    b.append(f'<rect x="0" y="0" width="{W * .35}" height="1.5" fill="url(#scan)" style="animation:sweep 6s cubic-bezier(.77,0,.175,1) infinite"/>')
    return svg(h, '\n'.join(b), 'CP Guragain, cyber security consultant')


def focus():
    cw, ch, gap = (W - 88 - 16) // 2, 168, 16
    h = 120 + 2 * ch + gap + 40
    b = [heading('01', 'focus', 'What I work on', cmd='cat focus.txt')]
    for i, (ic, title, body, evidence) in enumerate(FOCUS):
        x = 44 + (i % 2) * (cw + gap)
        y = 120 + (i // 2) * (ch + gap)
        d = .15 + i * .07
        g = [card(x, y, cw, ch)]
        g.append(f'<rect x="{x + 20}" y="{y + 20}" width="34" height="34" rx="9" fill="{GREEN}" fill-opacity=".08" stroke="{GREEN}" stroke-opacity=".2"/>')
        g.append(icon(ic, x + 27, y + 27, s=20))
        g.append(f'<text class="sans" x="{x + 68}" y="{y + 42}" font-size="16" font-weight="600" fill="{FG}">{esc(title)}</text>')
        for j, line in enumerate(wrap(body, 48)):
            g.append(f'<text class="sans" x="{x + 20}" y="{y + 80 + j * 19}" font-size="13" fill="{FG}" fill-opacity=".7">{esc(line)}</text>')
        cx = x + 20
        for e in evidence:
            s, w = chip(cx, y + ch - 36, e, size=10.5, color=MUTED)
            g.append(s)
            cx += w + 6
        b.append(f'<g class="enter" style="animation-delay:{d:.2f}s">' + ''.join(g) + '</g>')
    return svg(h, '\n'.join(b), 'What I work on: endpoint security, data protection, identity and access, security operations')


def experience():
    row = 92
    h = 128 + len(EXPERIENCE) * row + 10
    b = [heading('02', 'experience', 'Where I’ve worked', cmd='git log --career')]
    lx = 196
    top, bottom = 132, 128 + (len(EXPERIENCE) - 1) * row + 8
    b.append(f'<line x1="{lx}" x2="{lx}" y1="{top}" y2="{bottom}" stroke="#fff" stroke-opacity=".1"/>')
    b.append(f'<line x1="{lx}" x2="{lx}" y1="{top}" y2="{top + row}" stroke="{GREEN}" stroke-opacity=".6"/>')
    for i, (start, end, role, company, mode, desc) in enumerate(EXPERIENCE):
        y = 136 + i * row
        d = .15 + i * .08
        current = end == 'Present'
        g = []
        g.append(f'<text class="mono" x="44" y="{y + 4}" font-size="12" fill="{FG if current else MUTED}">{start}</text>')
        g.append(f'<text class="mono" x="44" y="{y + 22}" font-size="12" fill="{GREEN if current else DIM}">→ {end}</text>')
        if current:
            g.append(f'<circle cx="{lx}" cy="{y}" r="5" fill="{GREEN}" style="animation:pulse 2s ease-out infinite"/>')
            g.append(f'<circle cx="{lx}" cy="{y}" r="5" fill="{GREEN}"/>')
        else:
            g.append(f'<circle cx="{lx}" cy="{y}" r="4.5" fill="{BG}" stroke="#fff" stroke-opacity=".35" stroke-width="1.5"/>')
        g.append(f'<text class="sans" x="{lx + 28}" y="{y + 5}" font-size="16.5" font-weight="600" fill="{FG}">{esc(role)}</text>')
        g.append(f'<text class="sans" x="{lx + 28}" y="{y + 27}" font-size="13.5" fill="{MUTED}">{esc(company)}<tspan fill="{DIM}">  ·  {mode}</tspan></text>')
        g.append(f'<text class="sans" x="{lx + 28}" y="{y + 51}" font-size="13.5" fill="{FG}" fill-opacity=".72">{esc(desc)}</text>')
        b.append(f'<g class="enter" style="animation-delay:{d:.2f}s">' + ''.join(g) + '</g>')
    return svg(h, '\n'.join(b), 'Work experience')


def project_card(p):
    slug, title, tagline, cat, period, status, stack, access = p
    cw, ch = 412, 236
    b = []
    b.append(f'<text class="mono" x="24" y="34" font-size="11.5"><tspan fill="{GREEN}">❯</tspan><tspan fill="{MUTED}"> {slug}</tspan></text>')
    b.append(f'<text class="mono" x="{cw - 24}" y="34" font-size="11.5" fill="{DIM}" text-anchor="end">{esc(period)}</text>')
    b.append(f'<text class="eyebrow" x="24" y="68" font-size="10">{esc(cat)}</text>')
    b.append(f'<text class="sans" x="24" y="96" font-size="22" font-weight="600" letter-spacing="-.5" fill="{FG}">{esc(title)}</text>')
    for j, line in enumerate(wrap(tagline, 46)[:2]):
        b.append(f'<text class="sans" x="24" y="{124 + j * 20}" font-size="14" fill="{FG}" fill-opacity=".72">{esc(line)}</text>')
    cx = 24
    for s in stack:
        c, w = chip(cx, 166, s, size=10.5)
        b.append(c)
        cx += w + 6
    b.append(f'<line x1="24" x2="{cw - 24}" y1="202" y2="202" stroke="#fff" stroke-opacity=".06"/>')
    dot = {'public': GREEN, 'live': CYAN, 'private': AMBER}[access]
    tag = {'public': 'open source', 'live': 'live app', 'private': 'private code'}[access]
    b.append(f'<circle cx="28" cy="219" r="3" fill="{dot}"/><text class="mono" x="38" y="223" font-size="10.5" fill="{MUTED}">{tag} · {esc(status.lower())}</text>')
    b.append(f'<text class="mono" x="{cw - 24}" y="223" font-size="11" fill="{GREEN}" text-anchor="end">read →</text>')
    body = '\n'.join(b)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{cw}" height="{ch}" viewBox="0 0 {cw} {ch}" role="img" aria-label="{esc(title)}: {esc(tagline)}">
<title>{esc(title)}: {esc(tagline)}</title>
<style>{BASE_CSS}</style>
<defs>
  <linearGradient id="scan" x1="0" x2="1"><stop offset="0" stop-color="{GREEN}" stop-opacity="0"/><stop offset=".5" stop-color="{GREEN}" stop-opacity=".55"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></linearGradient>
  <radialGradient id="g" cx="0%" cy="0%" r="80%"><stop offset="0" stop-color="{GREEN}" stop-opacity=".07"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></radialGradient>
</defs>
<g class="fade">
<rect width="{cw}" height="{ch}" rx="14" fill="{CARD}"/>
<rect width="{cw}" height="{ch}" rx="14" fill="url(#g)"/>
<rect x="60" y="0" width="{cw - 120}" height="1" fill="url(#scan)"/>
<rect x=".5" y=".5" width="{cw - 1}" height="{ch - 1}" rx="13.5" fill="none" stroke="#fff" stroke-opacity=".08"/>
{body}
</g>
</svg>
"""


def all_projects_card():
    cw, ch = 412, 236
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{cw}" height="{ch}" viewBox="0 0 {cw} {ch}" role="img" aria-label="Read every project write-up on cpguragain.com">
<title>Read every project write-up on cpguragain.com</title>
<style>{BASE_CSS}</style>
<defs>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#fff" fill-opacity=".08"/></pattern>
  <radialGradient id="g" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="{GREEN}" stop-opacity=".12"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></radialGradient>
</defs>
<g class="fade">
<rect width="{cw}" height="{ch}" rx="14" fill="{BG}"/>
<rect width="{cw}" height="{ch}" rx="14" fill="url(#dots)"/>
<rect width="{cw}" height="{ch}" rx="14" fill="url(#g)"/>
<rect x=".5" y=".5" width="{cw - 1}" height="{ch - 1}" rx="13.5" fill="none" stroke="{GREEN}" stroke-opacity=".3" stroke-dasharray="4 5"/>
<text class="mono" x="{cw / 2}" y="98" font-size="13" text-anchor="middle"><tspan fill="{CYAN}">❯ </tspan><tspan fill="{GREEN}">open cpguragain.com/projects</tspan></text>
<text class="sans" x="{cw / 2}" y="134" font-size="20" font-weight="600" letter-spacing="-.4" fill="{FG}" text-anchor="middle">Read every write-up →</text>
<text class="sans" x="{cw / 2}" y="160" font-size="13.5" fill="{MUTED}" text-anchor="middle">How each one works and what it taught me</text>
</g>
</svg>
"""


def projects_header():
    h = 112
    b = [heading('03', 'projects', 'Things I’ve built', y=50, cmd='ls ~/projects')]
    return svg(h, '\n'.join(b), 'Things I have built')


def credentials():
    row = 34
    y0 = 146
    b = [heading('04', 'credentials', 'Verified credentials', cmd='verify --credentials')]
    y = y0
    delay = .12

    def group(label, color, count):
        return (f'<text class="eyebrow" x="44" y="{y}"><tspan fill="{color}">■</tspan>  {label}'
                f'<tspan fill="{DIM}">  ({count})</tspan></text>')

    def cert_row(y, code, name, exp, d):
        cw_ = mono_w(code, 11) + 16
        return (f'<g class="enter" style="animation-delay:{d:.2f}s">'
                f'<line x1="44" x2="{W - 44}" y1="{y + 13}" y2="{y + 13}" stroke="#fff" stroke-opacity=".05"/>'
                f'<text class="mono" x="44" y="{y + 1}" font-size="13" fill="{GREEN}">✓</text>'
                f'<rect x="66" y="{y - 13}" width="{cw_}" height="20" rx="5" fill="{CYAN}" fill-opacity=".08" stroke="{CYAN}" stroke-opacity=".25"/>'
                f'<text class="mono" x="74" y="{y + 1}" font-size="11" fill="{CYAN}">{code}</text>'
                f'<text class="sans" x="{66 + cw_ + 14}" y="{y + 1}" font-size="14.5" fill="{FG}">{esc(name)}</text>'
                f'<text class="mono" x="{W - 44}" y="{y + 1}" font-size="11" fill="{DIM}" text-anchor="end">valid to {exp}</text></g>')

    b.append(group('expert', GREEN, len(EXPERT)))
    y += 32
    for code, name, exp in EXPERT:
        b.append(cert_row(y, code, name, exp, delay)); y += row; delay += .05
    y += 18
    b.append(group('associate', CYAN, len(ASSOCIATE)))
    y += 32
    for code, name, exp in ASSOCIATE:
        b.append(cert_row(y, code, name, exp, delay)); y += row; delay += .05
    y += 18
    b.append(group('applied skills', AMBER, len(APPLIED)))
    y += 30
    for s in APPLIED:
        b.append(f'<g class="enter" style="animation-delay:{delay:.2f}s"><text class="mono" x="46" y="{y}" font-size="11" fill="{AMBER}">◆</text>'
                 f'<text class="sans" x="66" y="{y}" font-size="14" fill="{FG}" fill-opacity=".85">{esc(s)}</text></g>')
        y += 28
        delay += .04
    y += 22
    b.append(group('fundamentals &amp; industry', MUTED, len(FUNDAMENTALS)))
    y += 18
    cx, cy = 44, y
    for f in FUNDAMENTALS:
        w = mono_w(f, 11) + 18
        if cx + w > W - 44:
            cx, cy = 44, cy + 30
        s, w = chip(cx, cy, f, size=11)
        b.append(f'<g class="fade" style="animation-delay:{delay:.2f}s">{s}</g>')
        cx += w + 8
    return svg(cy + 22 + 40, '\n'.join(b), 'Verified credentials')


def stack():
    h = 120 + len(STACK) * 44 + 26
    b = [heading('05', 'toolkit', 'Tools I use', cmd='cat stack.txt')]
    y = 124
    for i, (label, color, items) in enumerate(STACK):
        d = .12 + i * .07
        g = [f'<text class="mono" x="44" y="{y + 15}" font-size="12" fill="{color}">{label}</text>']
        cx = 130
        for it in items:
            s, w = chip(cx, y, it, size=11)
            g.append(s)
            cx += w + 7
        b.append(f'<g class="enter" style="animation-delay:{d:.2f}s">' + ''.join(g) + '</g>')
        y += 44
    return svg(h, '\n'.join(b), 'Tools I use')


def contact():
    h = 250
    b = [heading('06', 'contact', 'Let’s build something secure')]
    lines = [
        ('cmd', 'connect --with cp_guragain'),
        ('kv', 'web     ', 'cpguragain.com'),
        ('kv', 'mail    ', 'connect@cpguragain.com'),
        ('kv', 'linkedin', 'in/cp-guragain-601b28198'),
    ]
    y = 140
    for i, ln in enumerate(lines):
        d = .2 + i * .15
        if ln[0] == 'cmd':
            inner = f'<tspan fill="{CYAN}">❯ </tspan><tspan fill="{GREEN}">{ln[1]}</tspan>'
        else:
            inner = f'<tspan fill="{DIM}">{ln[1]}  </tspan><tspan fill="{FG}">{ln[2]}</tspan>'
        b.append(f'<text class="mono enter" x="44" y="{y}" font-size="13.5" xml:space="preserve" style="animation-delay:{d:.2f}s">{inner}</text>')
        y += 26
    d = .2 + len(lines) * .15
    b.append(f'<g class="fade" style="animation-delay:{d:.2f}s"><text class="mono" x="44" y="{y + 2}" font-size="13.5" fill="{CYAN}">❯</text>'
             f'<rect x="61" y="{y - 10}" width="8" height="16" fill="{GREEN}" style="animation:blink 1.1s steps(1) infinite"/></g>')
    b.append(f'<text class="sans fade" x="{W - 44}" y="140" font-size="14" fill="{MUTED}" text-anchor="end" style="animation-delay:.3s">Open to consulting engagements,</text>')
    b.append(f'<text class="sans fade" x="{W - 44}" y="160" font-size="14" fill="{MUTED}" text-anchor="end" style="animation-delay:.32s">collaborations and interesting problems.</text>')
    return svg(h, '\n'.join(b), 'Contact CP Guragain')


def main():
    out = ROOT
    files = {
        'hero.svg': hero(),
        'focus.svg': focus(),
        'experience.svg': experience(),
        'projects.svg': projects_header(),
        'credentials.svg': credentials(),
        'stack.svg': stack(),
        'contact.svg': contact(),
    }
    files['project-all.svg'] = all_projects_card()
    for p in PROJECTS:
        files[f'project-{p[0]}.svg'] = project_card(p)
    for name, content in files.items():
        (out / name).write_text(content, encoding='utf-8', newline='\n')
        print(f'{name:32} {len(content) // 1024:>4} KB')


if __name__ == '__main__':
    main()
