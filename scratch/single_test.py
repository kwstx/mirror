import os
from playwright.sync_api import sync_playwright
from PIL import Image
import numpy as np

font_dir = os.path.abspath('public/fonts').replace('\\', '/')
img_uri = os.path.abspath('public/images/party_of_four_cards.png').replace('\\', '/')

html_content = f"""<!DOCTYPE html>
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
  padding-top: 1.5px;
}}
.headline {{
  font-family: 'Society', Georgia, serif;
  font-weight: 800;
  font-size: 27.8px;
  line-height: 28px;
  letter-spacing: -0.012em;
  color: #ffffff;
  margin-bottom: 12px;
}}
.headline-italic {{
  font-style: italic;
}}
.body-text {{
  font-family: 'Modern Era', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 11.35px;
  line-height: 16px;
  letter-spacing: 0.003em;
  color: #ffffff;
  text-align: center;
}}
.body-text p {{
  margin: 0;
  padding: 0;
  white-space: nowrap;
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
  <h2 class="headline">
    Party of <span class="headline-italic">four</span>
  </h2>
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

with open('public/test_single_render.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page()
    page.set_viewport_size({'width': 1024, 'height': 425})
    file_path = os.path.abspath('public/test_single_render.html').replace('\\', '/')
    page.goto(f'file:///{file_path}')
    page.wait_for_timeout(300)
    page.screenshot(path='public/debug_single_render.png')
    browser.close()

ref = Image.open('public/images/party_of_four_reference.png').convert('RGB')
test = Image.open('public/debug_single_render.png').convert('RGB')

ref_arr = np.array(ref)
test_arr = np.array(test)

diff = np.abs(ref_arr.astype(int) - test_arr.astype(int))
print(f"Total Mean Diff: {diff.mean():.4f}")
print(f"Headline Diff (y:0..40): {diff[0:40, :, :].mean():.4f}")
print(f"Body Diff (y:40..130): {diff[40:130, :, :].mean():.4f}")
print(f"Cards Diff (y:150..425): {diff[150:425, :, :].mean():.4f}")

diff_boost = Image.fromarray(np.clip(diff * 5, 0, 255).astype(np.uint8))
diff_boost.save('public/debug_single_diff.png')
