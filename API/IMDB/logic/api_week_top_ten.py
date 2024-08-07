import logging
from requests import RequestException
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider


class APIWeekTopTen:
    END_POINT = "/getWeekTop10"

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file('C:\\Users\\ananh\\OneDrive\\Desktop\\QA Course\\Automation\\Automation_GIT\\API\\IMDB\\config.json')

    def get_week_top_ten(self):
        """
        this function sends a get request, including headers
        :return: list of the week's top ten
        """
        try:
            logging.info("getting the week's top ten")
            full_url = f"{self.config['base_url']}{self.END_POINT}"
            return self._request.get_request(full_url, headers=self.config['headers'])
        except RequestException as e:
            logging.error(e)
