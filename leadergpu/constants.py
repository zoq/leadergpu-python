class Actions:
    START = 'start'
    STOP = 'stop'
    SUSPEND = 'suspend'
    RESUME = 'resume'

    def __init__(self):
        return


class Constants:
    def __init__(self, base_url, version):
        self.server_actions: Actions = Actions()
        """Available actions to perform on a server"""

        self.base_url: str = base_url
        """LeaderGPU's Public API URL"""

        self.version: str = version
        """Current SDK Version"""
