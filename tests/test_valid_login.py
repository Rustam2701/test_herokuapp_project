from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.security_page import SecurityPage
from configs.config import BASE_URL, VALID_USER, VALID_PASS


def test_successful_login_and_logout(page: Page):
    main_page = MainPage(page)
    login_page = LoginPage(page)
    security_page = SecurityPage(page)

    main_page.open()
    main_page.open_login_page.click()

    login_page.login_with_credentials(VALID_USER, VALID_PASS)

    expect(page).to_have_url(f"{BASE_URL}/secure")

    expect(security_page.header_title).to_be_visible()
    expect(security_page.header_title).to_have_text("Secure Area")

    expect(security_page.subheader_content).to_be_visible()
    expect(security_page.subheader_content).to_contain_text("Welcome to the Secure Area")

    expect(security_page.logout_button).to_be_visible()

    security_page.click_logout()

    expect(page).to_have_url(f"{BASE_URL}/login")
    expect(login_page.flash_message).to_be_visible()
    expect(login_page.flash_message).to_contain_text("You logged out of the secure area!")
