import unittest
from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.logic.main_page import MainPage
from intro_to_selenium.open_library.logic.search_result_page import SearchResultPage


class TestSearchFunction(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        MainPage(self.driver)

    def test_search_for_a_book(self):
        MainPage(self.driver).search_flow(self.config["book_name"])
        matching_results = SearchResultPage(self.driver).get_matching_results_for_book(self.config["book_name"])
        self.assertGreaterEqual(len(matching_results), 1)

    def test_search_for_an_author(self):
        MainPage(self.driver).click_on_search_filter()
        MainPage(self.driver).select_author()
        MainPage(self.driver).search_flow(self.config["author_name"])
        author_search = SearchResultPage(self.driver).get_results_for_author_search()
        self.assertGreaterEqual(len(author_search), 1)

    def tearDown(self):
        self.driver.quit()
