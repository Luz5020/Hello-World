from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://whatsmyuseragent.org/")
    page.screenshot(path="example.png")
    browser.close()
