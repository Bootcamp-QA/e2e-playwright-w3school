from playwright.sync_api import Page, expect
import re

def test_visit_menu_links(page:Page):
    print("Given the user visit homepage w3school")
    #Navegacion, abrir la url en el navegador
    page.goto("https://www.w3schools.com/")

    print("When the user accept the cookies")
    #Localizamos el elemento por texto.
    page.get_by_text("Accept all").click()
    page.wait_for_url("https://www.w3schools.com/")


    print("And click on HTML menu")
    #Localizamos el elemento por rol (button, link, heading) y por texto EXACTO.
    page.get_by_role("link", name="HTML", exact=True).click()


    print("Then user should be on HTML Tutorial page")
    #Comprobamos que la url de la pagina tiene la url exacta
    expect(page).to_have_url("https://www.w3schools.com/html/default.asp")
    #Comprueba que la url de la pagina contiene la palabra html
    expect(page).to_have_url(re.compile("html"))
    #Comprueba que el titula de la pagina tiene el texto exacto HTML Tutorial
    expect(page).to_have_title("HTML Tutorial")
    #Localizamos el elemento con titulo heading (h1), que tenga el texto exacto HTML Tutorial.
    expect(page.get_by_role("heading", name="HTML Tutorial", exact=True)).to_be_visible

    print("And click on CSS menu")
    page.get_by_role("link", name="CSS", exact=True).click()

    print("Then the user should be on CSS Tutorial page")
    expect(page).to_have_url("https://www.w3schools.com/css/default.asp")
    expect(page).to_have_title("CSS Tutorial")
    expect(page.get_by_role("heading", name="CSS Tutorial", exact=True)).to_be_visible


    print("And click on JAVASCRIPT menu")
    page.get_by_role("link", name="JAVASCRIPT", exact=True).click()

    print("Then the user should be on Javascript Tutorial page")
    expect(page).to_have_url("https://www.w3schools.com/js/default.asp")
    expect(page).to_have_title("JavaScript Tutorial")
    expect(page.get_by_role("heading", name="JavaScript Tutorial", exact=True)).to_be_visible


    print("And click on SQL menu")
    page.get_by_role("link", name="SQL", exact=True).click()

    print("Then the user should be on SQL Tutorial page")
    expect(page).to_have_url("https://www.w3schools.com/sql/default.asp")
    expect(page).to_have_title("SQL Tutorial")
    expect(page.get_by_role("heading", name="SQL Tutorial", exact=True)).to_be_visible

    print("And click on PYTHON menu")
    page.get_by_role("link", name="PYTHON", exact=True).click()

    print("Then the user should be on Python Tutorial page")
    expect(page).to_have_url("https://www.w3schools.com/python/default.asp")
    expect(page).to_have_title("Python Tutorial")
    expect(page.get_by_role("heading", name="Python Tutorial", exact=True)).to_be_visible

    print("And click on JAVA menu")
    page.get_by_role("link", name="JAVA", exact=True).click()

    print("Then the user should be on Java Tutorial page")
    expect(page).to_have_url("https://www.w3schools.com/java/default.asp")
    expect(page).to_have_title("Java Tutorial")
    expect(page.get_by_role("heading", name=" Tutorial", exact=True)).to_be_visible
    
