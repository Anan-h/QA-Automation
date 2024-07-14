
import unittest,logging

from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.logic.borrow_page import BorrowPage
from intro_to_selenium.open_library.logic.login_page import LoginPage
from intro_to_selenium.open_library.logic.main_page import MainPage
from intro_to_selenium.open_library.logic.my_books_page import MyBooksPage


class TestBorrowingBook(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        logging.info("launched the Open Library website ")
        MainPage(self.driver).click_on_log_in_button()
        LoginPage(self.driver).login_flow(self.config["email"], self.config["password"])
        MyBooksPage(self.driver)

    def test_the_borrow_book_function(self):
        logging.info("testing the borrow book function")
        logging.info("###########################################")
        MyBooksPage(self.driver).navigate_to_home_page()
        MainPage(self.driver).click_on_borrow_button_by_index()
        reader_is_visible = BorrowPage(self.driver).book_reader_is_visible()
        self.assertTrue(reader_is_visible)

    def tearDown(self):
        self.driver.back()
        MainPage(self.driver).log_out()
        self.driver.quit()
        logging.info("______________________________________________")

