from API.infra.api_wrapper import APIWrapper


class BackOfCard:
    URL="/static/img/back.png"

    def __init__(self,request:APIWrapper):
        self._request=request

    def get_back_of_card(self,url):
        full_url=f"{url}{self.URL}"
        return self._request.get_request(full_url)

    def post_back_of_card(self,url):
        full_url = f"{url}{self.URL}"
        return self._request.post_request(full_url)
