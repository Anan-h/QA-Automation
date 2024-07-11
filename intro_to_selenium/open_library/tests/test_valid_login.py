import unittest

from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.logic.login_page import LoginPage
from intro_to_selenium.open_library.logic.main_page import MainPage
from intro_to_selenium.open_library.logic.my_books_page import MyBooksPage


class TestValidLogIn(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        self.main_page = MainPage(self.driver)

    def test_valid_login(self):
        #Arrange
        self.main_page.click_on_log_in_button()
        login_page = LoginPage(self.driver)
        #Act
        login_page.login_flow(self.config["email"], self.config["password"])
        #Assert
        my_books_page = MyBooksPage(self.driver)
        name = my_books_page.get_user_name()
        self.assertIn(self.config["name"], name)

    def tearDown(self):
        my_books_page = MyBooksPage(self.driver)
        my_books_page.log_out()
        self.driver.quit()

