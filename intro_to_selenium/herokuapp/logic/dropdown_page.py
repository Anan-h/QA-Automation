from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from intro_to_selenium.herokuapp.logic.base_app_page import BaseAppPage


class DropDownPage(BaseAppPage):
    DROP_DOWN = "//select[@id='dropdown']"
    FIRST = "//option[@value='1']"
    SECOND = "//option[@value='2']"

    def __init__(self, driver):
        super().__init__(driver)
        self._dd = self._driver.find_element(By.XPATH, self.DROP_DOWN)
        self._first_option=self._driver.find_element(By.XPATH,self.FIRST)
        self._second_option = self._driver.find_element(By.XPATH, self.SECOND)

    def select_from_dropdown(self):
        select = Select(self._dd)
        select.select_by_value('1')
