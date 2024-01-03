from leadergpu.authentication.authentication import AuthenticationService
from leadergpu.http_client.http_client import HTTPClient
from leadergpu.products.products import ProductsService
from leadergpu.servers.servers import ServersService
from leadergpu.constants import Constants
from leadergpu.__version__ import VERSION


class LeaderGPUClient:
    """Client for interacting with LeaderGPU's public API"""

    def __init__(self, client_id: str, client_secret: str, base_url: str = "https://api.leaderssl.com/api/v1/users") -> None:
        """The LeaderGPU client

        :param client_id: client id
        :type client_id: str
        :param client_secret: client secret
        :type client_secret: str
        :param base_url: base url for all the endpoints, optional, defaults to "https://api.leaderssl.com/api/v1/users"
        :type base_url: str, optional
        """

        self.constants: Constants = Constants(base_url, VERSION)

        self._authentication: AuthenticationService = AuthenticationService(client_id, client_secret, self.constants.base_url)

        self._http_client: HTTPClient = HTTPClient(self._authentication, self.constants.base_url)

        self.products: ProductsService = ProductsService(self._http_client)
        self.servers: ServersService = ServersService(self._http_client)
