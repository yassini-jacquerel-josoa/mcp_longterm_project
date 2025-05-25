import os
from pathlib import Path
from .config import NOTES_FILE

def ensure_storage():
    Path(NOTES_FILE).parent.mkdir(exist_ok=True, parents=True)
    Path(NOTES_FILE).touch(exist_ok=True)

def append_note(msg: str):
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def read_all_notes() -> str:
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()
