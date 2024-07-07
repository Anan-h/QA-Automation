from selenium.webdriver.common.by import By

from intro_to_selenium.herokuapp.logic.base_app_page import BaseAppPage


class CheckBoxes(BaseAppPage):
    FIRST_CHECK_BOX = "//*[@id='checkboxes']/input[1]"
    SECOND_CHECK_BOX = "//*[@id='checkboxes']/input[2]"

    def __init__(self, driver):
        super().__init__(driver)
        self._box1 = self._driver.find_element(By.XPATH, self.FIRST_CHECK_BOX)
        self._box2 = self._driver.find_element(By.XPATH, self.SECOND_CHECK_BOX)

    def select_first(self):
        self._box1.click()

    def select_second(self):
        self._box2.click()
