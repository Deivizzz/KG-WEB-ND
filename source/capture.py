from playwright.sync_api import sync_playwright
from pathlib import Path
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os
os.chdir("/mnt/data/Nexus_Digital")
server=ThreadingHTTPServer(("127.0.0.1",8766),SimpleHTTPRequestHandler)
threading.Thread(target=server.serve_forever,daemon=True).start()
P=Path('/mnt/data/Nexus_Digital')
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--no-proxy-server','--proxy-bypass-list=*'])
 page=browser.new_page(viewport={'width':1440,'height':900},device_scale_factor=1)
 page.goto('http://127.0.0.1:8766/index.html',wait_until='load')
 page.evaluate('document.fonts.ready')
 height=page.evaluate('document.documentElement.scrollHeight')
 print('dimensions',height)
 page.screenshot(path=str(P/'Nexus_Digital_1440px.png'),full_page=True,animations='disabled')
 page.pdf(path=str(P/'Nexus_Digital_dizainas.pdf'),width='1440px',height=f'{height}px',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'},prefer_css_page_size=False)
 page.set_viewport_size({'width':390,'height':844})
 page.screenshot(path=str(P/'Nexus_Digital_mobilus.png'),full_page=True,animations='disabled')
 print('mobile scroll width',page.evaluate('document.documentElement.scrollWidth'))
 browser.close()
