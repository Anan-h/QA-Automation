from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class ProfilePage(BaseAppPage):
    EDIT_BUTTON = "//a[@title='Edit this page']"
    PROFILE_NAME = "//div[@id='contentHead']/h1"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._edit_button = self._driver.find_element(By.XPATH, self.EDIT_BUTTON)
            self._name = self._driver.find_element(By.XPATH, self.PROFILE_NAME)
        except NoSuchElementException as e:
            print(e)

    def click_on_edit_button(self):
        """
        This function clicks on the edit button
        :return:
        """
        self._edit_button.click()

    def get_profile_name(self):
        """
        This function extracts the name of the account
        :return:the name
        """
        return self._name.text
