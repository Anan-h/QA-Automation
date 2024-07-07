from selenium.webdriver.common.by import By
from intro_to_selenium.herokuapp.logic.base_app_page import BaseAppPage


class AddRemoveElements(BaseAppPage):
    ADD_BTN = "//button[text()='Add Element']"

    def __init__(self, driver):
        super().__init__(driver)
        self._add_btn = self._driver.find_element(By.XPATH, self.ADD_BTN)
        self._buttons = []

    def click_on_add_btn(self):
        self._add_btn.click()
        self._buttons = self._driver.find_elements(By.XPATH, "//button[@class='added-manually']")

    def click_on_delete_button(self, index=0):
        for i in range(index+1):
            self.click_on_add_btn()
        self._buttons[index].click()
