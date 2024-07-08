from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from intro_to_selenium.youtube.infra.base_page import BasePage


class BaseAppPage(BasePage):
    MENU_BUTTON = "//button[@aria-label='Guide']/yt-icon[@icon='yt-icons:menu']"
    HISTORY_BUTTON = "//ytd-guide-entry-renderer//a[@title='History']"
    YOUTUBE_LOGO = "//ytd-topbar-logo-renderer[@id='logo']//div//yt-icon[@id='logo-icon']"
    SIGN_IN_BUTTON = "//ytd-button-renderer[@class='style-scope ytd-masthead']//a"
    SEARCH_INPUT = "//input[@id='search']"
    SEARCH_ICON = "//button[@id='search-icon-legacy']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._menu_btn = self._driver.find_element(By.XPATH, self.MENU_BUTTON)
            self._logo = self._driver.find_element(By.XPATH, self.YOUTUBE_LOGO)
            self._sign_in_btn = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
            self._search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
            self._search_icon = self._driver.find_element(By.XPATH, self.SEARCH_ICON)
        except NoSuchElementException as e:
            print("element not found ", e)

    def click_on_menu(self):
        self._menu_btn.click()

    def click_on_history(self):
        self.click_on_menu()
        self._driver.implicitly_wait(2)
        history = self._driver.find_element(By.XPATH,self.HISTORY_BUTTON)
        history.click()

    def click_on_youtube_logo(self):
        self._logo.click()

    def fill_search_input(self, text):
        self._search_input.click()
        self._search_input.send_keys(text)

    def click_on_search_icon(self):
        self._search_icon.click()

    def click_on_sign_in_button(self):
        self._sign_in_btn.click()

    def search_flow(self, text):
        self.click_on_search_icon()
        self.fill_search_input(text)
        self.click_on_search_icon()
