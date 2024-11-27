from playwright.sync_api import Page, expect

def test_visual_homepage(page: Page, assert_snapshot):
    print("Given user visit homepage")
    page.goto("https://w3schools.com/")

    #comprueba que la captura de la pagina es igual a la mostrada
    assert_snapshot(page.screenshot())