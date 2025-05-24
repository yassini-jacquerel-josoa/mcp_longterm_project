#!/usr/bin/env bash
# Démarre le serveur TODO
uv run python src/mcp_server_todo/todo_server.py &

# Démarre le serveur Weather
uv run python src/mcp_server_weather/weather_server.py &

wait
