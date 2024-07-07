from intro_to_selenium.para_bank.infra.config_provider import ConfigProvider
from intro_to_selenium.para_bank.infra.browser_wrapper import BrowserWrapper
import unittest

from intro_to_selenium.para_bank.logic.registered_page import RegisteredPage
from intro_to_selenium.para_bank.logic.main_page import MainPage
from intro_to_selenium.para_bank.logic.register_page import RegisterPage


class RegisterTest(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        self.driver.maximize_window()
        self.main_page = MainPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        self.main_page.click_on_register_link()
        reg = RegisterPage(self.driver)
        reg.register_flow(self.config["first_name"], self.config["last_name"], self.config["address"],
                          self.config["city"], self.config["state"], self.config["zip_code"], self.config["phone"],
                          self.config["ssn"], self.config["user_name"], self.config["password"], self.config["confirm"])
        reg = RegisteredPage(self.driver)
        self.assertTrue(reg.title_is_displayed())
        self.assertEqual(reg.get_title_text(), f"Welcome {self.config["user_name"]}")

    def test_register_random(self):
        self.main_page.click_on_register_link()
        register = RegisterPage(self.driver)
        register.register_flow_random()
        registered = RegisteredPage(self.driver)
        self.assertTrue(registered.title_is_displayed())


