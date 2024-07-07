from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from intro_to_selenium.para_bank.logic.base_app_page import BaseAppPage


class RegisteredPage(BaseAppPage):
    TITLE = "//h1[@class='title']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._title = self._driver.find_element(By.XPATH, self.TITLE)
        except NoSuchElementException as e:
            print("element not found", e)

    def title_is_displayed(self):
        return self._title.is_displayed()

    def get_title_text(self):
        return self._title.text
