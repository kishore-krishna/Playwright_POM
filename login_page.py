from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Updated locators to match the mock site's HTML elements
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.error_message = page.locator("#flash")

    def navigate(self):
        # The live mock testing URL
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()