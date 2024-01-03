from typing import List


class Products:
    """A products class"""

    def __init__(self,
                 id: str,
                 code: str,
                 name: str,
                 period_type: str,
                 period_count: int,
                 price: float,
                 currency: str,
                 free_time: str,
                 server_configuration_id: int,
                 os: List[str],
                 weight: int) -> None:
        """Initialize a product object

        :param id: product id
        :type id: str
        :param code: product code e.g. 'GPU:Nvidia:GTX1080:4:Minute'
        :type code: str
        :param name: product name
        :type name: str
        :param period_type: product period type
        :type period_type: str
        :param period_count: product period count
        :type period_count: int
        :param price: product price
        :type price: float
        :param currency: product currency
        :type currency: str
        :param free_time: product free time
        :type free_time: str
        :param server_configuration_id: product server configuration id
        :type server_configuration_id: int
        :param os: product os
        :type os: List[str]
        :param weight: product weight
        :type weight: int
        """
        self._id = id
        self._code = code
        self._name = name
        self._period_type = period_type
        self._period_count = period_count
        self._price = price
        self._currency = currency
        self._free_time = free_time
        self._server_configuration_id = server_configuration_id
        self._os = os
        self._weight = weight

    @property
    def id(self) -> str:
        """Get the product id

        :return: product id
        :rtype: str
        """
        return self._id

    @property
    def code(self) -> str:
        """Get the product code

        :return: product code e.g. 'GPU:Nvidia:GTX1080:4:Minute'
        :rtype: str
        """
        return self._code

    @property
    def name(self) -> str:
        """Get the product name

        :return: product name
        :rtype: str
        """
        return self._name

    @property
    def period_type(self) -> str:
        """Get the product period type

        :return: product period type
        :rtype: str
        """
        return self._period_type

    @property
    def period_count(self) -> int:
        """Get the product period count

        :return: product period count
        :rtype: int
        """
        return self._period_count

    @property
    def price(self) -> float:
        """Get the product price

        :return: product price
        :rtype: float
        """
        return self._price

    @property
    def currency(self) -> str:
        """Get the product currency

        :return: product currency
        :rtype: str
        """
        return self._currency

    @property
    def free_time(self) -> str:
        """Get the product free time

        :return: product free time
        :rtype: str
        """
        return self._free_time

    @property
    def server_configuration_id(self) -> int:
        """Get the product server configuration id

        :return: product server configuration id
        :rtype: int
        """
        return self._server_configuration_id

    @property
    def os(self) -> List[str]:
        """Get the product os

        :return: product os
        :rtype: List[str]
        """
        return self._os

    @property
    def weight(self) -> int:
        """Get the product weight

        :return: product weight
        :rtype: int
        """
        return self._weight

    def __str__(self) -> str:
        """Print the product

        :return: product string representation
        :rtype: str
        """
        return (f'id: {self._id}\n'
                f'name: {self._name}\n'
                f'price: {self._price} {self._currency}\n'
                f'free_time: {self._free_time}\n'
                f'os: {self._os}\n'
                )


class ProductsService:
    """A service for interacting with the products endpoint"""

    def __init__(self, http_client) -> None:
        """Initialize a product service object

        :param http_client: http client to interact with the HTTP API
        :type http_client: HTTPClient
        """
        self._http_client = http_client

    def get(self) -> List[Products]:
        """Returns a list of available products

        :return: list of available products
        :rtype: List[Products]
        """
        products = self._http_client.get('/servers/products').json()
        product_objects = list(map(lambda product: Products(
            id=product['id'],
            code=product['code'],
            name=product['name'],
            period_type=product['period_type'],
            period_count=int(product['period_count']),
            price=float(product['price']),
            currency=product['currency'],
            free_time=product['free_time'],
            server_configuration_id=product['server_configuration_id'],
            os=product['os'],
            weight=int(product['weight'])
        ), products))
        return product_objects
