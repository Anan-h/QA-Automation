from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from intro_to_selenium.para_bank.logic.base_app_page import BaseAppPage


class MainPage(BaseAppPage):
    REGISTER_LINK = "//a[text()='Register']"
    USER_NAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_BUTTON = "//input[@value='Log In']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._register_link = self._driver.find_element(By.XPATH, self.REGISTER_LINK)
            self._uer_name_input = self._driver.find_element(By.XPATH, self.USER_NAME_INPUT)
            self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
        except NoSuchElementException as e:
            print("element not found", e)

    def click_on_register_link(self):
        self._register_link.click()

    def fill_user_name_input(self, user_name):
        self._uer_name_input.send_keys(user_name)

    def fill_password_input(self, password):
        self._password_input.send_keys(password)

    def click_on_login_button(self):
        self._login_button.click()

    def login_flow(self,user_name,password):
        self.fill_user_name_input(user_name)
        self.fill_password_input(password)
        self.click_on_login_button()
