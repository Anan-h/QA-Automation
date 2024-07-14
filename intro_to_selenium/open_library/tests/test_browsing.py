import logging
import unittest
from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.logic.book_page import BookPage
from intro_to_selenium.open_library.logic.main_page import MainPage
from intro_to_selenium.open_library.logic.trending_page import TrendingPage


class TestBrowsing(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        logging.info("launched the Open Library website ")
        MainPage(self.driver).click_on_browse_button()

    def test_show_a_random_book(self):
        logging.info("testing the view of a random book ")
        logging.info("###########################################")
        MainPage(self.driver).click_on_random_book()
        self.assertTrue(BookPage(self.driver).book_title_is_visible())

    def test_show_trending_all_time_books(self):
        logging.info("testing the view of all-time trending books")
        logging.info("###########################################")
        MainPage(self.driver).click_on_trending_button()
        TrendingPage(self.driver).click_on_all_time_trending_button()
        self.assertEqual(self.driver.current_url, self.config["trending_all_time_url"])
        self.assertEqual(TrendingPage(self.driver).get_title_text(), self.config["trending_all_time_title"])

    def tearDown(self):
        logging.info("______________________________________________")
