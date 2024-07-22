import logging
from requests import RequestException
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider


class APIOscarsWinners:
    END_POINT = "/getOscarWinners"

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file('../config.json')

    def get_oscars_winners(self):
        """
        this function sends a get request, including headers
        :return: list of all oscars winners
        """
        try:
            logging.info("getting all oscars winners")
            full_url = f"{self.config['base_url']}{self.END_POINT}"
            return self._request.get_request(full_url, headers=self.config["headers"])
        except RequestException as e:
            logging.error(e)
