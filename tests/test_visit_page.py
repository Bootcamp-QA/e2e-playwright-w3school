from playwright.sync_api import Page, expect

def test_visit(page: Page):
    print("Given user visit homepage")
    page.goto("https://w3schools.com")
    #page.pause()

    #EJEMPLOS LOCALIZADORES
    #IMAGEN POR ALT
    #page.get_by_alt_text("Code Game")
    #ELEMENTO POR TITLE. Filtrar de todos cuando hay varios, el que tenga el texto Tutorial
    #page.get_by_title("HTML Tutorial").filter(has_text="Tutorial")
    #ELEMENTO POR TITLE. DE TODOS COGER EL PRIMERO. EL ULTIMO. O EL DE LA POSICION 0,1,2..
    #page.get_by_title("HTML Tutorial").first
    #page.get_by_title("HTML Tutorial").last
    #page.get_by_title("HTML Tutorial").nth(1) #posicion 2
    #Localizar por id el menu
    #page.locator("#subtopnav")
    #Localizar por clase
    #page.locator(".classic")
    #Localizar por elemento
    #page.locator("h1")
    #Localizar por atributo
    #page.locator("input[aria-label='Search our tutorials']")
    #Localizadores anidados
    #locator("#subtopnav").locator("a").filter(has_text="MYSQL")