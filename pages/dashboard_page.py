from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def open_user_menu(self):
        self.page.locator(".oxd-userdropdown-tab").click()

    def logout(self):
        self.open_user_menu()
        self.page.get_by_text("Logout").click()