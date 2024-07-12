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
        main_page = MainPage(self.driver)
        main_page.click_on_log_in_button()
        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config["email"], self.config["password"])
        self.my_books_page = MyBooksPage(self.driver)

    def test_editing_display_name(self):
        name = Utils.generate_string_of_letters(4)
        self.my_books_page.navigate_to_my_profile_page()
        my_profile = ProfilePage(self.driver)
        my_profile.click_on_edit_button()
        editing = ProfileEditingPage(self.driver)
        editing.edit_name_flow(name)
        self.new_profile = ProfilePage(self.driver)
        new_name = self.new_profile.get_profile_name()
        self.assertEqual(name, new_name)

    def tearDown(self):
        #undo the changing of the name
        self.new_profile.click_on_edit_button()
        ProfileEditingPage(self.driver).edit_name_flow(self.config["name"])
        ProfilePage(self.driver).log_out()
        self.driver.quit()
