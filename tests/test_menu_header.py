from playwright.sync_api import Page, expect
import re
import utils

def test_visit_menu_header_links(page:Page):
    print("Given user visit w3school homepage")
    page.goto("https://www.w3schools.com/")

    print("And accept all cookies")
    page.get_by_text("Accept all & visit the site").click()
    
    print("When visit menu Tutorials")
    #Si es tamanio movil, hace click en el boton menu.
    if(utils.is_mobile(page)):
        page.get_by_label("Menu", exact=True).click()

    #Luego hace click en tutorial
    page.get_by_role("button", name="Tutorials").click()
    page.get_by_title("HTML Tutorial").nth(1).click()

    print("Then should see Tutorial page")
    expect(page.locator("#main").get_by_text("Tutorial", exact=True)).to_be_visible()

    print("When visit menu exercises")
    if(utils.is_mobile(page)):
        page.get_by_label("Menu", exact=True).click()

    page.get_by_role("button", name="Exercises").click()
    page.get_by_title("HTML Exercises").nth(1).click()

    print("Then should see Exercises page")
    expect(page.get_by_role("heading", name="HTML Exercises").locator("span")).to_be_visible()
    
    print("When visit menu Services, Free tutorials")
    if(utils.is_mobile(page)):
        page.get_by_label("Menu", exact=True).click()
        
    page.get_by_role("button", name="Services").click()
    page.get_by_role("link", name="Free tutorials").click()

    print("Then should see Services Free Tutorials page")
    expect(page.locator("h1")).to_contain_text("Tutorials")


