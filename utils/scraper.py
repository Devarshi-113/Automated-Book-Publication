from playwright.sync_api import sync_playwright
import os

def scrape_chapter(url, save_dir="data"):
    os.makedirs(f"{save_dir}/raw_html", exist_ok=True)
    os.makedirs(f"{save_dir}/screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_default_timeout(60000)           
        page.set_default_navigation_timeout(60000)
        page.goto(url, timeout=60000) 
        html = page.content()

        chapter_name = url.strip("/").split("/")[-1]
        html_path = f"{save_dir}/raw_html/{chapter_name}.html"
        screenshot_path = f"{save_dir}/screenshots/{chapter_name}.png"

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)

        page.screenshot(path=screenshot_path, full_page=True,timeout=60000)
        browser.close()

    return html_path, screenshot_path
