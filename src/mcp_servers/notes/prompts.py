from mcp.server.fastmcp import FastMCP
from .storage import read_all_notes

def register_prompts(mcp: FastMCP):
    @mcp.prompt()
    def note_summary_prompt() -> str:
        notes = read_all_notes()
        return "No notes." if not notes else f"Please summarize:\n{notes}"
