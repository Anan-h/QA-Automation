import logging
from requests import RequestException
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.infra.response_wrapper import ResponseWrapper


class APISearchImdb:
    END_POINT = "/searchIMDB?query="

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file('../config.json')

    def get_search_imdb_for_text(self, text):
        """
        this function sends a GET request ,including headers and text as param
        :param text: the search input
        :return:list of results for the search input
        """
        try:
            full_url = f"{self.config['base_url']}{self.END_POINT}{text}"
            logging.info(f"searching for: {text}")
            response = self._request.get_request(full_url, headers=self.config["headers"])
            return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
        except RequestException as e:
            logging.error(e)
