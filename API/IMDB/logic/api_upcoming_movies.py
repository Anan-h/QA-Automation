import logging
from requests import RequestException
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.logic.entities.movies_filter import MoviesFilter


class APIUpcomingMovies:
    END_POINT = "/getUpcomingMovies?region="

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file('C:\\Users\\ananh\\OneDrive\\Desktop\\QA Course\\Automation\\Automation_GIT\\API\\IMDB\\config.json')

    def get_upcoming_movies_in_country(self, country):
        """
        this function sends a get request, including headers
        :param country: country initials
        :return: list of all upcoming movies in the same country
        """
        try:
            country = MoviesFilter(country).country
            full_url = f"{self.config['base_url']}{self.END_POINT}{country}"
            logging.info(f"getting upcoming movies in: {country}")
            return self._request.get_request(full_url, headers=self.config["headers"])
        except RequestException as e:
            logging.error(e)