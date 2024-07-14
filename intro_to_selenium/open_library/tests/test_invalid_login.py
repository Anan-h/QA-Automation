import logging
import unittest
from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.logic.logic_utils import LogicUtils
from intro_to_selenium.open_library.logic.login_page import LoginPage
from intro_to_selenium.open_library.logic.main_page import MainPage


class TestInvalidLogIn(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        logging.info("launched the Open Library website ")
        MainPage(self.driver)

    def test_login_with_invalid_email(self):
        logging.info("testing login with invalid email address")
        logging.info("###########################################")
        MainPage(self.driver).click_on_log_in_button()
        LoginPage(self.driver)
        email = LogicUtils.generate_random_email_address()
        password = LogicUtils.generate_password()
        LoginPage(self.driver).login_flow(email, password)
        msg = LoginPage(self.driver).get_error_msg_text()
        self.assertTrue(LoginPage(self.driver).error_msg_is_visible())
        self.assertEqual(msg, self.config["invalid_login_msg"])

    def tearDown(self):
        self.driver.quit()
        logging.info("______________________________________________")
