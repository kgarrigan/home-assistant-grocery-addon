#!/usr/bin/with-contenv bashio
# Minimal startup script
exec uvicorn main:app --host 0.0.0.0 --port 8000
