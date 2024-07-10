from intro_to_selenium.open_library.infra.base_page import BasePage


class BaseAppPage(BasePage):

    LOGO="//img[@class='logo-icon']"
    MY_BOOKS_LINK="//ul[@class='navigation-component']//a[@href='/account/books']"
    SEARCH_INPUT="//input[@name='q']"
    MENU="//img[@class='hamburger__icon']"
