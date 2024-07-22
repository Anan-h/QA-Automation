import logging
from requests import RequestException
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.infra.response_wrapper import ResponseWrapper
from API.IMDB.logic.entities.movies_filter import MoviesFilter


class APIUpcomingTvEpisode:
    END_POINT = "/getUpcomingTVEpisode?region="

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file('../config.json')

    def get_upcoming_tv_episode_in_country(self, country):
        """
        this function sends a get request, including headers
        :param country: country initials
        :return: list of all upcoming tv episodes in the same country
        """
        try:
            country = MoviesFilter(country).country
            full_url = f"{self.config["base_url"]}{self.END_POINT}{country}"
            logging.info(f"getting upcoming tv episodes in: {country}")
            response = self._request.get_request(full_url, headers=self.config["headers"])
            return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
        except RequestException as e:
            logging.error(e)