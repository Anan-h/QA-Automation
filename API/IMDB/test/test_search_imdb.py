import logging
import unittest
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.logic.api_search_imbd import APISearchImdb


class TestSearchIMDB(unittest.TestCase):
    def setUp(self):
        self.config = ConfigProvider().load_from_file('../config.json')
        self.api_request = APIWrapper()
        self.request = APISearchImdb(self.api_request)

    def tearDown(self):
        logging.info("-----------------------------------------------------------------")

    def test_search_imdb_for_valid_movie_name(self):
        logging.info("testing the search function with valid input ")
        response = self.request.get_search_imdb_for_text(self.config["movie_name"])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, self.config["status_code"])
        self.assertEqual(response.data["message"], self.config["good_message"])

    def test_search_imdb_for_invalid_movie_name(self):
        logging.info("testing the search function with invalid input")
        response = self.request.get_search_imdb_for_text(self.config["invalid_name"])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, self.config["status_code"])
        self.assertEqual(response.data["message"], self.config["bad_message"])