<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>CP Guragain — Security Consultant</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet"/>
<style>
  :root {
    --bg: #050a0f;
    --surface: #0b1420;
    --surface2: #0f1e2e;
    --border: rgba(0,210,255,0.12);
    --cyan: #00d2ff;
    --cyan-dim: rgba(0,210,255,0.15);
    --cyan-glow: rgba(0,210,255,0.35);
    --orange: #ff6b2b;
    --orange-dim: rgba(255,107,43,0.15);
    --green: #00ff9d;
    --text: #e2eaf4;
    --muted: #607080;
    --font-head: 'Syne', sans-serif;
    --font-mono: 'Space Mono', monospace;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--font-mono);
    line-height: 1.6;
    overflow-x: hidden;
  }

  /* SCAN LINE OVERLAY */
  body::before {
    content: '';
    position: fixed; inset: 0;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,0,0,0.15) 2px,
      rgba(0,0,0,0.15) 4px
    );
    pointer-events: none;
    z-index: 9999;
  }

  /* GRID NOISE BG */
  body::after {
    content: '';
    position: fixed; inset: 0;
    background-image:
      linear-gradient(rgba(0,210,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,210,255,0.03) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none;
    z-index: 0;
  }

  .wrapper {
    position: relative;
    z-index: 1;
    max-width: 900px;
    margin: 0 auto;
    padding: 60px 24px 80px;
  }

  /* ─── HERO ─── */
  .hero {
    position: relative;
    padding: 60px 0 48px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 64px;
    overflow: hidden;
  }

  .hero-glow {
    position: absolute;
    top: -80px; left: -120px;
    width: 500px; height: 400px;
    background: radial-gradient(ellipse, rgba(0,210,255,0.08) 0%, transparent 65%);
    pointer-events: none;
  }

  .hero-status {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 11px;
    color: var(--green);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 24px;
    background: rgba(0,255,157,0.07);
    border: 1px solid rgba(0,255,157,0.2);
    padding: 6px 14px;
    border-radius: 2px;
  }

  .status-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 8px var(--green);
    animation: pulse 2s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; box-shadow: 0 0 8px var(--green); }
    50% { opacity: 0.5; box-shadow: 0 0 3px var(--green); }
  }

  .hero h1 {
    font-family: var(--font-head);
    font-size: clamp(40px, 8vw, 78px);
    font-weight: 800;
    line-height: 1;
    letter-spacing: -0.02em;
    color: #fff;
    margin-bottom: 6px;
  }

  .hero h1 .accent { color: var(--cyan); }

  .hero-title {
    font-family: var(--font-head);
    font-size: 13px;
    font-weight: 600;
    color: var(--orange);
    letter-spacing: 0.25em;
    text-transform: uppercase;
    margin-bottom: 28px;
  }

  .hero-desc {
    font-size: 13.5px;
    color: #8ba4bf;
    max-width: 600px;
    line-height: 1.85;
    border-left: 2px solid var(--cyan);
    padding-left: 18px;
    margin-bottom: 36px;
  }

  .hero-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  .tag {
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 5px 12px;
    border: 1px solid var(--border);
    color: var(--muted);
    background: var(--surface);
    transition: all 0.2s;
  }

  .tag:hover {
    border-color: var(--cyan);
    color: var(--cyan);
    background: var(--cyan-dim);
  }

  /* ─── SECTION HEADERS ─── */
  .section {
    margin-bottom: 60px;
    animation: fadeUp 0.5s ease both;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .section:nth-child(2) { animation-delay: 0.1s; }
  .section:nth-child(3) { animation-delay: 0.2s; }
  .section:nth-child(4) { animation-delay: 0.3s; }
  .section:nth-child(5) { animation-delay: 0.4s; }

  .section-label {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 10px;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--cyan);
    margin-bottom: 28px;
  }

  .section-label::before {
    content: '';
    display: block;
    width: 32px; height: 1px;
    background: var(--cyan);
  }

  .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
  }

  /* ─── ABOUT CARDS ─── */
  .about-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 16px;
  }

  .about-card {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 20px 22px;
    position: relative;
    transition: border-color 0.25s, background 0.25s;
    overflow: hidden;
  }

  .about-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 0;
    background: var(--cyan);
    transition: height 0.3s ease;
  }

  .about-card:hover { border-color: var(--cyan-glow); background: var(--surface2); }
  .about-card:hover::before { height: 100%; }

  .about-card-icon {
    font-size: 20px;
    margin-bottom: 10px;
  }

  .about-card-title {
    font-family: var(--font-head);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--orange);
    margin-bottom: 6px;
  }

  .about-card-text {
    font-size: 12.5px;
    color: #7a96b0;
    line-height: 1.7;
  }

  /* ─── TECH STACK ─── */
  .stack-category {
    margin-bottom: 24px;
  }

  .stack-cat-label {
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
  }

  .stack-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  .pill {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    background: var(--surface);
    border: 1px solid var(--border);
    font-size: 12px;
    color: #8ba4bf;
    transition: all 0.2s ease;
    cursor: default;
    position: relative;
    overflow: hidden;
  }

  .pill::after {
    content: '';
    position: absolute;
    inset: 0;
    background: var(--cyan-dim);
    opacity: 0;
    transition: opacity 0.2s;
  }

  .pill:hover {
    border-color: var(--cyan);
    color: var(--cyan);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,210,255,0.1);
  }

  .pill:hover::after { opacity: 1; }

  .pill-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  /* ─── CERTS ─── */
  .cert-list {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .cert-item {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 16px 20px;
    background: var(--surface);
    border: 1px solid var(--border);
    transition: all 0.25s;
    position: relative;
    overflow: hidden;
  }

  .cert-item::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 0;
    background: linear-gradient(90deg, rgba(0,210,255,0.08), transparent);
    transition: width 0.3s ease;
  }

  .cert-item:hover { border-color: var(--cyan-glow); }
  .cert-item:hover::before { width: 100%; }

  .cert-icon {
    width: 38px; height: 38px;
    background: linear-gradient(135deg, #0078d4, #00bcf2);
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
    box-shadow: 0 4px 16px rgba(0,120,212,0.3);
  }

  .cert-name {
    font-family: var(--font-head);
    font-size: 13px;
    font-weight: 700;
    color: var(--text);
  }

  .cert-sub {
    font-size: 11px;
    color: var(--muted);
    margin-top: 2px;
    letter-spacing: 0.05em;
  }

  .cert-badge {
    margin-left: auto;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--green);
    background: rgba(0,255,157,0.08);
    border: 1px solid rgba(0,255,157,0.2);
    padding: 3px 10px;
  }

  /* ─── STATS ─── */
  .stats-row {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 16px;
    margin-bottom: 28px;
  }

  .stat-box {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 24px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.25s;
  }

  .stat-box:hover {
    border-color: var(--cyan-glow);
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0,210,255,0.07);
  }

  .stat-box::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--cyan), transparent);
    opacity: 0;
    transition: opacity 0.3s;
  }

  .stat-box:hover::after { opacity: 1; }

  .stat-num {
    font-family: var(--font-head);
    font-size: 36px;
    font-weight: 800;
    color: var(--cyan);
    display: block;
    line-height: 1;
    margin-bottom: 6px;
  }

  .stat-label {
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--muted);
  }

  /* ─── GITHUB CARD ─── */
  .github-card {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 28px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
  }

  .github-card img {
    width: 100%;
    max-width: 500px;
    border: 1px solid var(--border);
    filter: brightness(0.9) contrast(1.05);
    transition: filter 0.3s;
  }

  .github-card img:hover { filter: brightness(1) contrast(1.1); }

  /* ─── CONNECT ─── */
  .connect-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 14px;
  }

  .connect-item {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 18px 20px;
    background: var(--surface);
    border: 1px solid var(--border);
    text-decoration: none;
    color: var(--text);
    transition: all 0.25s;
    position: relative;
    overflow: hidden;
  }

  .connect-item::before {
    content: '';
    position: absolute;
    left: -100%; top: 0; bottom: 0;
    width: 100%;
    background: linear-gradient(90deg, transparent, rgba(0,210,255,0.06), transparent);
    transition: left 0.4s ease;
  }

  .connect-item:hover { border-color: var(--cyan-glow); transform: translateX(4px); }
  .connect-item:hover::before { left: 100%; }

  .connect-icon {
    width: 36px; height: 36px;
    background: var(--cyan-dim);
    border: 1px solid var(--border);
    display: flex; align-items: center; justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
  }

  .connect-label {
    font-family: var(--font-head);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text);
  }

  .connect-sub {
    font-size: 11px;
    color: var(--muted);
    margin-top: 2px;
  }

  .connect-arrow {
    margin-left: auto;
    color: var(--cyan);
    font-size: 18px;
    opacity: 0;
    transform: translateX(-6px);
    transition: all 0.25s;
  }

  .connect-item:hover .connect-arrow {
    opacity: 1;
    transform: translateX(0);
  }

  /* ─── FOOTER ─── */
  .footer {
    margin-top: 80px;
    padding-top: 32px;
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }

  .footer-left {
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 0.05em;
  }

  .footer-right {
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 0.05em;
  }

  .footer-right span { color: var(--cyan); }

  /* ─── TERMINAL BLINK ─── */
  .blink {
    display: inline-block;
    width: 8px; height: 14px;
    background: var(--cyan);
    margin-left: 4px;
    vertical-align: middle;
    animation: blink 1.1s step-end infinite;
    box-shadow: 0 0 8px var(--cyan);
  }

  @keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
  }

  /* ─── SCROLLBAR ─── */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--border); }
  ::-webkit-scrollbar-thumb:hover { background: var(--cyan-glow); }

  /* ─── RESPONSIVE ─── */
  @media (max-width: 600px) {
    .footer { flex-direction: column; text-align: center; }
  }
