import unittest
from selenium import webdriver


from intro_to_selenium.pom.logic.sauce_lab_cart_page import SauceLabCartPage
from intro_to_selenium.pom.logic.sauce_lab_login_page import SauceLabLoginPage
from intro_to_selenium.pom.logic.sauce_lab_main_page import SauceLabMainPage


class SauceLabsTest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

    def test_login_success(self):
        driver = self.driver
        login = SauceLabLoginPage(driver)
        login.login_flow('standard_user', 'secret_sauce')
        url = driver.current_url
        self.assertEqual(url, 'https://www.saucedemo.com/inventory.html')

    def test_adding_two_items_to_cart(self):
        driver = self.driver
        login = SauceLabLoginPage(driver)
        login.login_flow('standard_user', 'secret_sauce')
        main = SauceLabMainPage(driver)
        main.adding_two_items_to_cart()
        main.click_on_cart_icon()
        cart = SauceLabCartPage(driver)
        cnt = cart.get_count_of_items()
        self.assertEqual(cnt, 2)

    def test_adding_three_items_to_cart(self):
        driver = self.driver
        login = SauceLabLoginPage(driver)
        login.login_flow('standard_user', 'secret_sauce')
        main = SauceLabMainPage(driver)
        main.adding_three_items_to_cart()
        main.click_on_cart_icon()
        cart = SauceLabCartPage(driver)
        cart.click_on_remove_bag_btn()
        cnt = cart.get_count_of_items()
        self.assertEqual(cnt, 2)
