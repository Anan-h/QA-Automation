from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class LoginPage(BaseAppPage):
    EMAIL_INPUT = "//input[@id='username']"
    PASSWORD_INPUT = "//input[@id='password']"
    LOG_IN_BUTTON = "//button[@name='login']"
    INVALID_EMAIL_MSG = "//div[@class='note']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
            self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._login_button = self._driver.find_element(By.XPATH, self.LOG_IN_BUTTON)
        except NoSuchElementException as e:
            print(e)

    def fill_email_input(self, email):
        self._email_input.send_keys(email)

    def fill_password_input(self, password):
        self._password_input.send_keys(password)

    def click_on_login_button(self):
        self._login_button.click()

    def login_flow(self, email, password):
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.click_on_login_button()

    #after trying to log in through invalid data an error message shall appear
    #these two functions interact with that message

    def error_msg_is_visible(self):
        try:
            msg = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.INVALID_EMAIL_MSG))
            )
            return msg.is_displayed()
        except NoSuchElementException as e:
            print(e)

    def get_error_msg_text(self):
        try:
            msg = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.INVALID_EMAIL_MSG))
            )
            return msg.text
        except NoSuchElementException as e:
            print(e)

