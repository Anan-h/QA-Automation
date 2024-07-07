from selenium.webdriver.chrome.webdriver import WebDriver


class Page:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def refresh_page(self):
        self._driver.refresh()

    def get_title(self):
        return self._driver.title

    def get_current_url(self):
        return self._driver.current_url
