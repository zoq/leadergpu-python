from typing import List, Union

import leadergpu.constants as Constants


class Server:
    """A server instance class"""

    def __init__(self,
                 id: int,
                 ip: str,
                 name: str,
                 config: str,
                 start_at: str,
                 end_at: str,
                 valid_to: str,
                 status: str,
                 username: str,
                 os_type: str,
                 token: str,
                 resume_available: bool,
                 suspend_available: bool,
                 uptime: int,
                 remaining: int,
                 progress: int,
                 boot_status: dict,
                 code: str,
                 os: str,
                 server_alias: str,
                 description: str,
                 nomenclature_id: int,
                 period_count: int,
                 nomenclature_ids: List[int],
                 free_time: int,
                 http_client: object
                 ) -> None:
        """Initialize the instance object

        :param id: server id
        :type id: str
        :param ip: server ip address
        :type ip: str
        :param name: server name
        :type name: str
        :param config: server config
        :type config: str
        :param start_at: time when the server started. null if the server has not been started yet
        :type start_at: str
        :param end_at: time when the server was stopped. null if the server currently working
        :type end_at: str
        :param valid_to: paid period for the server
        :type valid_to: str
        :param status: server status.
                       UP - the server is up and running by the user.
                       booting - the server is in boot process.
                       available - the server is available for start or resume.
                       queued - all servers in the pool are busy.
                       busy - deirectly assigned server is occupied by another user
        :type status: str
        :param username: default username (login) for selected OS
        :type username: str
        :param os_type: server os, can be one of the following: 'centos', 'windows', 'ubuntu'
        :type os_type: str
        :param token: server token for remote access
        :type token: str
        :param resume_available: boolean True if current server can be resumed
        :type resume_available: dict
        :param suspend_available: boolean True if current server can be suspended
        :type suspend_available: bool
        :param uptime: server uptime in seconds
        :type uptime: int
        :param remaining: remaining time in seconds
        :type remaining: int
        :param progress: progress in percents
        :type progress: int
        :param boot_status: boot status
        :type boot_status: dict
        :param code: server code
        :type code: str
        :param os: server os
        :type os: str
        :param server_alias: server alias
        :type server_alias: str
        :param description: server description
        :type description: str
        :param nomenclature_id: nomenclature id
        :type nomenclature_id: int
        :param period_count: period count
        :type period_count: int
        :param nomenclature_ids: nomenclature ids
        :type nomenclature_ids: List[int]
        :param free_time: free time
        :type free_time: int
        :param http_client: http client to interact with the HTTP API
        :type http_client: HTTPClient
        """
        self._id = id
        self._ip = ip
        self._name = name
        self._config = config
        self._start_at = start_at
        self._end_at = end_at
        self._valid_to = valid_to
        self._status = status
        self._username = username
        self._os_type = os_type
        self._token = token
        self._resume_available = resume_available
        self._suspend_available = suspend_available
        self._uptime = uptime
        self._remaining = remaining
        self._progress = progress
        self._boot_status = boot_status
        self._code = code
        self._os = os
        self._server_alias = server_alias
        self._description = description
        self._nomenclature_id = nomenclature_id
        self._period_count = period_count
        self._nomenclature_ids = nomenclature_ids
        self._free_time = free_time
        self._http_client = http_client

    @property
    def id(self) -> str:
        """Get the instance id

        :return: instance id
        :rtype: str
        """
        return self._id

    @property
    def instance_type(self) -> str:
        """Get the instance type

        :return: instance type
        :rtype: str
        """
        return self._instance_type

    @property
    def status(self) -> str:
        """Get the instance status

        :return: instance status
        :rtype: str
        """
        return self._status

    def resume(self) -> bool:
        """Resume the server

        :return: resume server success status
        :rtype: bool
        """
        result = self._http_client.post(f"/servers/{self._id}/resume").json()
        return result['success']

    def suspend(self) -> bool:
        """Suspend the server

        :return: suspend server success status
        :rtype: bool
        """
        result = self._http_client.post(f"/servers/{self._id}/suspend").json()
        return result['success']

    def stop(self) -> bool:
        """Stops the server

        :return: start server success status
        :rtype: bool
        """
        result = self._http_client.post(f"/servers/{self._id}/stop").json()
        return result['success']

    def start(self) -> bool:
        """Starts the server

        :return: start server success status
        :rtype: bool
        """
        result = self._http_client.post(f"/servers/{self._id}/start").json()
        return result['success']

    def __str__(self) -> str:
        """Print the server

        :return: server string representation
        :rtype: str
        """
        return (f'id: {self._id}\n'
                f'ip: {self._ip}\n'
                f'status: {self._status}\n'
                f'config: {self._config}\n'
                f'username: {self._username}\n'
                f'os: {self._os}\n'
                f'start_at: {self._start_at}\n'
                f'valid_to: {self._valid_to}\n'
                f'remaining: {self._remaining}\n'
                )


