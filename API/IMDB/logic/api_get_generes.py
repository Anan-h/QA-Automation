import logging
from requests import RequestException
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.infra.response_wrapper import ResponseWrapper


class APIGetGenres:
    END_POINT = "/getGenres"

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file('../config.json')

    def get_all_genres(self):
        """
        this function sends a get request, including headers
        :return: list of all genres
        """
        try:
            logging.info("getting all genres")
            full_url = f"{self.config['base_url']}{self.END_POINT}"
            response = self._request.get_request(full_url, headers=self.config["headers"])
            return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
        except RequestException as e:
            logging.error(e)
