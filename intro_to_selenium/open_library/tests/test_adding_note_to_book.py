import unittest,logging

from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.infra.utils import Utils
from intro_to_selenium.open_library.logic.book_page import BookPage
from intro_to_selenium.open_library.logic.login_page import LoginPage
from intro_to_selenium.open_library.logic.main_page import MainPage
from intro_to_selenium.open_library.logic.my_books_page import MyBooksPage


class TestAddingNoteToABook(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        logging.info("launched the Open Library website ")
        MainPage(self.driver).click_on_log_in_button()
        LoginPage(self.driver).login_flow(self.config["email"], self.config["password"])
        MyBooksPage(self.driver)

    def test_adding_note_to_a_book(self):
        logging.info("testing adding note to a book")
        logging.info("###########################################")
        MyBooksPage(self.driver).navigate_to_home_page()
        MainPage(self.driver).click_on_book_link_by_index()
        BookPage(self.driver).adding_note_flow(Utils.generate_string_of_letters(40))
        self.assertTrue(BookPage(self.driver).confirmation_message_appearance())
        self.driver.save_screenshot('adding note confirmation.png')

    def tearDown(self):
        BookPage(self.driver).log_out()
        self.driver.quit()
        logging.info("______________________________________________")
