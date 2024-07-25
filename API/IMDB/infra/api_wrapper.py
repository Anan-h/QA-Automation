import requests
from API.IMDB.infra.response_wrapper import ResponseWrapper


class APIWrapper:

    def __init__(self):
        self._request = None

    def get_request(self, url, body=None, headers=None):
        response = requests.get(url=url, json=body, headers=headers)
        return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())

    def post_request(self, url, body=None, headers=None):
        response = requests.post(url=url, json=body, headers=headers)
        return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
