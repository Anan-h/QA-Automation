import unittest

from intro_to_selenium.youtube.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.youtube.infra.config_provider import ConfigProvider
from intro_to_selenium.youtube.infra.utils import Utils
from intro_to_selenium.youtube.logic.base_app_page import BaseAppPage
from intro_to_selenium.youtube.logic.logging_in_page import LoggingInPage


class LogInTest(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["url"])
        self.main = BaseAppPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_invalid_phone_number_login(self):
        self.main.click_on_sign_in_button()
        login = LoggingInPage(self.driver)
        login.login_flow(Utils.generate_string_of_numbers(10))
        self.assertTrue(login.error_is_displayed())
        self.assertEqual(login.get_error_text(), "Enter a valid email or phone number")
