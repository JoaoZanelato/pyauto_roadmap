from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # Headless (does not open a browser window)
    page = browser.new_page()
    page.goto('https://www.hashtagtreinamentos.com/pg-inscricao-python-impressionador#secao-oferta')
    page.locator('xpath=//*[@id="botao-link-padrao1"]').click()
    page.locator('xpath=//*[@id="fullname"]').fill('John Doe')
    page.locator('xpath=//*[@id="email"]').fill('john.doe@example.com')
    page.locator('xpath=//*[@id="field[59]"]').fill('54')
    page.locator('xpath=//*[@id="field[60]"]').fill('999999999')
    page.locator('xpath=//*[@id="_form_5346_submit"]').click()
    time.sleep(5) # Wait for 5 seconds to see the page
    browser.close()