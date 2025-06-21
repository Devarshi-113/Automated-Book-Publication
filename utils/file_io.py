# utils/file_io.py

import os

def save_raw_html(url, html_text, chapter_name="Chapter_1"):
    """Save raw HTML text to data/raw_html/Chapter_1.html"""
    os.makedirs("data/raw_html", exist_ok=True)
    file_path = os.path.join("data", "raw_html", f"{chapter_name}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_text)

def save_screenshot(url, save_dir="data"):
    from playwright.sync_api import sync_playwright

    chapter_name = sanitize_filename(url)
    os.makedirs(f"{save_dir}/screenshots", exist_ok=True)
    file_path = f"{save_dir}/screenshots/{chapter_name}.png"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.screenshot(path=file_path, full_page=True,timeout=60000)
        browser.close()


import re
from urllib.parse import urlparse

def sanitize_filename(url):
    """
    Convert URL into a safe string to use as a filename
    """
    parsed = urlparse(url)
    path = parsed.path  # /wiki/...
    filename = path.replace('/', '_').replace(' ', '_')
    filename = re.sub(r'[^A-Za-z0-9_\-]', '', filename)
    return filename.strip('_') or "chapter"