# !bin/bash

uvicorn business:business_service --port 8002 &
uvicorn db:db_service --port 8001 &
uvicorn client:client --host 0.0.0.0 --port 8000