import logging

from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.open_library.infra.base_page import BasePage


class BorrowPage(BasePage):
    BOOK_READER = "//div[@id='BookReader']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._reader = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.BOOK_READER))
            )
        except NoSuchElementException as e:
            logging.error(e)

    def book_reader_is_visible(self):
        """
        A function that checks if the book reading theater is displayed on the screen
        :return:True or False
        """
        if self._reader.is_displayed():
            logging.info("the book reader was displayed")
        else:
            logging.warning("the book reader was not displayed")
        return self._reader.is_displayed()
