import unittest
from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.logic.book_page import BookPage
from intro_to_selenium.open_library.logic.login_page import LoginPage
from intro_to_selenium.open_library.logic.main_page import MainPage
from intro_to_selenium.open_library.logic.my_books_page import MyBooksPage


class TestRatingBook(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        MainPage(self.driver).click_on_log_in_button()
        LoginPage(self.driver).login_flow(self.config["email"], self.config["password"])
        MyBooksPage(self.driver)

    def test_rating_a_book_at_top_rating(self):
        MyBooksPage(self.driver).navigate_to_home_page()
        MainPage(self.driver).click_on_book_link_by_index()
        BookPage(self.driver).rate_as_top_rating()
        btn_is_visible = BookPage(self.driver).clear_rating_button_is_visible()
        self.assertTrue(btn_is_visible)

    def tearDown(self):
        BookPage(self.driver).click_on_clear_rating_button()
        BookPage(self.driver).log_out()
        self.driver.quit()
