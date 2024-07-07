from intro_to_selenium.pom.infra.page import Page
from selenium.webdriver.common.by import By


class SauceLabBasePage(Page):
    LEFT_MENU = "//button[@id='react-burger-menu-btn']"
    CART_ICON = "//a[@class='shopping_cart_link']"
    APP_LOGO = "//div[@class='app_logo']"
    TWITTER_LOGO = "//a[@data-test='social-twitter']"
    FACEBOOK_LOGO = "//a[@data-test='social-facebook']"
    LINKEDIN_LOGO = "//a[@data-test='social-linkedin']"
    CART_BADGE = "//span[@class='shopping_cart_badge']"

    def __init__(self, driver):
        super().__init__(driver)
        self._left_menu_btn = self._driver.find_element(By.XPATH, self.LEFT_MENU)
        self._cart = self._driver.find_element(By.XPATH, self.CART_ICON)
        self._app_logo = self._driver.find_element(By.XPATH, self.APP_LOGO)
        self._twitter_logo = self._driver.find_element(By.XPATH, self.TWITTER_LOGO)
        self._facebook_logo = self._driver.find_element(By.XPATH, self.FACEBOOK_LOGO)
        self._linkedin_logo = self._driver.find_element(By.XPATH, self.LINKEDIN_LOGO)


    def get_title(self):
        return self._app_logo.text

    def click_on_menu(self):
        self._left_menu_btn.click()

    def click_on_cart_icon(self):
        self._cart.click()

    def click_on_twitter_icon(self):
        self._twitter_logo.click()

    def click_on_facebook_icon(self):
        self._facebook_logo.click()

    def click_on_linkedin_icon(self):
        self._linkedin_logo.click()


