import datetime
import time
import unittest
from intro_to_selenium.para_bank.infra.config_provider import ConfigProvider
from intro_to_selenium.para_bank.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.para_bank.infra.utils import Utils_G
from intro_to_selenium.para_bank.logic.logged_in_page import LoggedInPage
from intro_to_selenium.para_bank.logic.login_failed import LogInFailed
from intro_to_selenium.para_bank.logic.main_page import MainPage


class LoginTest(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        self.driver.maximize_window()
        self.main_page = MainPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        self.main_page.login_flow(self.config["user_name"], self.config["password"])
        logged = LoggedInPage(self.driver)
        self.assertTrue(logged.title_is_displayed())
        self.assertEqual(logged.get_title_text(),"Accounts Overview")

    def test_login_invalid_user_name(self):
        self.main_page.login_flow(Utils_G.generate_string(4), self.config["password"])
        log = LogInFailed(self.driver)
        self.assertTrue(log.error_text_is_displayed())
        self.assertEqual(log.get_error_text(), "The username and password could not be verified.")

    def test_login_invalid_password(self):
        self.main_page.login_flow(self.config["user_name"], Utils_G.generate_string(4))
        log = LogInFailed(self.driver)
        self.assertTrue(log.error_text_is_displayed())
        self.assertEqual(log.get_error_text(), "The username and password could not be verified.")

