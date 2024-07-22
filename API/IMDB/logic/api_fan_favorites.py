import logging
from requests import RequestException
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.infra.response_wrapper import ResponseWrapper
from API.IMDB.logic.entities.movies_filter import MoviesFilter


class APIFanFavorites:
    END_POINT = "/getFanFavorites?country="

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file('../config.json')

    def get_fan_favorites_in_country(self, country):
        """
        this function sends a get request with country initials as param , including headers
        :param country: initials of country
        :return: list of all the fan favorites in the same country
        """
        try:
            country = MoviesFilter(country).country
            full_url = f"{self.config['base_url']}{self.END_POINT}{country}"
            logging.info(f"getting fan favorites in: {country}")
            response = self._request.get_request(full_url, headers=self.config["headers"])
            return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
        except RequestException as e:
            logging.error(e)
