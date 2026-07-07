import pytest
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from pages.login_page import LoginPage
from configs.config import VALID_USER, VALID_PASS


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("invalid_user", VALID_PASS, "Your username is invalid!"),
        (VALID_USER, "WrongPassword!", "Your password is invalid!"),
        ("invalid_user", "WrongPassword!", "Your username is invalid!"),
        (None, None, "Your username is invalid!"),
        ("TomSmith", VALID_PASS, "Your username is invalid!"),
        ("' OR '1'='1", "' OR '1'='1", "Your username is invalid!"),
    ],
    ids=[
        "wrong_user_correct_pass",
        "correct_user_wrong_pass",
        "both_invalid",
        "empty_fields",
        "case_sensitivity",
        "sql_injection_attempt"
    ]
)
def test_login_with_invalid_credentials(page: Page, username, password, expected_error):
    main_page = MainPage(page)
    login_page = LoginPage(page)

    main_page.open()
    main_page.open_login_page.click()

    login_page.login_with_credentials(username, password)

    expect(login_page.flash_message).to_be_visible()
    expect(login_page.flash_message).to_contain_text(expected_error)
