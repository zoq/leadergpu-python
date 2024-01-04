import os
from leadergpu import LeaderGPUClient

CLIENT_ID = os.environ['LEADERGPU_CLIENT_ID']
CLIENT_SECRET = os.environ['LEADERGPU_AUTH_TOKEN']

# Create LeaderGPU client
leadergpu = LeaderGPUClient(CLIENT_ID, CLIENT_SECRET)

# Get the first available server
available_server = [server for server in leadergpu.servers.get() if server._start_at != None][0]

# Print available server
print(available_server)

# Resume the server
available_server.resume()

# Suspend the server
print(available_server.suspend())
