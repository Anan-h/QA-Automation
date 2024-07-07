from intro_to_selenium.pom.logic.sauce_lab_base_page import SauceLabBasePage
from selenium.webdriver.common.by import By


class SauceLabCartPage(SauceLabBasePage):
    CONTINUE_SHOPPING_BTN = "//button[@id='continue-shopping']"
    CHECKOUT_BTN = "//button[@id='checkout']"
    ITEM_SECTION_IN_CART = "//div[@class='cart_item']"
    REMOVE_SHIRT_BTN = "//button[@id='remove-sauce-labs-bolt-t-shirt']"
    REMOVE_FLEECE_BTN = "//button[@id='remove-sauce-labs-fleece-jacket']"
    REMOVE_BIKE_LIGHT_BTN = "//button[@id='remove-sauce-labs-bike-light']"
    REMOVE_BAG_BTN = "//button[@id='remove-sauce-labs-backpack']"
    REMOVE_ONESIE_BTN = "//button[@id='remove-sauce-labs-onesie']"
    REMOVE_RED_SHIRT_BTN = "//button[@id='remove-test.allthethings()-t-shirt-(red)']"

    def __init__(self, driver):
        super().__init__(driver)
        self._continue_btn = self._driver.find_element(By.XPATH, self.CONTINUE_SHOPPING_BTN)
        self._checkout_btn = self._driver.find_element(By.XPATH, self.CHECKOUT_BTN)
        # self._items = self._driver.find_elements(By.XPATH, self.ITEM_SECTION_IN_CART)
        self._remove_shirt_btn = self._driver.find_element(By.XPATH, self.REMOVE_SHIRT_BTN)
        # self._remove_fleece_btn = self._driver.find_element(By.XPATH, self.REMOVE_FLEECE_BTN)
        # self._remove_bike_light_btn = self._driver.find_element(By.XPATH, self.REMOVE_BIKE_LIGHT_BTN)
        self._remove_bag_btn = self._driver.find_element(By.XPATH, self.REMOVE_BAG_BTN)
        # self._remove_onesie_btn = self._driver.find_element(By.XPATH, self.REMOVE_ONESIE_BTN)
        # self._remove_red_shirt_btn = self._driver.find_element(By.XPATH, self.REMOVE_RED_SHIRT_BTN)

    def click_on_continue_shopping(self):
        self._continue_btn.click()

    def click_on_checkout(self):
        self._checkout_btn.click()

    def get_count_of_items(self):
        items = self._driver.find_elements(By.XPATH, "//div[@class='cart_item']")
        return len(items)

    def click_on_remove_shirt_btn(self):
        self._remove_shirt_btn.click()

    # def click_on_remove_fleece_btn(self):
    #     self._remove_fleece_btn.click()

    # def click_on_remove_bike_light_btn(self):
    #     self._remove_bike_light_btn.click()
    #
    def click_on_remove_bag_btn(self):
        self._remove_bag_btn.click()

    # def click_on_remove_onesie_btn(self):
    #     self._remove_onesie_btn.click()
    #
    # def click_on_remove_red_shirt_btn(self):
    #     self._remove_red_shirt_btn.click()
