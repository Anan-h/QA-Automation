import requests


class APIWrapper:

    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, body=None, headers=None):
        return requests.get(url, json=body, headers=headers)

    @staticmethod
    def post_request(url, body=None, headers=None):
        return requests.post(url, json=body, headers=headers)

