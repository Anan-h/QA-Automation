from selenium.webdriver.common.by import By

from intro_to_selenium.open_library.infra.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = "//input[@id='username']"
    PASSWORD_INPUT = "//input[@id='password']"
    LOG_IN_BUTTON = "//button[@name='login']"

    def __init__(self, driver):
        super().__init__(driver)
        self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._login_button = self._driver.find_element(By.XPATH, self.LOG_IN_BUTTON)

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
