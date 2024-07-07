from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from intro_to_selenium.para_bank.infra.utils import Utils_G
from intro_to_selenium.para_bank.logic.base_app_page import BaseAppPage


class RegisterPage(BaseAppPage):
    FIRST_NAME_INPUT = "//input[@id='customer.firstName']"
    LAST_NAME_INPUT = "//input[@id='customer.lastName']"
    ADDRESS_INPUT = "//input[@id='customer.address.street']"
    CITY_INPUT = "//input[@id='customer.address.city']"
    STATE_INPUT = "//input[@id='customer.address.state']"
    ZIP_CODE_INPUT = "//input[@id='customer.address.zipCode']"
    PHONE_INPUT = "//input[@id='customer.phoneNumber']"
    SSN_INPUT = "//input[@id='customer.ssn']"
    USER_NAME_INPUT = "//input[@id='customer.username']"
    PASSWORD_INPUT = "//input[@id='customer.password']"
    CONFIRM_PASSWORD_INPUT = "//input[@id='repeatedPassword']"
    REGISTER_BUTTON = "//input[@value='Register']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._first_name_input = self._driver.find_element(By.XPATH, self.FIRST_NAME_INPUT)
            self._last_name_input = self._driver.find_element(By.XPATH, self.LAST_NAME_INPUT)
            self._address_input = self._driver.find_element(By.XPATH, self.ADDRESS_INPUT)
            self._city_input = self._driver.find_element(By.XPATH, self.CITY_INPUT)
            self._state_input = self._driver.find_element(By.XPATH, self.STATE_INPUT)
            self._zip_code_input = self._driver.find_element(By.XPATH, self.ZIP_CODE_INPUT)
            self._phone_input = self._driver.find_element(By.XPATH, self.PHONE_INPUT)
            self._ssn_input = self._driver.find_element(By.XPATH, self.SSN_INPUT)
            self._user_name_input = self._driver.find_element(By.XPATH, self.USER_NAME_INPUT)
            self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._confirm_input = self._driver.find_element(By.XPATH, self.CONFIRM_PASSWORD_INPUT)
            self._register_button = self._driver.find_element(By.XPATH, self.REGISTER_BUTTON)
        except NoSuchElementException as e:
            print("the element in not found", e)

    def fill_first_name_input(self, first_name):
        self._first_name_input.send_keys(first_name)

    def fill_last_name_input(self, last_name):
        self._last_name_input.send_keys(last_name)

    def fill_address_input(self, address):
        self._address_input.send_keys(address)

    def fill_city_input(self, city):
        self._city_input.send_keys(city)

    def fill_state_input(self, state):
        self._state_input.send_keys(state)

    def fill_zip_code_input(self, zip_code):
        self._zip_code_input.send_keys(zip_code)

    def fill_phone_input(self, phone):
        self._phone_input.send_keys(phone)

    def fill_ssn_input(self, ssn):
        self._ssn_input.send_keys(ssn)

    def fill_user_name_input(self, user):
        self._user_name_input.send_keys(user)

    def fill_password_input(self, ps):
        self._password_input.send_keys(ps)

    def fill_confirm_password_input(self, confirm):
        self._confirm_input.send_keys(confirm)

    def click_on_register_button(self):
        self._register_button.click()

    def register_flow(self, first, last, address, city, state, zip_code, phone, ssn, user, password, confirm):
        self.fill_first_name_input(first)
        self.fill_last_name_input(last)
        self.fill_address_input(address)
        self.fill_city_input(city)
        self.fill_state_input(state)
        self.fill_zip_code_input(zip_code)
        self.fill_phone_input(phone)
        self.fill_ssn_input(ssn)
        self.fill_user_name_input(user)
        self.fill_password_input(password)
        self.fill_confirm_password_input(confirm)
        self.click_on_register_button()

    def register_flow_random(self):
        password = Utils_G.generate_string(5)
        self.fill_first_name_input(Utils_G.generate_string(5))
        self.fill_last_name_input(Utils_G.generate_string(5))
        self.fill_address_input(Utils_G.generate_string(5))
        self.fill_city_input(Utils_G.generate_string(5))
        self.fill_state_input(Utils_G.generate_string(5))
        self.fill_zip_code_input(Utils_G.generate_string_of_numbers(7))
        self.fill_phone_input(Utils_G.generate_string_of_numbers(10))
        self.fill_ssn_input(Utils_G.generate_string_of_numbers(3))
        self.fill_user_name_input(Utils_G.generate_string(5))
        self.fill_password_input(password)
        self.fill_confirm_password_input(password)
        self.click_on_register_button()
