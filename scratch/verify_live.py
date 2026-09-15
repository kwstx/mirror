import os, time, threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright
from PIL import Image
import numpy as np

os.chdir(r'c:\Users\galan\mirror\dist')

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

server = HTTPServer(('127.0.0.1', 8080), QuietHandler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()
print('HTTP server running on http://127.0.0.1:8080')

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='msedge', headless=True)
        page = browser.new_page()
        page.set_viewport_size({'width': 1024, 'height': 800})
        page.goto('http://127.0.0.1:8080', wait_until='networkidle')
        page.wait_for_timeout(1000)
        
        # Scroll to double date section
        el = page.locator('#double-date-section')
        el.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        
        # Screenshot the section
        os.chdir(r'c:\Users\galan\mirror')
        el.screenshot(path='public/debug_live_section_screenshot.png')
        page.screenshot(path='public/debug_live_page_screenshot.png')
        browser.close()
    
    print('Live section screenshot captured successfully!')
    
    # Compare with reference
    ref = Image.open('public/images/party_of_four_reference.png').convert('RGB')
    live = Image.open('public/debug_live_section_screenshot.png').convert('RGB')
    
    print(f'Ref size: {ref.size}, Live size: {live.size}')
    
    # Check bounding boxes
    bg = np.array([90, 0, 15])
    ref_arr = np.array(ref)
    live_arr = np.array(live)
    
    print('Cards region diff (y:150..425):', np.abs(ref_arr[150:425, :, :].astype(int) - live_arr[150:425, :, :].astype(int)).mean())
    print('Total section mean diff:', np.abs(ref_arr.astype(int) - live_arr.astype(int)).mean())
    
finally:
    server.shutdown()
