import unittest

from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.logic.book_page import BookPage
from intro_to_selenium.open_library.logic.login_page import LoginPage
from intro_to_selenium.open_library.logic.main_page import MainPage
from intro_to_selenium.open_library.logic.my_books_page import MyBooksPage


class ShowARandomBookTest(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        main_page = MainPage(self.driver)
        main_page.click_on_log_in_button()
        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config["email"], self.config["password"])
        self.my_books_page = MyBooksPage(self.driver)

    def test_show_a_random_book(self):
        self.my_books_page.click_on_browse_button()
        self.my_books_page.click_on_random_book()
        self.assertTrue(BookPage(self.driver).book_title_is_visible())

    def tearDown(self):
        BookPage(self.driver).log_out()
        self.driver.quit()
