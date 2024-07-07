from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from intro_to_selenium.para_bank.logic.base_app_page import BaseAppPage


class LogInFailed(BaseAppPage):
    ERROR_TEXT = "//p[@class='error']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._error_text = self._driver.find_element(By.XPATH, self.ERROR_TEXT)
        except NoSuchElementException as e:
            print("element not found", e)

    def error_text_is_displayed(self):
        return self._error_text.is_displayed()

    def get_error_text(self):
        return self._error_text.text
