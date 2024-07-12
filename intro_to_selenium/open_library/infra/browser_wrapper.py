from selenium import webdriver
from intro_to_selenium.open_library.infra.config_provider import ConfigProvider


class BrowserWrapper:
    """
    This is the class that manage to open the web driver
    """

    def __init__(self):
        self.driver = None
        self.config = ConfigProvider.load_from_file('../config.json')
        print("Test Start")

    def get_driver(self, url):
        """
        This function load a website according to given url, on specific browser that
        is provided from outer file. and launches it on full screen
        :param url: the website link
        :return: opens the website on the desired browser
        """
        if self.config["browser"] == "Chrome":
            self._driver = webdriver.Chrome()
        elif self.config["browser"] == "FireFox":
            self._driver = webdriver.Firefox()
        elif self.config["browser"] == "Edge":
            self._driver = webdriver.Edge()

        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver
