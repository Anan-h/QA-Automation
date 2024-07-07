import random

from selenium.webdriver.common.by import By
from intro_to_selenium.herokuapp.logic.base_app_page import BaseAppPage


class ChallengingDom(BaseAppPage):
    BLUE_BTN = "//a[@class='button']"
    RED_BTN = "//a[@class='button alert']"
    GREEN_BTN = "//a[@class='button success']"
    CANVAS = "//canvas[@id='canvas']"
    EDIT_BTNS = "//td//a[@href='#edit']"
    DELETE_BTNS = "//td//a[@href='#delete']"

    def __init__(self, driver):
        super().__init__(driver)
        self._blue = self._driver.find_element(By.XPATH, self.BLUE_BTN)
        self._red = self._driver.find_element(By.XPATH, self.RED_BTN)
        self._green = self._driver.find_element(By.XPATH, self.GREEN_BTN)
        self._canvas = self._driver.find_element(By.XPATH, self.CANVAS)
        self._edit = self._driver.find_elements(By.XPATH, self.EDIT_BTNS)
        self._delete = self._driver.find_elements(By.XPATH, self.DELETE_BTNS)

    def click_on_blue_btn(self):
        self._blue.click()

    def click_on_red_btn(self):
        self._red.click()

    def click_on_green_btn(self):
        self._green.click()

    def click_on_one_edit_btn(self):
        self._edit[random.randint(0, 9)].click()

    def click_on_one_delete_btn(self):
        self._delete[random.randint(0, 9)].click()
