from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from intro_to_selenium.youtube.logic.base_app_page import BaseAppPage


class ResultPage(BaseAppPage):
    PATH = "//yt-formatted-string[contains(text(),'')]"

    def __init__(self, driver):
        super().__init__(driver)
        self._res = []

    def get_matching_results(self, text):
        try:
            self._res = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_any_elements_located((By.XPATH, f"//yt-formatted-string[contains(text(),'{text}')]")))
            return self._res
        except TimeoutException as e:
            print(e)

    def click_on_video_link_by_index(self, text, index=0):
        results = self.get_matching_results(text)
        try:
            results[index].click()
        except IndexError as e:
            print(e)
