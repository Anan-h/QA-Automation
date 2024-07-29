import logging
import unittest
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.infra.jira_handler import JiraHandler
from API.IMDB.logic.api_popular_movies import APIPopularMovies
from API.IMDB.logic.enum.country import Country
from API.IMDB.logic.enum.genre import Genre


class TestPopularMovies(unittest.TestCase):
    jira_handler = JiraHandler()

    def setUp(self):
        self.config = ConfigProvider().load_from_file(
            'C:\\Users\\ananh\\OneDrive\\Desktop\\QA Course\\Automation\\Automation_GIT\\API\\IMDB\\config.json')
        self.api_request = APIWrapper()
        self.request = APIPopularMovies(self.api_request)

    def tearDown(self):
        logging.info("-----------------------------------------------------------------")

    def test_get_all_popular_movies(self):
        logging.info("testing the get all popular movies function")
        response = self.request.get_all_popular_movies()
        self.assertEqual(response.status, self.config["status_code"])
        self.assertEqual(response.data["message"], self.config["good_message"])

    def test_get_popular_movies_in_country_by_genre(self):
        logging.info("testing the get popular movies with genre and country filters function")
        response = self.request.get_popular_movies_in_country_by_genre(Country.USA.value, Genre.ACTION.value)
        d = response.data["data"]
        page_info = d["pageInfo"]
        total = page_info["total"]
        self.assertEqual(response.status, self.config["status_code"])
        self.assertEqual(response.data["message"], self.config["good_message"])
        self.assertIsNotNone(total)
