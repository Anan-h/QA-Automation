from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from intro_to_selenium.open_library.infra.base_page import BasePage


class BaseAppPage(BasePage):
    LOGO = "//img[@class='logo-icon']"
    MY_BOOKS_LINK = "//ul[@class='navigation-component']//a[@href='/account/books']"
    SEARCH_INPUT = "//input[@name='q']"
    MENU = "//img[@class='hamburger__icon']"
    BROWSE_DROPDOWN = "//ul[@class='navigation-component']//div[@class='browse-component header-dropdown']"
    SEARCH_BY_SELECTOR = "//select[@aria-label='Search by']"
    SEARCH_ICON = "//input[@class='search-bar-submit']"
    RANDOM_BOOK_BUTTON = "//ul[@class='navigation-component']//a[@href='/random']"
    LOG_IN_BUTTON = "//a[@class='btn']"
    LOGGED_IN_IMG = "//img[@class='account__icon']"
    LOG_OUT_BUTTON = "//form[@name='hamburger-logout']/button"
    SETTINGS_LINK = "//a[@data-ol-link-track='Hamburger|MySettings']"
    MY_PROFILE_LINK = "//a[@data-ol-link-track='Hamburger|MyProfile']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._logo = self._driver.find_element(By.XPATH, self.LOGO)
            self._my_books_link = self._driver.find_element(By.XPATH, self.MY_BOOKS_LINK)
            self._search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
            self._menu = self._driver.find_element(By.XPATH, self.MENU)
            self._browse_drop_down = self._driver.find_element(By.XPATH, self.BROWSE_DROPDOWN)
            self._search_by_selector = self._driver.find_element(By.XPATH, self.SEARCH_BY_SELECTOR)
            self._search_icon = self._driver.find_element(By.XPATH, self.SEARCH_ICON)
        except NoSuchElementException as e:
            print(e)

    def navigate_to_home_page(self):
        self._logo.click()

    def navigate_to_my_books_page(self):
        self._my_books_link.click()

    def fill_search_input(self, text):
        self._search_input.send_keys(text)

    def click_on_menu_icon(self):
        self._menu.click()

    def click_on_browse_button(self):
        self._browse_drop_down.click()

    def click_on_random_book(self):
        self.click_on_browse_button()
        try:
            random_book = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.RANDOM_BOOK_BUTTON))
            )
            random_book.click()
        except NoSuchElementException as e:
            print(e)

    def click_on_log_in_button(self):
        try:
            log_in = self._driver.find_element(By.XPATH, self.LOG_IN_BUTTON)
            log_in.click()
        except NoSuchElementException as e:
            print(e)

    def click_on_profile_icon(self):
        try:
            profile = self._driver.find_element(By.XPATH, self.LOGGED_IN_IMG)
            profile.click()
        except NoSuchElementException as e:
            print(e)

    def click_on_search_by(self):
        self._search_by_selector.click()

    def click_on_search_icon(self):
        self._search_icon.click()

    def search_flow(self, text):
        self.fill_search_input(text)
        self.click_on_search_icon()

    def click_log_out_button(self):
        try:
            log_out = self._driver.find_element(By.XPATH, self.LOG_OUT_BUTTON)
            log_out.click()
        except NoSuchElementException as e:
            print(e)

    def log_out(self):
        self.click_on_profile_icon()
        self.click_log_out_button()

    def navigate_to_settings_page(self):
        self.click_on_profile_icon()
        try:
            settings_link = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.SETTINGS_LINK))
            )
            settings_link.click()
        except NoSuchElementException as e:
            print(e)

    def navigate_to_my_profile_page(self):
        self.click_on_profile_icon()
        try:
            my_profile = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.MY_PROFILE_LINK))
            )
            my_profile.click()
        except NoSuchElementException as e:
            print(e)


