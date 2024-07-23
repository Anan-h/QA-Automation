import requests
from API.IMDB.infra.response_wrapper import ResponseWrapper


class APIWrapper:

    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, body=None, headers=None):
        response = requests.get(url, json=body, headers=headers)
        return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())

    @staticmethod
    def post_request(url, body=None, headers=None):
        response = requests.post(url, json=body, headers=headers)
        return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())

