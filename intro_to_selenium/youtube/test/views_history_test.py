import unittest

from intro_to_selenium.youtube.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.youtube.infra.config_provider import ConfigProvider
from intro_to_selenium.youtube.logic.base_app_page import BaseAppPage
from intro_to_selenium.youtube.logic.views_history_page import ViewsHistoryPage


class ViewsHistoryTest(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["url"])
        self.base = BaseAppPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_deleting_views_history_signed_out(self):
        self.base.click_on_history()
        history = ViewsHistoryPage(self.driver)
        msg_display = history.error_msg_is_displayed()
        self.assertTrue(msg_display)
        self.assertEqual(history.get_error_msg_text(), "Watch history isn't viewable when signed out.")
