from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class SearchResultPage(BaseAppPage):
    BOOK_TITLE_PATH = "//a[contains(text(),'')]"
    AUTHOR_SEARCH_RESULTS = "//li[@class='searchResultItem']"

    def __init__(self, driver):
        super().__init__(driver)
        self._results_books_titles = []
        self._results_for_author = []

    def get_matching_results_for_book(self, title):
        """
        a function that returns a list of all the titles that match the search input
        :param title: the input of the search
        :return: list of all the titles
        """
        try:
            self._results_books_titles = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_any_elements_located((By.XPATH, f"//a[contains(text(),'{title}')]"))
            )
            return self._results_books_titles
        except TimeoutException as e:
            print(e)

    def click_on_book_title_by_index(self, title, index=0):
        """
        This function clicks on a certain title from the search results according to given index
        by default it clicks on the first title
        :param title: input of the search
        :param index: index of the desired title
        :return:
        """
        results = self.get_matching_results_for_book(title)
        try:
            results[index].click()
        except IndexError as e:
            print(e)

    def get_results_for_author_search(self):
        """
        This function extracts the search results for an author
        :return: the results as list
        """
        try:
            self._results_for_author = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_any_elements_located((By.XPATH, self.AUTHOR_SEARCH_RESULTS))
            )
            return self._results_for_author
        except TimeoutException as e:
            print(e)
