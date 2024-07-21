from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.logic.entities.movies_filter import MoviesFilter


class APIUpcomingMovies:
    URL = "https://imdb188.p.rapidapi.com/api/v1/getUpcomingMovies?region="
    HEADERS = {"x-rapidapi-host": "imdb188.p.rapidapi.com",
               "x-rapidapi-key": "23bdb40c39mshf54e59983cc594fp14cb41jsnd33cf0964b97"}

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_upcoming_movies_in_country(self, country):
        """
        this function sends a get request, including headers
        :param country: country initials
        :return: list of all upcoming movies in the same country
        """
        country = MoviesFilter(country).country
        full_url = f"{self.URL}{country}"
        return self._request.get_request(full_url, headers=self.HEADERS)