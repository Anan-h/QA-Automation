import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class TrendingPage(BaseAppPage):
    ALL_TIME_BUTTON = "//a[@href='/trending/forever']"
    TRENDING_TITLE = "//h1"
    TRENDING_BOOKS_TITLES = "//h3[@class='booktitle']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._all_time_button = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.ALL_TIME_BUTTON))
            )
            self._trending_title = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.TRENDING_TITLE))
            )
            self._trending_books = []
        except TimeoutException as e:
            logging.error(e)

    def click_on_all_time_trending_button(self):
        """
        This function clicks on the all-time button
        :return:
        """
        self._all_time_button.click()
        logging.info("clicked on all-time button")

    def title_is_visible(self):
        """
        This function checks if the title of the page is shown on the screen
        :return:True/False
        """
        if self._trending_title.is_displayed():
            logging.info("the title for the all-time trending books was displayed")
        else:
            logging.warning("the title for the all-time trending books was not displayed")
        return self._trending_title.is_displayed()

    def get_title_text(self):
        """
        This function extracts the title of the page
        :return:the title as text
        """
        logging.info(f"the title is: {self._trending_title.text}")
        return self._trending_title.text

    def get_trending_books_titles(self):
        """
        This function extracts the trending books titles
        :return: the books titles as list
        """
        try:
            self._trending_books = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_any_elements_located((By.XPATH, self.TRENDING_BOOKS_TITLES))
            )
            logging.info("extracted all the books title that are trending")
            return self._trending_books
        except TimeoutException as e:
            logging.error(e)
