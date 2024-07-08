from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from intro_to_selenium.youtube.logic.base_app_page import BaseAppPage


class VideoPage(BaseAppPage):
    PAUSE_BUTTON = "//button[@title='Pause (k)']"
    PLAY_BUTTON = "//button[@title='Play (k)']"
    MUTE_BUTTON = "//button[@title='Mute (m)']"
    UNMUTE_BUTTON = "//button[@title='Unmute (m)']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._pause = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.PAUSE_BUTTON)))
            self._mute = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.MUTE_BUTTON)))
        except TimeoutException as e:
            print(e)

    def click_on_pause_btn(self):
        self._pause.click()

    def click_on_mute_btn(self):
        self._mute.click()

    def play_btn_is_displayed(self):
        try:
            play = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.PLAY_BUTTON)))
            return play.is_displayed()
        except TimeoutException as e:
            print(e)

    def unmute_btn_is_displayed(self):
        try:
            unmute = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.UNMUTE_BUTTON)))
            return unmute.is_displayed()
        except TimeoutException as e:
            print(e)

    def pause_btn_is_displayed(self):
        return self._pause.is_displayed()

    def mute_btn_is_displayed(self):
        self._mute.is_displayed()
