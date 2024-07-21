import logging

from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.logic.entities.movies_filter import MoviesFilter


class APIWhatsStreaming:
    URL = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming?"
    HEADERS = {"x-rapidapi-host": "imdb188.p.rapidapi.com",
               "x-rapidapi-key": "23bdb40c39mshf54e59983cc594fp14cb41jsnd33cf0964b97"}

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_whats_streaming_in_country(self, country):
        """
        this function sends a get request ,including headers
        :param country: country initials
        :return: list of what's streaming in the same country
        """
        country = MoviesFilter(country).country
        full_url = f"{self.URL}{country}"
        logging.info(f"getting what's streaming in: {country}")
        return self._request.get_request(full_url, headers=self.HEADERS)