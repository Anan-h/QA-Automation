import unittest

from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.logic.borrow_page import BorrowPage
from intro_to_selenium.open_library.logic.login_page import LoginPage
from intro_to_selenium.open_library.logic.main_page import MainPage
from intro_to_selenium.open_library.logic.my_books_page import MyBooksPage


class TestBorrowing_book(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        main_page = MainPage(self.driver)
        main_page.click_on_log_in_button()
        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config["email"], self.config["password"])
        self.my_books_page = MyBooksPage(self.driver)

    def test_the_borrow_ending_message_visibility(self):
        self.my_books_page.navigate_to_home_page()
        home = MainPage(self.driver)
        home.click_on_the_first_borrow_button()
        self.borrow = BorrowPage(self.driver)
        reader_is_visible = self.borrow.book_reader_is_visible()
        self.assertTrue(reader_is_visible)

    def tearDown(self):
        self.driver.back()
        MainPage(self.driver).log_out()
        self.driver.quit()

