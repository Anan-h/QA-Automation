import unittest
from selenium import webdriver

from intro_to_selenium.pom.logic.sauce_lab_base_page import SauceLabBasePage
from intro_to_selenium.pom.logic.sauce_lab_login_page import SauceLabLoginPage
from intro_to_selenium.pom.logic.sauce_lab_main_page import SauceLabMainPage


class SauceLabsTest(unittest.TestCase):

    def test_login_success(self):
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')
        login = SauceLabLoginPage(driver)
        login.login_flow('standard_user', 'secret_sauce')
        url = driver.current_url
        self.assertEqual(url, 'https://www.saucedemo.com/inventory.html')

    def test_adding_two_items_to_cart(self):
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')
        login = SauceLabLoginPage(driver)
        login.login_flow('standard_user', 'secret_sauce')
        main = SauceLabMainPage(driver)
        main.adding_two_items_to_cart()
        cnt = main.get_items_count_in_cart()
        self.assertEqual(cnt, '2')
