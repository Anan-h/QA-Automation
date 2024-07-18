from API.IMDB.infra.api_wrapper import APIWrapper


class APIOscarsWinners:
    URL = "https://imdb188.p.rapidapi.com/api/v1/getOscarWinners"
    HEADERS = {"x-rapidapi-host": "imdb188.p.rapidapi.com",
               "x-rapidapi-key": "23bdb40c39mshf54e59983cc594fp14cb41jsnd33cf0964b97"}

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_oscars_winners(self):
        return self._request.get_request(self.URL,headers=self.HEADERS)
