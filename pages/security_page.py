from pages.base_page import BasePage


class SecurityPage(BasePage):

    @property
    def header_title(self):
        return self.page.locator("h2")

    @property
    def subheader_content(self):
        return self.page.locator("h4.subheader")

    @property
    def logout_button(self):
        return self.page.get_by_role("link", name="Logout")

    def click_logout(self):
        self.logout_button.click()
