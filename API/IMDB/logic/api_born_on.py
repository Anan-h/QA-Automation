import logging

from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.logic.entities.date import Date


class APIBornOn:
    URL = "https://imdb188.p.rapidapi.com/api/v1/getBornOn?"
    HEADERS = {"x-rapidapi-host": "imdb188.p.rapidapi.com",
               "x-rapidapi-key": "23bdb40c39mshf54e59983cc594fp14cb41jsnd33cf0964b97"}

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_actors_born_on_date(self, day, month):
        """
        this function sends a get request to url with day and month as params ,including headers
        :param day: specific day
        :param month: specific month
        :return: list of actors that born on the same date
        """
        date = Date(day, month).__str__()
        full_url = f"{self.URL}{date}"
        logging.info(f"getting actors that born on: {date} ")
        return self._request.get_request(full_url, headers=self.HEADERS)


