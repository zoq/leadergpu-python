import requests
import json

from leadergpu.exceptions import APIException
from leadergpu.__version__ import VERSION


def handle_error(response: requests.Response) -> None:
    """checks for the response status code and raises an exception if it's 400 or higher.

    :param response: the API call response
    :raises APIException: an api exception with message and error type code
    """
    if not response.ok:
        data = json.loads(response.text)
        code = data['code'] if 'code' in data else None
        message = data['message'] if 'message' in data else None
        raise APIException(code, message)


class HTTPClient:
    """An http client, a wrapper for the requests library.

    For each request, it adds the authentication header with an access token.
    If the access token is expired it refreshes it before calling the specified API endpoint.
    Also checks the response status code and raises an exception if needed.
    """

    def __init__(self, auth_service, base_url: str) -> None:
        self._version = VERSION
        self._base_url = base_url
        self._auth_service = auth_service
        self._auth_service.authenticate()

    def post(self, url: str, json: dict = None, params: dict = None, **kwargs) -> requests.Response:
        """Sends a POST request.

        A wrapper for the requests.post method.

        Builds the url, uses custom headers, refresh tokens if needed.

        :param url: relative url of the API endpoint
        :type url: str
        :param json: A JSON serializable Python object to send in the body of the Request, defaults to None
        :type json: dict, optional
        :param params: Dictionary of querystring data to attach to the Request, defaults to None
        :type params: dict, optional

        :raises APIException: an api exception with message and error type code

        :return: Response object
        :rtype: requests.Response
        """

        url = self._add_base_url(url)
        headers = self._generate_headers()

        response = requests.post(url, json=json, headers=headers, params=params, **kwargs)
        handle_error(response)

        return response

    def get(self, url: str, params: dict = None, **kwargs) -> requests.Response:
        """Sends a GET request.

        A wrapper for the requests.get method.

        Builds the url, uses custom headers, refresh tokens if needed.

        :param url: relative url of the API endpoint
        :type url: str
        :param params: Dictionary of querystring data to attach to the Request, defaults to None
        :type params: dict, optional

        :raises APIException: an api exception with message and error type code

        :return: Response object
        :rtype: requests.Response
        """
        headers = self._generate_headers()
        url = self._add_base_url(url)

        response = requests.get(url, headers=headers)
        handle_error(response)

        return response

    def _generate_headers(self) -> dict:
        """Generate the default headers for every request

        :return: dict with request headers
        :rtype: dict
        """
        headers = {
            'User-Agent': self._generate_user_agent(),
            'Content-Type': 'application/json',
            'X-Auth-Token': self._auth_service._auth_token
        }
        return headers

    def _generate_user_agent(self) -> str:
        """Generate the user agent string.

        :return: user agent string
        :rtype: str
        """
        client_id_truncated = self._auth_service._client_id[:10]

        return f'leadergpu-python-v{self._version}-{client_id_truncated}'

    def _add_base_url(self, url: str) -> str:
        """Adds the base url to the relative url

        :param url: a relative url path
        :type url: str
        :return: the full url path
        :rtype: str
        """
        return self._base_url + "/" + str(self._auth_service._user_id) + url
