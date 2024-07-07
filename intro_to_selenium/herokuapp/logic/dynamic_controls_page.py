from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.herokuapp.logic.base_app_page import BaseAppPage


class DynamicControlsPage(BaseAppPage):
    REMOVE_BTN = "//button[text()='Remove']"
    ENABLE_BTN = "//button[text()='Enable']"

    def __init__(self, driver):
        super().__init__(driver)
        self._remove=self._driver.find_element(By.XPATH,self.REMOVE_BTN)
        self._enable = self._driver.find_element(By.XPATH, self.ENABLE_BTN)

    def click_on_remove_btn(self):
        self._remove.click()

    def click_on_enable_btn(self):
        self._enable.click()

    def appearance_of_add_btn(self):
        self.click_on_remove_btn()
        add=WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Add']")))
        add.click()