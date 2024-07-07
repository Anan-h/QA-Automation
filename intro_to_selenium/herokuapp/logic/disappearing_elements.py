from selenium.webdriver.common.by import By

from intro_to_selenium.herokuapp.logic.base_app_page import BaseAppPage


class DisappearingElements(BaseAppPage):
    HOME_BTN = "//a[text()='Home']"
    ABOUT_BTN = "//a[text()='About']"
    CONTACT_BTN = "//a[text()='Contact Us']"
    PORTFOLIO_BTN = "//a[text()='Portfolio']"

    def __init__(self, driver):
        super().__init__(driver)
        self._home = self._driver.find_element(By.XPATH, self.HOME_BTN)
        self._about = self._driver.find_element(By.XPATH, self.ABOUT_BTN)
        self._con = self._driver.find_element(By.XPATH, self.CONTACT_BTN)
        self._port = self._driver.find_element(By.XPATH, self.PORTFOLIO_BTN)
        self._gallery = None

    def gallery_button_appearance(self):
        self.refresh_page()
        self._gallery = self._driver.find_element(By.XPATH, "//a[text()='Gallery']")
        return self._gallery