</style>
</head>
<body>
<div class="wrapper">

  <!-- HERO -->
  <header class="hero">
    <div class="hero-glow"></div>
    <div class="hero-status">
      <span class="status-dot"></span>
      Available for consulting engagements
    </div>
    <h1><span class="accent">CP</span> Guragain<span class="blink"></span></h1>
    <p class="hero-title">Security Consultant · Cloud Infrastructure · Automation Specialist</p>
    <p class="hero-desc">
      IT Specialist and Cyber Security professional with 3+ years of hands-on experience
      securing enterprise environments, executing cloud migrations, and automating
      mission-critical workflows. Currently deploying Microsoft Defender suites and
      enterprise data protection at NCS Australia.
    </p>
    <div class="hero-tags">
      <span class="tag">Microsoft Defender</span>
      <span class="tag">Azure</span>
      <span class="tag">Purview</span>
      <span class="tag">PowerShell</span>
      <span class="tag">Python</span>
      <span class="tag">Zero Trust</span>
      <span class="tag">Cloud Migration</span>
    </div>
  </header>

  <!-- ABOUT -->
  <section class="section">
    <div class="section-label">About Me</div>
    <div class="about-grid">
      <div class="about-card">
        <div class="about-card-icon">🔭</div>
        <div class="about-card-title">Currently Building</div>
        <div class="about-card-text">Large-scale IT workflow automation and custom AI agents — PowerShell Architects & SharePoint Experts — to streamline enterprise technical operations.</div>
      </div>
      <div class="about-card">
        <div class="about-card-icon">🌱</div>
        <div class="about-card-title">Exploring</div>
        <div class="about-card-text">Advanced algorithmic Forex trading strategies with Python and MetaTrader 5. Building quantitative models for systematic market execution.</div>
      </div>
      <div class="about-card">
        <div class="about-card-icon">🎓</div>
        <div class="about-card-title">Education</div>
        <div class="about-card-text">Bachelor of IT (Cyber Security). Currently pursuing further postgraduate studies in Information Technology and Security Architecture.</div>
      </div>
      <div class="about-card">
        <div class="about-card-icon">⚡</div>
        <div class="about-card-title">Off the Clock</div>
        <div class="about-card-text">Trackside for Formula 1, fine-tuning automated trading strategies, and pushing the boundaries of what PowerShell can do in production.</div>
      </div>
    </div>
  </section>

  <!-- STATS -->
  <section class="section">
    <div class="section-label">By the Numbers</div>
    <div class="stats-row">
      <div class="stat-box">
        <span class="stat-num">3+</span>
        <span class="stat-label">Years in Security</span>
      </div>
      <div class="stat-box">
        <span class="stat-num">8+</span>
        <span class="stat-label">Certifications</span>
      </div>
      <div class="stat-box">
        <span class="stat-num">3</span>
        <span class="stat-label">Cloud Platforms</span>
      </div>
      <div class="stat-box">
        <span class="stat-num">∞</span>
        <span class="stat-label">Scripts Written</span>
      </div>
    </div>
  </section>

  <!-- CERTIFICATIONS -->
  <section class="section">
    <div class="section-label">Certifications</div>
    <div class="cert-list">
      <div class="cert-item">
        <div class="cert-icon">🛡️</div>
        <div>
          <div class="cert-name">Cybersecurity Architect Expert</div>
          <div class="cert-sub">Microsoft Certified — SC-100</div>
        </div>
        <span class="cert-badge">Expert</span>
      </div>
      <div class="cert-item">
        <div class="cert-icon">⚙️</div>
        <div>
          <div class="cert-name">M365 Administrator Expert</div>
          <div class="cert-sub">Microsoft Certified — MS-102</div>
        </div>
        <span class="cert-badge">Expert</span>
      </div>
      <div class="cert-item">
        <div class="cert-icon">🤖</div>
        <div>
          <div class="cert-name">Applied Skills — M365 Copilot</div>
          <div class="cert-sub">Microsoft Applied Skills</div>
        </div>
        <span class="cert-badge">Applied</span>
      </div>
      <div class="cert-item">
        <div class="cert-icon">🔒</div>
        <div>
          <div class="cert-name">Applied Skills — Microsoft Purview</div>
          <div class="cert-sub">Microsoft Applied Skills · Data Governance</div>
        </div>
        <span class="cert-badge">Applied</span>
      </div>
    </div>
  </section>

  <!-- TECH STACK -->
  <section class="section">
    <div class="section-label">Tech Stack</div>

    <div class="stack-category">
      <div class="stack-cat-label">Languages &amp; Scripting</div>
      <div class="stack-pills">
        <div class="pill"><span class="pill-dot" style="background:#5391FE;"></span> PowerShell</div>
        <div class="pill"><span class="pill-dot" style="background:#3776AB;"></span> Python</div>
        <div class="pill"><span class="pill-dot" style="background:#eee;"></span> Markdown</div>
        <div class="pill"><span class="pill-dot" style="background:#f7df1e;"></span> Bash / KQL</div>
      </div>
    </div>

    <div class="stack-category">
      <div class="stack-cat-label">Cloud &amp; Infrastructure</div>
      <div class="stack-pills">
        <div class="pill"><span class="pill-dot" style="background:#0089D6;"></span> Microsoft Azure</div>
        <div class="pill"><span class="pill-dot" style="background:#FF9900;"></span> AWS</div>
        <div class="pill"><span class="pill-dot" style="background:#4285F4;"></span> Google Cloud</div>
        <div class="pill"><span class="pill-dot" style="background:#FCC624;"></span> Linux</div>
        <div class="pill"><span class="pill-dot" style="background:#00d2ff;"></span> Entra ID</div>
      </div>
    </div>

    <div class="stack-category">
      <div class="stack-cat-label">Security &amp; M365 Ecosystem</div>
      <div class="stack-pills">
        <div class="pill"><span class="pill-dot" style="background:#0078D4;"></span> Microsoft Defender</div>
        <div class="pill"><span class="pill-dot" style="background:#D83B01;"></span> Microsoft 365</div>
        <div class="pill"><span class="pill-dot" style="background:#0078D4;"></span> SharePoint</div>
        <div class="pill"><span class="pill-dot" style="background:#742774;"></span> Microsoft Purview</div>
        <div class="pill"><span class="pill-dot" style="background:#F2C811;"></span> Power BI</div>
        <div class="pill"><span class="pill-dot" style="background:#00a4ef;"></span> Intune / MEM</div>
        <div class="pill"><span class="pill-dot" style="background:#008272;"></span> Sentinel</div>
      </div>
    </div>
  </section>

  <!-- GITHUB STATS -->
  <section class="section">
    <div class="section-label">GitHub Activity</div>
    <div class="github-card">
      <img
        src="https://github-readme-stats.vercel.app/api?username=Chanan57&show_icons=true&theme=dark&bg_color=0b1420&border_color=1a2e44&title_color=00d2ff&icon_color=ff6b2b&text_color=8ba4bf&ring_color=00d2ff"
        alt="CP Guragain GitHub Stats"
      />
      <img
        src="https://github-readme-streak-stats.herokuapp.com/?user=Chanan57&theme=dark&background=0b1420&border=1a2e44&ring=00d2ff&fire=ff6b2b&currStreakLabel=00d2ff&sideLabels=8ba4bf&dates=8ba4bf"
        alt="GitHub Streak"
      />
    </div>
  </section>

  <!-- CONNECT -->
  <section class="section">
    <div class="section-label">Let's Connect</div>
    <div class="connect-grid">
      <a href="https://cpguragain.com" target="_blank" class="connect-item">
        <div class="connect-icon">🌐</div>
        <div>
          <div class="connect-label">Website</div>
          <div class="connect-sub">cpguragain.com</div>
        </div>
        <span class="connect-arrow">→</span>
      </a>
      <a href="https://www.linkedin.com/in/cp-guragain-601b28198/" target="_blank" class="connect-item">
        <div class="connect-icon">💼</div>
        <div>
          <div class="connect-label">LinkedIn</div>
          <div class="connect-sub">Professional Network</div>
        </div>
        <span class="connect-arrow">→</span>
      </a>
      <a href="mailto:connect@cpguragain.com" class="connect-item">
        <div class="connect-icon">✉️</div>
        <div>
          <div class="connect-label">Email</div>
          <div class="connect-sub">connect@cpguragain.com</div>
        </div>
        <span class="connect-arrow">→</span>
      </a>
    </div>
  </section>

  <footer class="footer">
    <div class="footer-left">© 2025 CP Guragain · NCS Australia</div>
    <div class="footer-right">Built with <span>precision</span> · Secured by <span>design</span></div>
  </footer>

</div>
</body>
</html>
