from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from intro_to_selenium.open_library.infra.base_page import BasePage


class BaseAppPage(BasePage):

    LOGO="//img[@class='logo-icon']"
    MY_BOOKS_LINK="//ul[@class='navigation-component']//a[@href='/account/books']"
    SEARCH_INPUT="//input[@name='q']"
    MENU="//img[@class='hamburger__icon']"
    BROWSE_DROPDOWN="//ul[@class='navigation-component']//div[@class='browse-component header-dropdown']"
    SEARCH_BY_SELECTOR="//select[@aria-label='Search by']"
    SEARCH_ICON="//input[@class='search-bar-submit']"
    RANDOM_BOOK_BUTTON="//ul[@class='navigation-component']//a[@href='/random']"
    REPORT_PROBLEM_LINK="//a[text()='Report A Problem']"
    LOG_IN_BUTTON="//a[@class='btn']"

    def __init__(self,driver):
        super().__init__(driver)
        try:
            self._logo=self._driver.find_element(By.XPATH,self.LOGO)
            self._my_books_link=self._driver.find_element(By.XPATH,self.MY_BOOKS_LINK)
            self._search_input=self._driver.find_element(By.XPATH,self.SEARCH_INPUT)
            self._menu=self._driver.find_element(By.XPATH,self.MENU)
            self._browse_drop_down=self._driver.find_element(By.XPATH,self.BROWSE_DROPDOWN)
            self._search_by_selector=self._driver.find_element(By.XPATH,self.SEARCH_BY_SELECTOR)
            self._search_icon=self._driver.find_element(By.XPATH,self.SEARCH_ICON)
        except NoSuchElementException as e:
            print(e)
