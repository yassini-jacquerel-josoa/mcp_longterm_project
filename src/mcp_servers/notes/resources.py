from mcp.server.fastmcp import FastMCP
from .storage import read_all_notes

def register_resources(mcp: FastMCP):
    @mcp.resource("notes://latest")
    def get_latest_notes() -> str:
        notes = read_all_notes().splitlines()
        return notes[-1] if notes else "No notes yet."
