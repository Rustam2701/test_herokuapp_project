class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def click(self, selector):
        self.page.click(selector)

    def get_text(self, selector):
        return self.page.locator(selector).inner_text()
