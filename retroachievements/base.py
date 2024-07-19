import requests as request
from retroachievements import __version__

_BASE_URL = "https://retroachievements.org/API/"


class BaseRAClient:
    """
    Main class for accessing the RetroAchievements Web API
    """

    headers = {"User-Agent": "RetroAchievements-api-python/" + __version__}

    def __init__(self, username: str, api_key: str):
        self.username = username
        self.api_key = api_key

    def url_params(self, params: dict | None = None):
        """
        Inserts the auth and query params into the request
        """
        if params is None:
            params = {}
        params.update({"z": self.username, "y": self.api_key})
        return params

    # URL construction
    def _call_api(
        self,
        endpoint: dict | None = None,
        params: dict | None = None,
        timeout: int = 30,
        headers: dict | None = None,
    ):
        if endpoint is None:
            endpoint = {}
        req = request.get(
            f"{_BASE_URL}{endpoint}",
            params=self.url_params(params),
            timeout=timeout,
            headers=headers,
        )
        return req
