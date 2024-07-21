from API.IMDB.infra.api_wrapper import APIWrapper


class APIEmmyWinners:
    URL = " https://imdb188.p.rapidapi.com/api/v1/emmyWinners"
    HEADERS = {"x-rapidapi-host": "imdb188.p.rapidapi.com",
               "x-rapidapi-key": "23bdb40c39mshf54e59983cc594fp14cb41jsnd33cf0964b97"}

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_all_emmy_winners(self):
        """
        this function sends a get request including headers
        :return: list of all emmy winners
        """
        return self._request.get_request(self.URL, headers=self.HEADERS)