from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page

    def go_to(self, url):
        self.page.goto(url)

    def assert_url_contains(self, text):
        assert text in self.page.url

    # UI assertions
    def assert_visible(self, locator):
        expect(locator).to_be_visible()

    def assert_text_visible(self, text):
        expect(self.page.get_by_text(text)).to_be_visible()