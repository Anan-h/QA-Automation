import unittest

from intro_to_selenium.youtube.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.youtube.infra.config_provider import ConfigProvider
from intro_to_selenium.youtube.logic.base_app_page import BaseAppPage
from intro_to_selenium.youtube.logic.result_page import ResultPage
from intro_to_selenium.youtube.logic.video_page import VideoPage


class VideoPageTest(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        self.base = BaseAppPage(self.driver)
        self.base.search_flow(self.config["search"])
        self.res = ResultPage(self.driver)
        self.res.click_on_video_link_by_index(self.config["search"])

    def tearDown(self):
        self.driver.quit()

    def test_pause_btn_functionality(self):
        video = VideoPage(self.driver)
        video.click_on_pause_btn()
        self.assertTrue(video.play_btn_is_displayed())

    def test_mute_btn_functionality(self):
        video = VideoPage(self.driver)
        video.click_on_mute_btn()
        self.assertTrue(video.unmute_btn_is_displayed())


