import logging
from requests import RequestException
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.infra.response_wrapper import ResponseWrapper
from API.IMDB.logic.entities.movies_filter import MoviesFilter


class APIPopularTvShows:
    END_POINT = "/getPopularTVShows"

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file('../config.json')

    def get_all_popular_tv_shows(self):
        """
        this function sends a post request, including headers
        :return: list of all popular tv shows worldwide
        """
        try:
            logging.info("getting all popular tv shows")
            full_url = f"{self.config['base_url']}{self.END_POINT}"
            response = self._request.post_request(full_url, headers=self.config["headers"])
            return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
        except RequestException as e:
            logging.error(e)

    def get_popular_tv_shows_in_country_by_genre(self, country, genre):
        """
        this function sends a post request, including headers and body
        :param country: country initials
        :param genre: genre of the tv show
        :return: list of all popular tv shows in the same country that their genre is the same
        """
        try:
            full_url = f"{self.config['base_url']}{self.END_POINT}"
            body = MoviesFilter(country, genre).to_dict()
            logging.info(f"getting all popular {genre} tv shows, in the {country}")
            response = self._request.post_request(full_url, headers=self.config['headers'], body=body)
            return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
        except RequestException as e:
            logging.error(e)
