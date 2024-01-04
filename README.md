# Unofficial LeaderGPU Python SDK

A Python library for interacting with the LeaderGPU Public API

### Getting Started

1. Install with pip:

pip install leadergpu-python

2. Set the `LEADERGPU_CLIENT_ID` (Email) and `LEADERGPU_AUTH_TOKEN` (password) from environment variable

```bash
export LEADERGPU_CLIENT_ID="username@mail.org"
export LEADERGPU_AUTH_TOKEN="XXXXXX"
```

3. Example for showing avilable server:

```python
import os
from leadergpu import LeaderGPUClient

CLIENT_ID = os.environ['LEADERGPU_CLIENT_ID']
CLIENT_SECRET = os.environ['LEADERGPU_AUTH_TOKEN']

# Create LeaderGPU client
leadergpu = LeaderGPUClient(CLIENT_ID, CLIENT_SECRET)


servers = leadergpu.servers.get()
for server in servers:
    print(server)
    print("---------------")
```
