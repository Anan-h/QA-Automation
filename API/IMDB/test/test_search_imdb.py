import logging
import unittest
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.infra.jira_handler import JiraHandler
from API.IMDB.logic.api_search_imbd import APISearchImdb


class TestSearchIMDB(unittest.TestCase):
    def setUp(self):
        self.config = ConfigProvider().load_from_file(
            'C:\\Users\\ananh\\OneDrive\\Desktop\\QA Course\\Automation\\Automation_GIT\\API\\IMDB\\config.json')
        self.api_request = APIWrapper()
        self.request = APISearchImdb(self.api_request)
        self.jira_handler = JiraHandler()

    def tearDown(self):
        if hasattr(self, '_outcome'):
            errors = self._outcome.errors
            for test, exc_info in errors:
                if exc_info is not None:
                    logging.error("Test failed: %s", self._testMethodName)
        logging.info("-----------------------------------------------------------------")

    def test_search_imdb_for_valid_movie_name(self):
        logging.info("testing the search function with valid input ")
        response = self.request.get_search_imdb_for_text(self.config["movie_name"])
        # self.assertTrue(response.ok)
        # self.assertEqual(response.status, self.config["status_code"])
        # self.assertEqual(response.data["message"], self.config["good_message"])
        self.assertTrue(False)

    def test_search_imdb_for_invalid_movie_name(self):
        logging.info("testing the search function with invalid input")
        response = self.request.get_search_imdb_for_text(self.config["invalid_name"])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, self.config["status_code"])
        self.assertEqual(response.data["message"], self.config["bad_message"])
