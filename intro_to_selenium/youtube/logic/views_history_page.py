from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from intro_to_selenium.youtube.logic.base_app_page import BaseAppPage


class ViewsHistoryPage(BaseAppPage):
    ERROR_MSG = "//yt-formatted-string[@id='submessage']/span[1]"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._msg = self._driver.find_element(By.XPATH, self.ERROR_MSG)
        except NoSuchElementException as e:
            print("element not found", e)

    def error_msg_is_displayed(self):
        return self._msg.is_displayed()

    def get_error_msg_text(self):
        return self._msg.text
