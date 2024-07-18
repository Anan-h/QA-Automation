from API.deck_of_cards.infra.api_wrapper import APIWrapper


class BrandNewDeck:
    URL = "/api/deck/new/"
    JOKERS = "/api/deck/new/?jokers_enabled=true"

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_new_deck(self, url):
        full_url = f"{url}{self.URL}"
        return self._request.get_request(full_url)

    def post_new_deck(self, url):
        full_url = f"{url}{self.URL}"
        return self._request.post_request(full_url)

    def get_new_deck_with_jokers(self, url):
        full_url = f"{url}{self.JOKERS}"
        return self._request.get_request(full_url)

    def post_new_deck_with_jokers(self, url):
        full_url = f"{url}{self.JOKERS}"
        return self._request.post_request(full_url)
