import logging
import unittest
from intro_to_selenium.open_library.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider
from intro_to_selenium.open_library.infra.utils import Utils
from intro_to_selenium.open_library.logic.login_page import LoginPage
from intro_to_selenium.open_library.logic.main_page import MainPage
from intro_to_selenium.open_library.logic.my_books_page import MyBooksPage
from intro_to_selenium.open_library.logic.pofile_editing_page import ProfileEditingPage
from intro_to_selenium.open_library.logic.profile_page import ProfilePage


class TestEditName(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        logging.info("launched the Open Library website ")
        MainPage(self.driver).click_on_log_in_button()
        LoginPage(self.driver).login_flow(self.config["email"], self.config["password"])
        MyBooksPage(self.driver)

    def test_editing_display_name(self):
        logging.info("testing the editing of the display name ")
        logging.info("###########################################")
        name = Utils.generate_string_of_letters(4)
        MyBooksPage(self.driver).navigate_to_my_profile_page()
        ProfilePage(self.driver).click_on_edit_button()
        ProfileEditingPage(self.driver).edit_name_flow(name)
        new_name = ProfilePage(self.driver).get_profile_name()
        self.assertEqual(name, new_name)

    def tearDown(self):
        ProfilePage(self.driver).click_on_edit_button()
        ProfileEditingPage(self.driver).edit_name_flow(self.config["name"])
        ProfilePage(self.driver).log_out()
        self.driver.quit()
        logging.info("______________________________________________")
