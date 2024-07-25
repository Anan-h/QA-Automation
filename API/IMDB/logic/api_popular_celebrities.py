import logging
from requests import RequestException
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider


class APIPopularCelebrities:
    END_POINT = "/getPopularCelebrities"

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file('C:\\Users\\ananh\\OneDrive\\Desktop\\QA Course\\Automation\\Automation_GIT\\API\\IMDB\\config.json')

    def get_all_popular_celebrities(self):
        """
        this function sends a get request, including headers
        :return: list of all popular celebrities
        """
        try:
            logging.info("getting all popular celebrities")
            full_url = f"{self.config['base_url']}{self.END_POINT}"
            return self._request.get_request(full_url, headers=self.config["headers"])
        except RequestException as e:
            logging.error(e)
