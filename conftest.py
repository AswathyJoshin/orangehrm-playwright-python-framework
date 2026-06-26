import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def login(page):
    login_page = LoginPage(page)
    login_page.open()   # opens automatically
    return login_page


@pytest.fixture
def dashboard(page):
    return DashboardPage(page)