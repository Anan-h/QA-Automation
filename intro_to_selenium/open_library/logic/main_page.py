import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class MainPage(BaseAppPage):
    BORROW_BUTTON = "//a[@data-ol-link-track='CTAClick|Borrow']"
    BOOK_LINK = "//img[@class='bookcover']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._borrow_buttons = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_any_elements_located((By.XPATH, self.BORROW_BUTTON))
            )
            self._books_links = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_any_elements_located((By.XPATH, self.BOOK_LINK))
            )
        except NoSuchElementException as e:
            logging.error(e)

    def click_on_first_borrow_button(self):
        """
        This function clicks on the first borrow button that is shown on the screen,
        :return:
        """
        self._borrow_buttons[0].click()
        logging.info("clicked on the first borrow button ")

    def click_on_first_book_link(self):
        """
        This function clicks on the first book link that is shown on the screen
        :return:
        """
        self._books_links[0].click()
        logging.info("clicked on the first book link ")
