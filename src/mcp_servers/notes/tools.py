from mcp.server.fastmcp import FastMCP
from .storage import append_note, read_all_notes

def register_tools(mcp: FastMCP):
    @mcp.tool()
    def add_note(message: str) -> str:
        append_note(message) 
        return "Note added 👍"

    @mcp.tool()
    def read_notes() -> str:
        return read_all_notes()
