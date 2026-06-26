from pages.base_page import BasePage
from config import BASE_URL


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        self.go_to(BASE_URL)

    def login(self, username, password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()



