import os
from playwright.sync_api import sync_playwright
from PIL import Image
import numpy as np
import io

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
  src: url('{font_dir}/Society_800_normal.woff2') format('woff2'),
       url('{font_dir}/Society_800_normal.ttf') format('truetype');
  font-style: normal;
  font-weight: 800;
}}
@font-face {{
  font-family: 'Society';
  src: url('{font_dir}/Society_800_italic.woff2') format('woff2'),
       url('{font_dir}/Society_800_italic.ttf') format('truetype');
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
}}
.headline {{
  font-family: 'Society', Georgia, serif;
  font-weight: 800;
  font-size: {hl_size}px;
  line-height: {hl_lh};
  letter-spacing: {hl_ls}em;
  color: #ffffff;
  margin-top: {hl_mt}px;
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
  margin-top: {body_mt}px;
}}
.body-bold {{
  font-weight: 700;
}}
.cards-container {{
  position: absolute;
  top: 158px;
  left: 317px;
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

os.makedirs('scratch', exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page()
    page.set_viewport_size({'width': 1024, 'height': 425})
    
    best_hl_diff = 999999
    best_hl_params = None
    
    for hl_size in [26.0, 26.5, 27.0, 27.5, 28.0, 28.5]:
        for hl_lh in ['1.0', '1.05', '1.1']:
            for hl_ls in [-0.02, -0.015, -0.01, -0.005, 0]:
                for hl_mt in [2, 3, 4, 5, 6, 7]:
                    html = html_template.format(
                        font_dir=font_dir,
                        img_uri=img_uri,
                        hl_size=hl_size,
                        hl_lh=hl_lh,
                        hl_ls=hl_ls,
                        hl_mt=hl_mt,
                        body_size=11.3,
                        body_lh=16.0,
                        body_ls=0.002,
                        body_mt=13
                    )
                    page.set_content(html)
                    page.wait_for_timeout(20)
                    shot = page.screenshot()
                    test_img = Image.open(io.BytesIO(shot)).convert('RGB')
                    test_arr = np.array(test_img)
                    
                    diff = np.abs(ref_arr[0:40, 300:724, :].astype(int) - test_arr[0:40, 300:724, :].astype(int)).mean()
                    if diff < best_hl_diff:
                        best_hl_diff = diff
                        best_hl_params = (hl_size, hl_lh, hl_ls, hl_mt)
                        print(f"New best HL: diff={diff:.3f} params={best_hl_params}")

    print("Best HL:", best_hl_params, "diff:", best_hl_diff)

    # Now optimize body params
    hl_size, hl_lh, hl_ls, hl_mt = best_hl_params
    best_body_diff = 999999
    best_body_params = None
    
    for body_size in [11.0, 11.2, 11.4, 11.5, 11.6, 11.8, 12.0]:
        for body_lh in [15.5, 16.0, 16.2, 16.5]:
            for body_ls in [-0.01, 0, 0.002, 0.005, 0.01]:
                for body_mt in [10, 11, 12, 13, 14, 15]:
                    html = html_template.format(
                        font_dir=font_dir,
                        img_uri=img_uri,
                        hl_size=hl_size,
                        hl_lh=hl_lh,
                        hl_ls=hl_ls,
                        hl_mt=hl_mt,
                        body_size=body_size,
                        body_lh=body_lh,
                        body_ls=body_ls,
                        body_mt=body_mt
                    )
                    page.set_content(html)
                    page.wait_for_timeout(20)
                    shot = page.screenshot()
                    test_img = Image.open(io.BytesIO(shot)).convert('RGB')
                    test_arr = np.array(test_img)
                    
                    diff = np.abs(ref_arr[40:140, 300:724, :].astype(int) - test_arr[40:140, 300:724, :].astype(int)).mean()
                    if diff < best_body_diff:
                        best_body_diff = diff
                        best_body_params = (body_size, body_lh, body_ls, body_mt)
                        print(f"New best Body: diff={diff:.3f} params={best_body_params}")

    print("Best Body:", best_body_params, "diff:", best_body_diff)
    
    # Save best screenshot and final diff
    body_size, body_lh, body_ls, body_mt = best_body_params
    html = html_template.format(
        font_dir=font_dir,
        img_uri=img_uri,
        hl_size=hl_size,
        hl_lh=hl_lh,
        hl_ls=hl_ls,
        hl_mt=hl_mt,
        body_size=body_size,
        body_lh=body_lh,
        body_ls=body_ls,
        body_mt=body_mt
    )
    page.set_content(html)
    page.wait_for_timeout(50)
    page.screenshot(path='public/debug_best_render.png')
    
    test_img = Image.open('public/debug_best_render.png').convert('RGB')
    test_arr = np.array(test_img)
    total_diff = np.abs(ref_arr.astype(int) - test_arr.astype(int))
    print(f"TOTAL MEAN DIFF ACROSS ALL PIXELS: {total_diff.mean():.3f}")
    
    diff_boost = Image.fromarray(np.clip(total_diff * 5, 0, 255).astype(np.uint8))
    diff_boost.save('public/debug_best_diff.png')
    
    browser.close()
