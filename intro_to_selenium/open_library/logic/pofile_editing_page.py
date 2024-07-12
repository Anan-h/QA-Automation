from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class ProfileEditingPage(BaseAppPage):
    DISPLAY_NAME_INPUT = "//input[@id='title']"
    SAVE_BUTTON = "//button[@title='Save']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._name_input = self._driver.find_element(By.XPATH, self.DISPLAY_NAME_INPUT)
            self._save_button = self._driver.find_element(By.XPATH, self.SAVE_BUTTON)
        except NoSuchElementException as e:
            print(e)

    def replace_display_name(self, new_name):
        """
        This function clears the existing name on the name input and insert the new name instead
        :param new_name:the desired name to change for
        :return:
        """
        self._name_input.clear()
        self._name_input.send_keys(new_name)

    def click_on_save_button(self):
        """
        This function clicks on the save button after changing the name
        :return:
        """
        self._save_button.click()

    def edit_name_flow(self, new_name):
        """
        This function performs the whole process of the name editing
        :param new_name: the desired name to change for
        :return:
        """
        self.replace_display_name(new_name)
        self.click_on_save_button()
