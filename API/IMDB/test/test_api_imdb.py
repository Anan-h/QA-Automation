import logging
import unittest
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.logic.api_born_on import APIBornOn
from API.IMDB.logic.api_emmy_winners import APIEmmyWinners
from API.IMDB.logic.api_fan_favorites import APIFanFavorites
from API.IMDB.logic.api_get_countries import APIGetCountries
from API.IMDB.logic.api_get_generes import APIGetGenres
from API.IMDB.logic.api_keywords import APIKeywords
from API.IMDB.logic.api_languages import APILanguages
from API.IMDB.logic.api_oscars_winners import APIOscarsWinners
from API.IMDB.logic.api_popular_celebrities import APIPopularCelebrities
from API.IMDB.logic.api_popular_movies import APIPopularMovies
from API.IMDB.logic.api_popular_tv_shows import APIPopularTvShows
from API.IMDB.logic.api_search_imbd import APISearchImdb
from API.IMDB.logic.api_upcoming_movies import APIUpcomingMovies
from API.IMDB.logic.api_upcoming_tv_episode import APIUpcomingTvEpisode
from API.IMDB.logic.api_upcoming_tv_series import APIUpcomingTvSeries
from API.IMDB.logic.api_week_top_ten import APIWeekTopTen
from API.IMDB.logic.api_whats_streaming import APIWhatsStreaming
from API.IMDB.logic.enum.country import Country
from API.IMDB.logic.enum.genre import Genre


class TestAPIImdb(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider().load_from_file('../config.json')
        self.api_request = APIWrapper()

    def tearDown(self):
        logging.info("-----------------------------------------------------------------")

    def test_search_imdb_for_valid_movie_name(self):
        logging.info("testing the search function with valid input ")
        request = APISearchImdb(self.api_request)
        response = request.get_search_imdb_for_text(self.config["movie_name"])
        data = response.json()
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(data["message"], self.config["good_message"])

    def test_search_imdb_for_invalid_movie_name(self):
        logging.info("testing the search function with invalid input")
        request = APISearchImdb(self.api_request)
        response = request.get_search_imdb_for_text(self.config["invalid_name"])
        data = response.json()
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(data["message"], self.config["bad_message"])

    def test_get_all_popular_movies(self):
        logging.info("testing the get all popular movies function")
        request = APIPopularMovies(self.api_request)
        response = request.get_all_popular_movies()
        response_body = response.json()
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])

    def test_get_popular_movies_in_country_by_genre(self):
        logging.info("testing the get popular movies with genre and country filters function")
        request = APIPopularMovies(self.api_request)
        response = request.get_popular_movies_in_country_by_genre(Country.USA.value, Genre.ACTION.value)
        response_body = response.json()
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])

    def test_get_popular_tv_shows_in_country_by_genre(self):
        logging.info("testing the get popular tv shows with genre and country filters function")
        request = APIPopularTvShows(self.api_request)
        response = request.get_popular_tv_shows_in_country_by_genre(Country.USA.value, Genre.ACTION.value)
        response_body = response.json()
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])

    def test_get_all_popular_tv_shows(self):
        logging.info("testing the get all popular tv shows function")
        request = APIPopularTvShows(self.api_request)
        response = request.get_all_popular_tv_shows()
        response_body = response.json()
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])

    def test_get_oscars_winners(self):
        logging.info("testing the get oscars winners function ")
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
        logging.info("testing the get fan favorites in country function ")
        request = APIFanFavorites(self.api_request)
        response = request.get_fan_favorites_in_country(Country.USA.value)
        response_body = response.json()
        data = response_body["data"]
        count = data["list"]
        total = len(count)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["favorite_usa"])

    def test_get_actors_born_on_date(self):
        logging.info("testing the get actors born on date function")
        request = APIBornOn(self.api_request)
        response = request.get_actors_born_on_date(self.config["day"], self.config["month"])
        response_body = response.json()
        data = response_body["data"]
        count = data["list"]
        total = len(count)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["born_on"])

    def test_get_week_top_ten(self):
        logging.info("testing the get week's top ten function")
        request = APIWeekTopTen(self.api_request)
        response = request.get_week_top_ten()
        response_body = response.json()
        data = response_body["data"]
        total = len(data)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["top_ten"])

    def test_whats_streaming_in_country(self):
        logging.info("testing the get what's streaming in country function ")
        request = APIWhatsStreaming(self.api_request)
        response = request.get_whats_streaming_in_country(Country.USA.value)
        response_body = response.json()
        data = response_body["data"]
        total = len(data)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["whats_streaming_usa"])

    def test_get_all_genres(self):
        logging.info("testing the get all genres function")
        request = APIGetGenres(self.api_request)
        response = request.get_all_genres()
        response_body = response.json()
        data = response_body["data"]
        all_genres = data["all_genres"]
        total = len(all_genres)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["all_genres"])

    def test_get_all_countries(self):
        logging.info("testing the get all countries function ")
        request = APIGetCountries(self.api_request)
        response = request.get_all_countries()
        response_body = response.json()
        data = response_body["data"]
        all_countries = data["all_countries"]
        total = len(all_countries)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["all_countries"])

    def test_get_all_emmy_winners(self):
        logging.info("testing the get emmy winners function ")
        request = APIEmmyWinners(self.api_request)
        response = request.get_all_emmy_winners()
        response_body = response.json()
        data = response_body["data"]
        emmy = data["list"]
        total = len(emmy)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["emmy_winners"])

    def test_popular_celebrities(self):
        logging.info("testing the get popular celebrities function")
        request = APIPopularCelebrities(self.api_request)
        response = request.get_all_popular_celebrities()
        response_body = response.json()
        data = response_body["data"]
        celeb = data["list"]
        total = len(celeb)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["popular_celebrities"])

    def test_get_all_keywords(self):
        logging.info("testing the get all keywords function")
        request = APIKeywords(self.api_request)
        response = request.get_all_keywords()
        response_body = response.json()
        data = response_body["data"]
        key = data["all_keywords"]
        total = len(key)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["key_words"])

    def test_get_all_languages(self):
        logging.info("testing the get all languages function")
        request = APILanguages(self.api_request)
        response = request.get_languages()
        response_body = response.json()
        data = response_body["data"]
        lang = data["all_languages"]
        total = len(lang)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(response_body["message"], self.config["good_message"])
        self.assertEqual(total, self.config["languages"])

    def test_upcoming_movies_in_country(self):
        logging.info("testing the get upcoming movies in country function")
        request = APIUpcomingMovies(self.api_request)
        response = request.get_upcoming_movies_in_country(Country.INDIA.value)
        response_body = response.json()
        movies = response_body["message"]
        total = len(movies)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(total, self.config["india_upcoming_movies"])

    def test_upcoming_tv_series_in_country(self):
        logging.info("testing the get upcoming tv series in country function")
        request = APIUpcomingTvSeries(self.api_request)
        response = request.get_upcoming_tv_series_in_country(Country.INDIA.value)
        response_body = response.json()
        series = response_body["message"]
        total = len(series)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(total, self.config["india_upcoming_series"])

    def test_upcoming_tv_episode_in_country(self):
        logging.info("testing the get upcoming tv episodes in country function")
        request = APIUpcomingTvEpisode(self.api_request)
        response = request.get_upcoming_tv_episode_in_country(Country.INDIA.value)
        response_body = response.json()
        episode = response_body["message"]
        total = len(episode)
        self.assertEqual(response.status_code, self.config["status_code"])
        self.assertEqual(total, self.config["india_upcoming_episode"])
