import unittest

from intro_to_selenium.youtube.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.youtube.infra.config_provider import ConfigProvider
from intro_to_selenium.youtube.logic.base_app_page import BaseAppPage
from intro_to_selenium.youtube.logic.result_page import ResultPage


class SearchFunctionTest(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["url"])
        self.base = BaseAppPage(self.driver)
        self.base.search_flow(self.config["search"])
        self.res = ResultPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search_function(self):
        results = self.res.get_matching_results(self.config["search"])
        self.assertGreater(len(results), 0)
        self.assertEqual(self.res.get_current_url(),
                         'https://www.youtube.com/results?search_query=Python+for+beginners')
