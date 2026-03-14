#!/bin/sh
set -e

# Wait for MongoDB to accept connections
python - <<'PY'
import socket, time
host = "mongo"
port = 27017
while True:
    try:
        with socket.create_connection((host, port), timeout=2):
            break
    except OSError:
        time.sleep(1)
PY

exec "$@"
