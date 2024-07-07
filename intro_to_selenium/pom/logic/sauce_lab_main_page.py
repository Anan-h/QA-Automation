from intro_to_selenium.pom.logic.sauce_lab_base_page import SauceLabBasePage
from selenium.webdriver.common.by import By


class SauceLabMainPage(SauceLabBasePage):
    BAG_ADD_TO_CART_BTN = "//button[@id='add-to-cart-sauce-labs-backpack']"
    BIKE_LIGHT_ADD_TO_CART_BTN = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    SHIRT_ADD_TO_CART_BTN = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    FLEECE_ADD_TO_CART_BTN = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    ONESIE_ADD_TO_CART_BTN = "//button[@id='add-to-cart-sauce-labs-onesie']"
    RED_SHIRT_ADD_TO_CART_BTN = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"

    def __init__(self, driver):
        super().__init__(driver)
        self._bag_adding = self._driver.find_element(By.XPATH, self.BAG_ADD_TO_CART_BTN)
        self._bike_light_adding = self._driver.find_element(By.XPATH, self.BIKE_LIGHT_ADD_TO_CART_BTN)
        self._shirt_adding = self._driver.find_element(By.XPATH, self.SHIRT_ADD_TO_CART_BTN)
        self._fleece_adding = self._driver.find_element(By.XPATH, self.FLEECE_ADD_TO_CART_BTN)
        self._onesie_adding = self._driver.find_element(By.XPATH, self.ONESIE_ADD_TO_CART_BTN)
        self._red_shirt_adding = self._driver.find_element(By.XPATH, self.RED_SHIRT_ADD_TO_CART_BTN)

    def add_bike_light_to_cart(self):
        self._bike_light_adding.click()

    def add_shirt_to_cart(self):
        self._shirt_adding.click()

    def add_bag_to_cart(self):
        self._bag_adding.click()

    def add_fleece_to_cart(self):
        self._fleece_adding.click()

    def add_onesie_to_cart(self):
        self._onesie_adding.click()

    def add_red_shirt_to_cart(self):
        self._red_shirt_adding.click()

    def adding_two_items_to_cart(self):
        self.add_bag_to_cart()
        self.add_shirt_to_cart()

    def adding_three_items_to_cart(self):
        self.add_bag_to_cart()
        self.add_shirt_to_cart()
        self.add_bike_light_to_cart()

    def adding_all_items_to_cart(self):
        self.add_shirt_to_cart()
        self.add_fleece_to_cart()
        self.add_onesie_to_cart()
        self.add_red_shirt_to_cart()
        self.add_bike_light_to_cart()
        self.add_bag_to_cart()
