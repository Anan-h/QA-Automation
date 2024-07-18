from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.logic.entities.movies_filter import MoviesFilter


class APIPopularMovies:
    URL = "https://imdb188.p.rapidapi.com/api/v1/getPopularMovies"
    HEADERS = {"x-rapidapi-host": "imdb188.p.rapidapi.com",
               "x-rapidapi-key": "23bdb40c39mshf54e59983cc594fp14cb41jsnd33cf0964b97"}

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_all_popular_movies(self):
        return self._request.post_request(self.URL, headers=self.HEADERS)

    def get_popular_movies_in_country_by_genre(self, country, genre):
        body = MoviesFilter(country, genre).to_dict()
        return self._request.post_request(self.URL, headers=self.HEADERS, body=body)
