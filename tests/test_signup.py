from playwright.sync_api import Page, expect
import uuid
def generar_email_aleatorio():
    textounico = uuid.uuid4().hex
    random_email = textounico + "@test.com"
    return random_email

def test_signup_with_valid_email(page:Page):
    print("Given user visit signup page")
    page.goto("https://profile.w3schools.com/signup")

    print("When the user fill email with valid email")
    #Limpiamos el campo email con .clear
    page.get_by_placeholder("email").clear()
    #Introducimos un email aleatorio y rellenamos el campo con placeholder email con ese email aleatorio
    email = generar_email_aleatorio()
    page.get_by_placeholder("email").fill(email)

    print("And the user fill password with valid password")
    password = "Test-1234"
    #limpiamos el campo password
    page.get_by_placeholder("password").clear()
    #Rellenamos el campo password con una password correcta
    page.get_by_placeholder("password").fill(password)

    print("And the user fill the name")
    page.get_by_placeholder("first name").clear()
    #Rellenamos el campo password con una password correcta
    page.get_by_placeholder("first name").fill("Test Name")

    print("And the user fill the last name")
    page.get_by_placeholder("last name").clear()
    #Rellenamos el campo password con una password correcta
    page.get_by_placeholder("last name").fill("Test Last Name")

    print("And the user click on signup button")
    #Hacemos click en el boton sigunp
    page.get_by_role("button",name="Sign Up").click()

    print("Then the user should see verify your email message")
    #Buscamos un elemento que contenga el texto Verify your email y comprobamos que este visible
    expect(page.get_by_text("Verify your email")).to_be_visible

def test_signup_with_empty_email(page:Page):
    print("Given the user open w3school signup page")
    page.goto("https://profile.w3schools.com/signup")

    print("When user leaves empty email")
    #dejamos vacio el campo email con clear
    page.get_by_placeholder("email").clear()

    print("And the user fill password")
    page.get_by_placeholder("password").clear()
    page.get_by_placeholder("password").fill("Test-1234")

    print("And the user fill first name and last name")
    page.get_by_placeholder("first name").clear()
    page.get_by_placeholder("first name").fill("Reyes")

    print("and the user fill last name")
    page.get_by_placeholder("last name").clear()
    page.get_by_placeholder("last name").fill("Cuesta")

    print("and the user click sign up button")
    page.get_by_role("button", name="Sign Up").click()

    print("Then the user should see error message")
    expect(page.get_by_text("Please fill in all fields")).to_be_visible()

def test_signup_with_empty_password(page:Page):
    print("Given the user visit signup w3school page")
    page.goto("https://profile.w3schools.com/signup")

    print("And the user fill email with valid email")
    page.get_by_placeholder("email").clear()
    page.get_by_placeholder("email").fill("reyes@gmail.com")

    print("And the user fill first name")
    page.get_by_placeholder("first name").clear()
    page.get_by_placeholder("first name").fill("Reyes")

    print("And the user fill last name")
    page.get_by_placeholder("last name").clear()
    page.get_by_placeholder("last name").fill("Cuesta")

    print("And the user click sign up button")
    page.get_by_role("button", name="Sign Up").click()

    print("Then the user should see an error message")
    expect(page.get_by_text("Please fill in all fields")).to_be_visible()

