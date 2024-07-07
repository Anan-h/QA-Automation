from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from intro_to_selenium.para_bank.infra.page import Page


class BaseAppPage(Page):
    HOME_BUTTON = "//a[text()='Home']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._home_btn = self._driver.find_element(By.XPATH, self.HOME_BUTTON)
        except NoSuchElementException as e:
            print("element not found", e)

    def click_on_home_button(self):
        self._home_btn.click()
