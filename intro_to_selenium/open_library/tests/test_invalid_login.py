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
        self.main_page = MainPage(self.driver)

    def test_login_with_invalid_email(self):
        #Arrange
        self.main_page.click_on_log_in_button()
        login_page = LoginPage(self.driver)
        email = LogicUtils.generate_random_email_address()
        password = LogicUtils.generate_password()
        #Act
        login_page.login_flow(email, password)
        #Assert
        msg = login_page.get_error_msg_text()
        self.assertTrue(login_page.error_msg_is_visible())
        self.assertEqual(msg, self.config["invalid_login_msg"])

    def tearDown(self):
        self.driver.quit()
