import pytest
from playwright.sync_api import expect
from config import USERNAME, PASSWORD


# TC_001 Valid Login
@pytest.mark.smoke
def test_validlogin(login):

    login.login(USERNAME, PASSWORD)
    login.page.wait_for_timeout(2000)
    login.assert_url_contains("dashboard")


# TC_002 Invalid Username
@pytest.mark.regression
def test_wrongusername(login):

    login.login("WrongUser", PASSWORD)
    login.assert_text_visible("Invalid credentials")


# TC_003 Invalid Password
def test_invalid_password(login):

    login.login(USERNAME, "WrongPass")
    login.assert_text_visible("Invalid credentials")


# TC_004 Empty Username
def test_empty_username(login):

    login.login("", PASSWORD)
    login.assert_text_visible("Required")


# TC_005 Empty Password
def test_empty_password(login):

    login.login(USERNAME, "")
    login.assert_text_visible("Required")


# TC_006 Login UI
def test_login_page_ui(login):

    login.assert_visible(login.page.get_by_placeholder("Username"))
    login.assert_visible(login.page.get_by_placeholder("Password"))
    login.assert_visible(login.page.get_by_role("button", name="Login"))


# TC_007 Logout
def test_logout(login, dashboard):

    login.login(USERNAME, PASSWORD)

    dashboard.logout()

    login.assert_url_contains("auth/login")


# TC_008 Session Security
def test_session_security(login, dashboard):

    login.login(USERNAME, PASSWORD)

    dashboard.logout()

    login.page.goto(BASE_URL := "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    login.assert_url_contains("auth/login")