import unittest
from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.logic.login_page import LoginPage
from intro_to_selenium.open_library.logic.main_page import MainPage
from intro_to_selenium.open_library.logic.my_books_page import MyBooksPage
from intro_to_selenium.open_library.logic.search_result_page import SearchResultPage


class TestSearchFunction(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        main_page = MainPage(self.driver)
        main_page.click_on_log_in_button()
        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config["email"], self.config["password"])
        self.my_books_page = MyBooksPage(self.driver)

    def test_search_for_a_book(self):
        self.my_books_page.search_flow(self.config["book_name"])
        matching_results = SearchResultPage(self.driver).get_matching_results_for_book(self.config["book_name"])
        self.assertGreaterEqual(len(matching_results), 1)

    def test_search_for_an_author(self):
        self.my_books_page.click_on_search_filter()
        self.my_books_page.select_author()
        self.my_books_page.search_flow(self.config["author_name"])
        author = SearchResultPage(self.driver).get_results_for_author_search()
        self.assertGreaterEqual(len(author), 1)

    def tearDown(self):
        SearchResultPage(self.driver).log_out()
        self.driver.quit()
