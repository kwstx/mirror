import os, sys, io
from playwright.sync_api import sync_playwright
from PIL import Image
import numpy as np

font_dir = os.path.abspath('public/fonts').replace('\\', '/')
img_uri = os.path.abspath('public/images/party_of_four_cards.png').replace('\\', '/')

ref = Image.open('public/images/party_of_four_reference.png').convert('RGB')
ref_arr = np.array(ref)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
@font-face {{
  font-family: 'Modern Era';
  src: url('{font_dir}/ModernEra-Regular.woff2') format('woff2');
  font-style: normal;
  font-weight: 400;
}}
@font-face {{
  font-family: 'Modern Era';
  src: url('{font_dir}/ModernEra-Bold.woff2') format('woff2');
  font-style: normal;
  font-weight: 700;
}}
@font-face {{
  font-family: 'Society';
  src: url('{font_dir}/Society_800_normal.woff2') format('woff2');
  font-style: normal;
  font-weight: 800;
}}
@font-face {{
  font-family: 'Society';
  src: url('{font_dir}/Society_800_italic.woff2') format('woff2');
  font-style: italic;
  font-weight: 800;
}}
* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}
body {{
  background-color: #5a000f;
  color: #ffffff;
  width: 1024px;
  height: 425px;
  overflow: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}}
.section {{
  position: relative;
  width: 1024px;
  height: 425px;
  background-color: #5a000f;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-top: {pt}px;
}}
.headline {{
  font-family: 'Society', Georgia, serif;
  font-weight: 800;
  font-size: {hl_size}px;
  line-height: {hl_lh}px;
  letter-spacing: {hl_ls}em;
  color: #ffffff;
  margin-bottom: {hl_mb}px;
}}
.headline-italic {{
  font-style: italic;
}}
.body-text {{
  font-family: 'Modern Era', -apple-system, sans-serif;
  font-size: {body_size}px;
  line-height: {body_lh}px;
  letter-spacing: {body_ls}em;
  color: #ffffff;
}}
.body-bold {{
  font-weight: 700;
}}
.cards-container {{
  position: absolute;
  top: 158px;
  left: 314px;
  width: 396px;
  height: 250px;
}}
.cards-img {{
  width: 396px;
  height: 250px;
  display: block;
}}
</style>
</head>
<body>
<div class="section">
  <h2 class="headline">Party of <span class="headline-italic">four</span></h2>
  <div class="body-text">
    <p>First dates don't have to feel like job interviews.</p>
    <p><span class="body-bold">Double Date</span> changes the math: you bring your person, they bring theirs, and</p>
    <p>suddenly it's just four people at a table seeing what happens. Less pressure.</p>
    <p>More fun. The kind of night that's good either way.</p>
  </div>
  <div class="cards-container">
    <img src="{img_uri}" class="cards-img" />
  </div>
</div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page()
    page.set_viewport_size({'width': 1024, 'height': 425})
    
    best_total_diff = 999999
    best_config = None
    
    for pt in [4, 5, 6, 7]:
        for hl_size in [26.0, 26.5, 27.0, 27.5, 28.0]:
            for hl_lh in [28, 29, 30]:
                for hl_ls in [-0.015, -0.01, -0.005, 0]:
                    for hl_mb in [12, 13, 14, 15]:
                        for body_size in [11.0, 11.2, 11.4, 11.5, 11.6]:
                            for body_lh in [15.5, 16.0, 16.5]:
                                for body_ls in [-0.005, 0, 0.002, 0.005]:
                                    pass
    
    # Let's test a targeted set of candidates
    candidates = []
    for pt in [4, 5, 6]:
        for hl_size in [26.5, 27.0, 27.5]:
            for hl_ls in [-0.01, -0.005, 0]:
                for hl_mb in [12, 13, 14]:
                    for body_size in [11.2, 11.4, 11.6]:
                        for body_lh in [15.8, 16.0, 16.2]:
                            for body_ls in [0, 0.002, 0.005]:
                                candidates.append((pt, hl_size, 29, hl_ls, hl_mb, body_size, body_lh, body_ls))
    
    print(f"Testing {len(candidates)} candidates...", flush=True)
    for i, c in enumerate(candidates):
        pt, hl_size, hl_lh, hl_ls, hl_mb, body_size, body_lh, body_ls = c
        html = html_template.format(
            font_dir=font_dir,
            img_uri=img_uri,
            pt=pt,
            hl_size=hl_size,
            hl_lh=hl_lh,
            hl_ls=hl_ls,
            hl_mb=hl_mb,
            body_size=body_size,
            body_lh=body_lh,
            body_ls=body_ls
        )
        page.set_content(html)
        shot = page.screenshot()
        test_img = Image.open(io.BytesIO(shot)).convert('RGB')
        test_arr = np.array(test_img)
        diff = np.abs(ref_arr.astype(int) - test_arr.astype(int)).mean()
        if diff < best_total_diff:
            best_total_diff = diff
            best_config = c
            print(f"[{i}/{len(candidates)}] New best total diff: {best_total_diff:.4f} config: {best_config}", flush=True)

    print("BEST CONFIG:", best_config, "DIFF:", best_total_diff, flush=True)
    
    # Save the screenshot for the best config
    pt, hl_size, hl_lh, hl_ls, hl_mb, body_size, body_lh, body_ls = best_config
    html = html_template.format(
        font_dir=font_dir,
        img_uri=img_uri,
        pt=pt,
        hl_size=hl_size,
        hl_lh=hl_lh,
        hl_ls=hl_ls,
        hl_mb=hl_mb,
        body_size=body_size,
        body_lh=body_lh,
        body_ls=body_ls
    )
    page.set_content(html)
    page.screenshot(path='public/debug_best_render.png')
    
    test_img = Image.open('public/debug_best_render.png').convert('RGB')
    test_arr = np.array(test_img)
    total_diff = np.abs(ref_arr.astype(int) - test_arr.astype(int))
    diff_boost = Image.fromarray(np.clip(total_diff * 5, 0, 255).astype(np.uint8))
    diff_boost.save('public/debug_best_diff.png')
    
    browser.close()
