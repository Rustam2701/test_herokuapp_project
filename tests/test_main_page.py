from pages.main_page import MainPage
from playwright.sync_api import expect


def test_main_page(page):
    main_page = MainPage(page)

    main_page.open()

    expect(page).to_have_title("The Internet")
    expect(main_page.links).to_have_count(44)
    expect(main_page.has_github_button).to_be_visible()
