import requests

from leadergpu.http_client.http_client import handle_error

TOKEN_ENDPOINT = '/signin'


class AuthenticationService:
    """A service for client authentication"""

    def __init__(self, client_id: str, client_secret: str, base_url: str) -> None:
        """Initialize a authentication service object

        :param client_id: client id
        :type client_id: str
        :param client_secret: client secret
        :type client_secret: str
        :param base_url: base url
        :type base_url: str
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = base_url

    def authenticate(self) -> dict:
        """Authenticate the client and store the authentication token

        returns an authentication data dictionary with the following schema:
        {
            "id": the user's id int,
            "auth_token": authentication token
        }

        :return: authentication data (id, auth_token)
        :rtype: dict
        """
        url = self._base_url + TOKEN_ENDPOINT
        payload = {
            "login": self._client_id,
            "password": self._client_secret
        }

        response = requests.post(url, data=payload, headers=self._generate_headers())
        handle_error(response)

        auth_data = response.json()

        self._auth_token = auth_data['auth_token']
        self._user_id = auth_data['id']

        return auth_data

    def _generate_headers(self):
        # get the first 10 chars of the client id
        client_id_truncated = self._client_id[:10]
        headers = {
            "Accept": "application/json",
            'User-Agent': 'leadergpu-python-' + client_id_truncated
        }
        return headers
