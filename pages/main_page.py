from pages.base_page import BasePage
from configs.config import BASE_URL


class MainPage(BasePage):

    def open(self):
        super().open(BASE_URL)

    @property
    def open_login_page(self):
        return self.page.get_by_role("link", name="Form Authentication")

    @property
    def links(self):
        return self.page.locator("#content ul li a")

    @property
    def has_github_button(self):
        return self.page.get_by_role("img", name="Fork me on GitHub")
