from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        'https://acconsulti.safewebpss.com.br/gerenciamentoac/#/pages/relatorios/relatorio-emissao')
    page.wait_for_timeout(2000)
    browser.close()
