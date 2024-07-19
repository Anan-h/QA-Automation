import unittest
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.logic.api_born_on import APIBornOn
from API.IMDB.logic.api_fan_favorites import APIFanFavorites
from API.IMDB.logic.api_oscars_winners import APIOscarsWinners
from API.IMDB.logic.api_popular_movies import APIPopularMovies
from API.IMDB.logic.api_popular_tv_shows import APIPopularTvShows
from API.IMDB.logic.api_search_imbd import APISearchImdb


class TestAPIImdb(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider().load_from_file('../config.json')
        self.api_request = APIWrapper()

    def test_search_imdb_for_valid_movie_name(self):
        request = APISearchImdb(self.api_request)
        response = request.get_search_imdb_for_text(self.config["movie_name"])
        data = response.json()
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(data["message"], self.config["good_message"])

    def test_search_imdb_for_invalid_movie_name(self):
        request = APISearchImdb(self.api_request)
        response = request.get_search_imdb_for_text(self.config["invalid_name"])
        data = response.json()
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(data["message"], self.config["bad_message"])

    def test_get_all_popular_movies(self):
        request = APIPopularMovies(self.api_request)
        response = request.get_all_popular_movies()
        response_body = response.json()
        data = response_body["data"]
        page_info = data["pageInfo"]
        total = page_info["total"]
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["all_popular_movies"])

    def test_get_popular_movies_in_country_by_genre(self):
        request = APIPopularMovies(self.api_request)
        response = request.get_popular_movies_in_country_by_genre(self.config["country"], self.config["genre"])
        response_body = response.json()
        data = response_body["data"]
        page_info = data["pageInfo"]
        total = page_info["total"]
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["action_us"])

    def test_get_popular_tv_shows_in_country_by_genre(self):
        request = APIPopularTvShows(self.api_request)
        response = request.get_popular_tv_shows_in_country_by_genre(self.config["country"], self.config["genre"])
        response_body = response.json()
        data = response_body["data"]
        page_info = data["pageInfo"]
        total = page_info["total"]
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["tv_action_us"])

    def test_get_all_popular_tv_shows(self):
        request = APIPopularTvShows(self.api_request)
        response = request.get_all_popular_tv_shows()
        response_body = response.json()
        data = response_body["data"]
        page_info = data["pageInfo"]
        total = page_info["total"]
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["all_tv_shows"])

    def test_get_oscars_winners(self):
        request = APIOscarsWinners(self.api_request)
        response = request.get_oscars_winners()
        response_body = response.json()
        data = response_body["data"]
        page_info = data["pageInfo"]
        total = page_info["total"]
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["oscars"])

    def test_fan_favorites_in_country(self):
        request = APIFanFavorites(self.api_request)
        response = request.get_fan_favorites_in_country(self.config["country"])
        response_body = response.json()
        data = response_body["data"]
        count = data["list"]
        total = len(count)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["favorite_usa"])

    def test_get_actors_born_on_date(self):
        request = APIBornOn(self.api_request)
        response = request.get_actors_born_on_date(self.config["day"], self.config["month"])
        response_body = response.json()
        data = response_body["data"]
        count = data["list"]
        total = len(count)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["born_on"])
