# !bin/bash

podman build -t app .
podman run -p 8000:8000 app