class ServersService:
    """A service for interacting with the servers endpoint"""

    def __init__(self, http_client) -> None:
        """Initialize the servers service object

        :param http_client: http client to interact with the HTTP API
        :type http_client: HTTPClient
        """
        self._http_client = http_client

    def get(self) -> List[Server]:
        """Get all of the client's non-deleted servers, or servers with specific status

        :return: list of server details objects
        :rtype: List[Server]
        """
        servers_dict = self._http_client.get("/servers").json()
        servers = list(map(lambda servers_dict: Server(
            id=servers_dict['id'],
            ip=servers_dict['ip'],
            name=servers_dict['name'],
            config=servers_dict['config'],
            start_at=servers_dict['start_at'],
            end_at=servers_dict['end_at'],
            valid_to=servers_dict['valid_to'],
            status=servers_dict['status'],
            username=servers_dict['username'],
            os_type=servers_dict['os_type'],
            token=servers_dict['token'],
            resume_available=servers_dict['resume_available'],
            suspend_available=servers_dict['suspend_available'],
            uptime=servers_dict['uptime'],
            remaining=servers_dict['remaining'],
            progress=servers_dict['progress'],
            boot_status=servers_dict['boot_status'],
            code=servers_dict['code'],
            os=servers_dict['os'],
            server_alias=servers_dict['server_alias'],
            description=servers_dict['description'],
            nomenclature_id=servers_dict['nomenclature_id'],
            period_count=servers_dict['period_count'],
            nomenclature_ids=servers_dict['nomenclature_ids'],
            free_time=servers_dict['free_time'],
            http_client=self._http_client
        ), servers_dict))
        return servers

    def get_by_id(self, id: int) -> Server:
        """Get a server with specified id

        :param id: server id
        :type id: int
        :return: server details object
        :rtype: Server
        """
        return [server for server in self.get() if server.id == id][0]

    def order(self, nomenclature_id: int, os: str, period_count: int) -> dict:
        """Creates a new server instance

        :param nomenclature_id: product id returned in products list call
        :type nomenclature_id: int
        :param os: os type, can be one of the following: 'centos', 'windows', 'ubuntu'
        :type os: str
        :param period_count: order period
        :type period_count: int
        """
        payload = {
            "nomenclature_id": nomenclature_id,
            "os": os,
            "period_count": period_count
        }
        return self._http_client.post("/servers/order", json=payload).json()

    def action(self, id_list: Union[List[int], int], action: str) -> List[bool]:
        """Performs an action on a list of servers / single server

        :param id_list: list of server ids, or a server id
        :type id_list: Union[List[int], int]
        :param action: the action to perform
        :type action: str
        :return: action success status
        :rtype: List[bool]
        """
        if type(id_list) is int:
            id_list = [id_list]

        status = []
        for id in id_list:
            server = self.get_by_id(id)

            if action == Constants.Actions.START:
                status.append(server.start())
            elif action == Constants.Actions.RESUME:
                status.append(server.resume())
            elif action == Constants.Actions.SUSPEND:
                status.append(server.suspend())
            elif action == Constants.Actions.STOP:
                status.append(server.stop())

        return status
