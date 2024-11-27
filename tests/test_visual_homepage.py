from playwright.sync_api import Page, expect
import utils

def test_visual_homepage(page: Page, assert_snapshot):
    if not utils.is_mobile(page):
        print("Given user visit homepage")
        page.goto("https://w3schools.com/")

        #comprueba que la captura de la pagina es igual a la mostrada
        assert_snapshot(page.screenshot())