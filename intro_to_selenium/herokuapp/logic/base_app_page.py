from selenium.webdriver.common.by import By
from intro_to_selenium.herokuapp.infra.page import Page


class BaseAppPage(Page):
    RIGHT_IMG = "//img[@alt='Fork me on GitHub']"
    FOOTER = "//div[@id='page-footer']"
    SELENIUM_LINK="//a[text()='Elemental Selenium']"
    GIT_LINK="//a[@href='https://github.com/tourdedave/the-internet']"

    def __init__(self,driver):
        super().__init__(driver)
        self._img=self._driver.find_element(By.XPATH,self.RIGHT_IMG)
        self._footer=self._driver.find_element(By.XPATH,self.FOOTER)
        self._selenium = self._driver.find_element(By.XPATH, self.SELENIUM_LINK)
        self._git = self._driver.find_element(By.XPATH, self.GIT_LINK)

    def click_on_git_link(self):
        self._git.click()

    def click_on_selenium_link(self):
        self._selenium.click()