from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class MyBooksPage(BaseAppPage):
    USER_NAME_TITLE = "//h2[@class='account-username']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._user_name = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.USER_NAME_TITLE)))

        except NoSuchElementException as e:
            print(e)

    def get_user_name(self):
        """
        This function extracts the display name of the account
        :return: name of the user as string
        """
        return self._user_name.text
