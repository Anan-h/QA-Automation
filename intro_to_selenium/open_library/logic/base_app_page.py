import logging

from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.open_library.infra.base_page import BasePage


class BaseAppPage(BasePage):
    LOGO = "//img[@class='logo-icon']"
    MY_BOOKS_LINK = "//ul[@class='navigation-component']//a[@href='/account/books']"
    SEARCH_INPUT = "//input[@name='q']"
    BROWSE_BUTTON = "//ul[@class='navigation-component']//div[@class='browse-component header-dropdown']"
    SEARCH_FILTER = "//select[@aria-label='Search by']"
    SEARCH_ICON = "//input[@class='search-bar-submit']"
    RANDOM_BOOK_BUTTON = "//ul[@class='navigation-component']//a[@href='/random']"
    LOG_IN_BUTTON = "//a[@class='btn']"
    LOGGED_IN_IMG = "//img[@class='account__icon']"
    LOG_OUT_BUTTON = "//form[@name='hamburger-logout']/button"
    MY_PROFILE_LINK = "//a[@data-ol-link-track='Hamburger|MyProfile']"
    TRENDING_BUTTON = "//ul[@class='navigation-component']//a[@href='/trending']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._logo = self._driver.find_element(By.XPATH, self.LOGO)
            self._my_books_link = self._driver.find_element(By.XPATH, self.MY_BOOKS_LINK)
            self._search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
            self._browse_button = self._driver.find_element(By.XPATH, self.BROWSE_BUTTON)
            self._search_filter = self._driver.find_element(By.XPATH, self.SEARCH_FILTER)
            self._search_icon = self._driver.find_element(By.XPATH, self.SEARCH_ICON)
        except NoSuchElementException as e:
            logging.error(e)

    def navigate_to_home_page(self):
        """
        A function that navigates to the main page of the website
        :return:
        """
        self._logo.click()
        logging.info("navigated to home page")

    def navigate_to_my_books_page(self):
        """
        A function that navigates to my books page
        :return:
        """
        self._my_books_link.click()
        logging.info("navigated to my books page")

    def fill_search_input(self, text):
        """
         A function that gets a specific text and inserts it in the search bar
        :param text: input to search for
        :return:
        """
        self._search_input.send_keys(text)
        logging.info(f"searched for {text}")

    def click_on_browse_button(self):
        """
        A function that clicks on a button called browse
        :return:
        """
        self._browse_button.click()
        logging.info("clicked on browse button")

    def click_on_random_book(self):
        """
        A function that clicks on a button called Random Book located in the browse dropdown
        :return:
        """
        try:
            random_book = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.RANDOM_BOOK_BUTTON))
            )
            random_book.click()
            logging.info("clicked on random book button")
        except TimeoutException as e:
            logging.error(e)

    def click_on_log_in_button(self):
        """
        A function that clicks on the login button
        :return:
        """
        try:
            log_in = self._driver.find_element(By.XPATH, self.LOG_IN_BUTTON)
            log_in.click()
            logging.info("clicked on login button")
        except NoSuchElementException as e:
            logging.error(e)

    def click_on_profile_icon(self):
        """
        A function that clicks on the profile icon that is shown only after logged in
        :return:
        """
        try:
            profile = self._driver.find_element(By.XPATH, self.LOGGED_IN_IMG)
            profile.click()
            logging.info("clicked on profile icon")
        except NoSuchElementException as e:
            logging.error(e)

    def click_on_search_filter(self):
        """
        A function that clicks on the search filter button
        :return:
        """
        self._search_filter.click()
        logging.info("clicked on search filter")

    def click_on_search_icon(self):
        """
        A function that clicks on the search icon shaped as magnifying glass
        :return:
        """
        self._search_icon.click()
        logging.info("clicked on search icon")

    def search_flow(self, text):
        """
        this function performs a flow of all the actions needed to search for desired text
        :param text: desired input to search for
        :return:
        """
        self.fill_search_input(text)
        self.click_on_search_icon()

    def click_log_out_button(self):
        """
        this function clicks on the logout button that is shown only after logged in
        :return:
        """
        try:
            log_out = self._driver.find_element(By.XPATH, self.LOG_OUT_BUTTON)
            log_out.click()
            logging.info("clicked on logout button")
        except NoSuchElementException as e:
            logging.error(e)

    def log_out(self):
        """
        this function performs a flow of all the actions needed to log the user out
        :return:
        """
        self.click_on_profile_icon()
        self.click_log_out_button()

    def navigate_to_my_profile_page(self):
        """
        this function navigates to the user profile page
        :return:
        """
        self.click_on_profile_icon()
        try:
            my_profile = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.MY_PROFILE_LINK))
            )
            my_profile.click()
            logging.info("navigated to my profile page ")
        except TimeoutException as e:
            logging.error(e)

    def click_on_trending_button(self):
        """
        this function clicks on the trending button inside the browse dropdown
        :return:
        """
        try:
            trending = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.TRENDING_BUTTON))
            )
            trending.click()
            logging.info("clicked on trending button")
        except TimeoutException as e:
            logging.error(e)

    def select_author(self):
        """
        this function selects the author option from the search filter by value
        :return:
        """
        select = Select(self._search_filter)
        select.select_by_value('author')
        logging.info("selected the author option from search filter")
