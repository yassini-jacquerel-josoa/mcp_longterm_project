# common/utils.py
import os
import json
import logging
from pathlib import Path
from dotenv import load_dotenv
import httpx

# ————— Config & .env —————
def load_env(env_path: str = None):
    """Charge le .env à la racine si présent."""
    load_dotenv(env_path or Path(__file__).parents[2] / ".env")

def load_json_config(path: str) -> dict:
    """Charge une config JSON depuis un fichier."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# ————— Gestion des chemins —————
def expand_path(p: str) -> Path:
    """Déplie '~' et crée le dossier parent si besoin."""
    path = Path(p).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    return path

# ————— Logger partagé —————
def setup_logging(level: str = "INFO"):
    """Configure un logger racine uniforme."""
    fmt = "%(asctime)s %(levelname)s %(name)s – %(message)s"
    logging.basicConfig(level=getattr(logging, level.upper()), format=fmt)

# ————— Client HTTP réutilisable —————
_http_client: httpx.AsyncClient | None = None
def get_http_client() -> httpx.AsyncClient:
    global _http_client
    if _http_client is None:
        _http_client = httpx.AsyncClient(timeout=30.0)
    return _http_client
