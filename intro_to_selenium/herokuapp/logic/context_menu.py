from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

from intro_to_selenium.herokuapp.logic.base_app_page import BaseAppPage


class ContextMenu(BaseAppPage):
    BOX = "//div[@id='hot-spot']"

    def __init__(self, driver):
        super().__init__(driver)
        self._hot_spot = self._driver.find_element(By.XPATH,self.BOX)

    def right_click_on_hot_spot(self):
        action=AC(self._driver)
        action.context_click(self._hot_spot).perform()
