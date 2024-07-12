import unittest
from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.logic.login_page import LoginPage
from intro_to_selenium.open_library.logic.main_page import MainPage
from intro_to_selenium.open_library.logic.my_books_page import MyBooksPage
from intro_to_selenium.open_library.logic.trending_page import TrendingPage


class ShowTrendingBooksAllTime(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        main_page = MainPage(self.driver)
        main_page.click_on_log_in_button()
        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config["email"], self.config["password"])
        self.my_books_page = MyBooksPage(self.driver)

    def test_show_trending_all_times_books(self):
        self.my_books_page.click_on_browse_button()
        self.my_books_page.click_on_trending_button()
        TrendingPage(self.driver).click_on_all_time_trending_button()
        self.assertEqual(self.driver.current_url, self.config["trending_all_time_url"])
        self.assertEqual(TrendingPage(self.driver).get_title_text(), self.config["trending_all_time_title"])

    def tearDown(self):
        TrendingPage(self.driver).log_out()
        self.driver.quit()
