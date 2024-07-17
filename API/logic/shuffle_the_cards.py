from API.infra.api_wrapper import APIWrapper


class ShuffleTheCards:
    URL = "/api/deck/new/shuffle/?deck_count="

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_shuffle_the_cards(self,url,count=1):
        full_url=f"{url}{self.URL}{count}"
        return self._request.get_request(full_url)

    def post_shuffle_the_cards(self,url,count=1):
        full_url = f"{url}{self.URL}{count}"
        return self._request.post_request(full_url)

