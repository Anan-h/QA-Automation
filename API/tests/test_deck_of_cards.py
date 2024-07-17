import unittest

from API.infra.api_wrapper import APIWrapper
from API.infra.config_provider import ConfigProvider
from API.logic.back_of_card import BackOfCard
from API.logic.brand_new_deck import BrandNewDeck
from API.logic.shuffle_the_cards import ShuffleTheCards


class TestDeckOfCards(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider().load_from_file('../config.json')
        self.api_request = APIWrapper()

    def test_get_new_deck(self):
        request = BrandNewDeck(self.api_request)
        response = request.get_new_deck(self.config["base_url"])
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(response.status_code, self.config["status"])

    def test_get_shuffle_the_cards_in_five_decks(self):
        request = ShuffleTheCards(self.api_request)
        response = request.get_shuffle_the_cards(self.config["base_url"], self.config["count_of_decks"])
        data = response.json()
        self.assertEqual(response.status_code, self.config["status"])
        self.assertEqual(data["remaining"], self.config["deck"] * self.config["count_of_decks"])

    def test_post_new_deck_with_jokers(self):
        request = BrandNewDeck(self.api_request)
        response = request.post_new_deck_with_jokers(self.config["base_url"])
        data = response.json()
        self.assertEqual(response.status_code, self.config["status"])
        self.assertEqual(data["remaining"], self.config["deck"])

    def test_post_back_of_card(self):
        request = BackOfCard(self.api_request)
        response = request.post_back_of_card(self.config["base_url"])
        self.assertEqual(response.status_code, self.config["not_allowed"])
