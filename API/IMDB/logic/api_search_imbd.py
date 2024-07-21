from API.IMDB.infra.api_wrapper import APIWrapper


class APISearchImdb:
    BASE_URL = "https://imdb188.p.rapidapi.com"
    HEADERS = {"x-rapidapi-host": "imdb188.p.rapidapi.com",
               "x-rapidapi-key": "23bdb40c39mshf54e59983cc594fp14cb41jsnd33cf0964b97"}
    SEARCH_URL = "/api/v1/searchIMDB"
    SPECIFIC_SEARCH = "/api/v1/searchIMDB?query="

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_search_imdb_for_text(self, text):
        """
        this function sends a GET request ,including headers and text as param
        :param text: the search input
        :return:list of results for the search input
        """
        full_url = f"{self.BASE_URL}{self.SPECIFIC_SEARCH}{text}"
        return self._request.get_request(full_url, headers=self.HEADERS)
