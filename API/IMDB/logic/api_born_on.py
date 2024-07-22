import logging
from requests import RequestException
from API.IMDB.infra.api_wrapper import APIWrapper
from API.IMDB.infra.config_provider import ConfigProvider
from API.IMDB.infra.response_wrapper import ResponseWrapper
from API.IMDB.logic.entities.birth_date import BirthDate


class APIBornOn:
    END_POINT = "/getBornOn?"

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file('../config.json')

    def get_actors_born_on_date(self, day, month):
        """
        this function sends a get request to url with day and month as params ,including headers
        :param day: specific day
        :param month: specific month
        :return: list of actors that born on the same date
        """
        try:
            birth_date = BirthDate(day, month).__str__()
            full_url = f"{self.config["base_url"]}{self.END_POINT}{birth_date}"
            logging.info(f"getting actors that born on: {birth_date} ")
            response = self._request.get_request(full_url, headers=self.config["headers"])
            return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
        except RequestException as e:
            logging.error(e)

