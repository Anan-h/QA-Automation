from intro_to_selenium.open_library.infra.logging_setup import LoggingSetup


class BasePage:
    """
    This class is the basic web page for every website
    """

    def __init__(self, driver):
        self._driver = driver
