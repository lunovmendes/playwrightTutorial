from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://accounts.autodesk.com/logon?resume=%2Fas%2FzrAYCsaYqm%2Fresume%2Fas%2Fauthorization.ping&spentity=null#username")
    page.wait_for_load_state()
    page.get_by_placeholder("name@example.com").fill("compras.informatica@vale.com")
    page.get_by_label("Next button").click()
    page.get_by_label("Password text field").fill("Asset.1234")
    page.get_by_label("Sign in button").click()



    page.get_by_role("button", name="Configurações").click()
    page.get_by_role("button", name="Informações pessoais").click()
    page.get_by_role("button", name="Segurança").click()
    page.get_by_test_id("uh-me-menu-button-user").click()
    page.locator("#uh-me-menu-link0_0").click()
    page.get_by_role("link", name="Por usuário", exact=True).click()
    page.get_by_role("button", name="Ken Pendlebury - 9857 - April").click()
    page.get_by_text("Contrato Julho").click()
    page.get_by_role("link", name="Exportar").click()
    page.locator("div").filter(has_text=re.compile(r"^Assinaturas$")).get_by_role("checkbox").uncheck()
    page.locator("div").filter(has_text=re.compile(r"^Uso$")).get_by_role("checkbox").uncheck()
    page.get_by_role("button", name="Exportar").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright: run(playwright)
