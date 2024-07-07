from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

from intro_to_selenium.herokuapp.logic.base_app_page import BaseAppPage


class DragAndDrop(BaseAppPage):
    COLUMN_A = "//div[@id='column-a']"
    COLUMN_B = "//div[@id='column-b']"

    def __init__(self, driver):
        super().__init__(driver)
        self._a = self._driver.find_element(By.XPATH, self.COLUMN_A)
        self._b = self._driver.find_element(By.XPATH, self.COLUMN_B)

    def drag_a_to_b(self):
        action = AC(self._driver)
        action.drag_and_drop(self._a, self._b).perform()
