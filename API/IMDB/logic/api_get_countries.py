import logging
from requests import RequestException
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider


class APIGetCountries:
    END_POINT = "/getCountries"

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file('C:\\Users\\ananh\\OneDrive\\Desktop\\QA Course\\Automation\\Automation_GIT\\API\\IMDB\\config.json')

    def get_all_countries(self):
        """
        this function sends a get request ,including headers
        :return: a list of all countries
        """
        try:
            logging.info("getting all countries")
            full_url = f"{self.config['base_url']}{self.END_POINT}"
            return self._request.get_request(full_url, headers=self.config["headers"])
        except RequestException as e:
            logging.error(e)
