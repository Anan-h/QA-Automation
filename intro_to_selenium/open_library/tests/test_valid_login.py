import logging
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
        logging.info("launched the Open Library website ")
        MainPage(self.driver)

    def test_valid_login(self):
        logging.info("testing login with valid account data")
        logging.info("###########################################")
        MainPage(self.driver).click_on_log_in_button()
        LoginPage(self.driver).login_flow(self.config["email"], self.config["password"])
        name = MyBooksPage(self.driver).get_user_name()
        self.assertIn(self.config["name"], name)

    def tearDown(self):
        MyBooksPage(self.driver).log_out()
        self.driver.quit()
        logging.info("______________________________________________")

