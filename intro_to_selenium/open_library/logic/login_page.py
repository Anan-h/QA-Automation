import logging

from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class LoginPage(BaseAppPage):
    EMAIL_INPUT = "//input[@id='username']"
    PASSWORD_INPUT = "//input[@id='password']"
    LOG_IN_BUTTON = "//button[@name='login']"
    INVALID_EMAIL_MSG = "//div[@class='note']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
            self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._login_button = self._driver.find_element(By.XPATH, self.LOG_IN_BUTTON)
        except NoSuchElementException as e:
            logging.error(e)

    def fill_email_input(self, email):
        """
        This function insert a given email address to the email input bar
        :param email: email address as string
        :return:
        """
        self._email_input.send_keys(email)
        logging.info(f"{email} inserted in email input bar")

    def fill_password_input(self, password):
        """
        This function insert a given password to the password input bar
        :param password: password as string
        :return:
        """
        self._password_input.send_keys(password)
        logging.info(f"{password} inserted in password input bar")

    def click_on_login_button(self):
        """
        This function clicks on the login button
        :return:
        """
        self._login_button.click()
        logging.info("clicked on login button")

    def login_flow(self, email, password):
        """
        This function performs the whole process of the login
        :param email:email address as string
        :param password: password as string
        :return:
        """
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.click_on_login_button()

    def error_msg_is_visible(self):
        """
        This function checks if the error message is shown after trying to log in via invalid email address
        :return: True/False
        """
        try:
            msg = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.INVALID_EMAIL_MSG))
            )
            if msg.is_displayed():
                logging.info("error message was displayed ")
            else:
                logging.warning("error message was not displayed")
            return msg.is_displayed()
        except TimeoutException as e:
            logging.error(e)

    def get_error_msg_text(self):
        """
        This function extracts the text of the error message
        :return: the content of the message
        """
        try:
            msg = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.INVALID_EMAIL_MSG))
            )
            logging.info(f"the message content is:{msg.text}")
            return msg.text
        except TimeoutException as e:
            logging.error(e)
