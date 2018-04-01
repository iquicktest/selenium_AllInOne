from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FlightLoginPage(BasePage):
    _username_textbox = (By.NAME, "userName")
    _password_textbox = (By.NAME, "password")
    _login_button = (By.NAME, "login")
    _login_success_msg = (By.XPATH, "//a[.='SIGN-OFF']")
    _login_failed_msg = (By.XPATH, "//font[contains(.,'Enter your user information')]")

    def __init__(self, driver):
        self.driver = driver
        self._goto('/')

    def login_with(self, usr, pwd):
        self._input(self._username_textbox, usr)
        self._input(self._password_textbox, pwd)
        self._click(self._login_button)

    def success_msg_exist(self):
        return self._is_displayed(self._login_success_msg)

    def failed_msg_exist(self):
        return self._is_displayed(self._login_failed_msg)
