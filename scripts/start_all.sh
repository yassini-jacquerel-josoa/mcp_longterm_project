
# Démarre le serveur sticky notes
uv run -m src.mcp_servers.notes.main &

# Démarre le serveur API
uv run main.py

