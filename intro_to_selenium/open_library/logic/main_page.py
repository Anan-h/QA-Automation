from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class MainPage(BaseAppPage):
    TRENDING_LINK = "//a[@href='/trending/daily']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._trending_link = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.TRENDING_LINK))
            )
        except NoSuchElementException as e:
            print(e)

    def navigate_to_trending_books_page(self):
        self._trending_link.click()