from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC

from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class MyBooksPage(BaseAppPage):
    MY_NOTES_LINK = "//div[@class='mybooks-menu']//a[@data-ol-link-track='MyBooksSidebar|MyNotes']"
    USER_NAME_TITLE = "//h2[@class='account-username']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._my_notes = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.MY_NOTES_LINK)))
            self._user_name = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.USER_NAME_TITLE)))

        except NoSuchElementException as e:
            print(e)

    def navigate_to_my_notes_page(self):
        self._my_notes.click()

    def get_user_name(self):
        return self._user_name.text
