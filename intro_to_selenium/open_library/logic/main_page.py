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

    def click_on_borrow_button_by_index(self, index=0):
        """
        This function clicks on one of the borrow buttons that is shown on the screen,
        by default it clicks on the first one
        :param index:index of the desired borrow button to click
        :return:
        """
        self._borrow_buttons[index].click()
        logging.info(f"clicked on the borrow button located at the index:{index}")

    def click_on_book_link_by_index(self, index=0):
        """
        This function clicks on one of the book links that is shown on the screen,
        by default it clicks on the first one
        :param index:index of the desired book link to click
        :return:
        """
        self._books_links[index].click()
        logging.info(f"clicked on the book link located at the index:{index}")
