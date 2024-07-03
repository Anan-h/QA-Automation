from intro_to_selenium.pom.practice.base_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):

    USERNAME_INPUT="//input[@id='txt-username']"
    PASSWORD_INPUT="//input[@id='txt-password']"
    LOGIN_BTN="//button[@id='btn-login']"

    def __init__(self,driver):
        super().__init__(driver)
        self._user_name_input=self._driver.find_elemnt(By.XPATH,self.USERNAME_INPUT)
        self._password_input = self._driver.find_elemnt(By.XPATH, self.PASSWORD_INPUT)
        self._login_btn = self._driver.find_elemnt(By.XPATH, self.LOGIN_BTN)

    def fill_user_name(self,user_name):
        self._user_name_input.send_keys(user_name)

    def fill_password(self, password):
        self._password_input.send_keys(password)


    def click_on_login_btn(self):
        self._login_btn.click()

    def login_flow(self,user_name,password):
        self.fill_user_name(user_name)
        self.fill_password(password)
        self.click_on_login_btn()
