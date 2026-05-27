# Import the Page Object class we just created
from playwright.sync_api import expect
from login_page import LoginPage

def test_invalid_login_shows_error(page):
    login_page = LoginPage(page)
    
    # 1. Open the mock page
    login_page.navigate()
    
    # 2. Try logging in with incorrect credentials
    login_page.login("wrong_user", "wrong_password")
    
    # 3. Assert that the error banner appears and contains the expected text
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Your username is invalid!")