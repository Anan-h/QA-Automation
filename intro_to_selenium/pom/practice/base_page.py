from intro_to_selenium.pom.infra.page import Page
from selenium.webdriver.common.by import By

class BasePage(Page):
    LEFT_MENU_BTN="//a[@id='menu-toggle']"
    FACEBOOK_BTN="//i[@class='fa fa-facebook fa-fw fa-3x']"
    TWITTER_BTN="//i[@class='fa fa-twitter fa-fw fa-3x']"
    DRIBBLE_BTN="//i[@class='fa fa-dribbble fa-fw fa-3x']"
    SCROLL_UPP_BTN="//i[@class='fa fa-chevron-up fa-fw fa-1x']"
    MAKE_APPOINTMENT_BTN = "//a[@id='btn-make-appointment']"
    def __init__(self, driver):
        super().__init__(driver)
        self._left_menu_btn=self._driver.find_elemnt(By.XPATH,self.LEFT_MENU_BTN)
        self._facebook_btn = self._driver.find_elemnt(By.XPATH, self.FACEBOOK_BTN)
        self._dribble_btn = self._driver.find_elemnt(By.XPATH, self.DRIBBLE_BTN)
        self._scroll_up_btn = self._driver.find_elemnt(By.XPATH, self.SCROLL_UPP_BTN)
        self._make_appointment_btn = self._driver.find_elemnt(By.XPATH, self.MAKE_APPOINTMENT_BTN)


