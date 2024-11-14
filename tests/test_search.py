from playwright.sync_api import Page, expect

def test_search_empty(page:Page):
    print("Given the user is on the w3school homepage")
    page.goto("https://www.w3schools.com/")

    #print("When the user accept the cookies")
    #page.get_by_text("Accept all & visit the site").click()

    print("And the user search with empty value")
    page.get_by_placeholder("Search our tutorials, e.g.").clear()
    #Presiona la tecla enter
    page.get_by_placeholder("Search our tutorials, e.g.").press("Enter")

    print("Then the user should keep seeing search bar")
    expect(page.get_by_placeholder("Search our tutorials, e.g.")).to_be_visible()

def test_search_valid_value(page:Page):
    print("Given the user open w3school homepage")
    page.goto("https://www.w3schools.com/")

    #print("When user accept cookies")
    #page.get_by_text("Accept all & visit the site").click()

    print("And the user search for HTML content")
    page.get_by_placeholder("Search our tutorials, e.g.").click()
    page.get_by_placeholder("Search our tutorials, e.g.").fill("HTML")
    page.get_by_placeholder("Search our tutorials, e.g.").press("Enter")

    print("Then the user should see HTML Tutorial page")
    expect(page.locator("h1")).to_contain_text("HTML Tutorial")