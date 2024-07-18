import requests


class APIWrapper:
    def _init_(self):
        self._request = None

    @staticmethod
    def get_request(url, body=None):
        return requests.get(url, json=body)

    @staticmethod
    def post_request(url, body=None):
        return requests.post(url, json=body)
