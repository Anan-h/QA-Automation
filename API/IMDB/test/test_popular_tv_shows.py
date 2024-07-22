import logging
import unittest
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.logic.api_popular_tv_shows import APIPopularTvShows
from API.IMDB.logic.enum.country import Country
from API.IMDB.logic.enum.genre import Genre


class TestPopularTvShows(unittest.TestCase):
    def setUp(self):
        self.config = ConfigProvider().load_from_file('../config.json')
        self.api_request = APIWrapper()
        self.request = APIPopularTvShows(self.api_request)

    def tearDown(self):
        logging.info("-----------------------------------------------------------------")

    def test_get_popular_tv_shows_in_country_by_genre(self):
        logging.info("testing the get popular tv shows with genre and country filters function")
        response = self.request.get_popular_tv_shows_in_country_by_genre(Country.USA.value, Genre.ACTION.value)
        self.assertEqual(response.status, self.config["status_code"])
        self.assertEqual(response.data["message"], self.config["good_message"])

    def test_get_all_popular_tv_shows(self):
        logging.info("testing the get all popular tv shows function")
        response = self.request.get_all_popular_tv_shows()
        self.assertEqual(response.status, self.config["status_code"])
        self.assertEqual(response.data["message"], self.config["good_message"])
