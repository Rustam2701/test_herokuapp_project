from pages.base_page import BasePage


class LoginPage(BasePage):

    @property
    def username_input(self):
        return self.page.locator("#username")

    @property
    def password_input(self):
        return self.page.locator("#password")

    @property
    def login_button(self):
        return self.page.locator("button[type='submit']")

    @property
    def flash_message(self):
        return self.page.locator("#flash")

    def login_with_credentials(self, username: str, password: str):
        if username is not None:
            self.username_input.fill(username)
        else:
            self.username_input.clear()

        if password is not None:
            self.password_input.fill(password)
        else:
            self.password_input.clear()

        self.login_button.click()

    def get_flash_message_text(self) -> str:
        return self.flash_message.inner_text()
