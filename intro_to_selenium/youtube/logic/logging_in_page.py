from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from intro_to_selenium.youtube.infra.base_page import BasePage


class LoggingInPage(BasePage):
    EMAIL_INPUT = "//input[@type='email']"
    NEXT_BTN = "//span[text()='Next']"
    ERROR_MSG = "//div/div[2]/div/div/div[1]//div/div/div[1]/div/div[2]/div[2]/div"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
            self._next_btn = self._driver.find_element(By.XPATH, self.NEXT_BTN)
        except NoSuchElementException as e:
            print("element not found", e)

    def fill_email_input(self, text):
        self._email_input.send_keys(text)

    def click_on_next_btn(self):
        self._next_btn.click()

    def login_flow(self, text):
        self.fill_email_input(text)
        self.click_on_next_btn()

    def error_is_displayed(self):

        try:
            msg = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.ERROR_MSG)))
            return msg.is_displayed()
        except TimeoutException as e:
            print(e)

    def get_error_text(self):
        try:
            msg = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.ERROR_MSG)))
            return msg.text
        except TimeoutException as e:
            print(e)
