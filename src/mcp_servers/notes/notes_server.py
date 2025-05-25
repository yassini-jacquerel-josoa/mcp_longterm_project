from mcp.server.fastmcp import FastMCP
import os
import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route, Mount
from starlette.responses import Response

from mcp.server.sse import SseServerTransport

sse = SseServerTransport("/messages/")


async def handle_sse(request: Request):
    _server = mcp._mcp_server
    async with sse.connect_sse(
        request.scope,
        request.receive,
        request._send
    ) as (reader, writer):
        await _server.run(reader, writer, _server.create_initialization_options())

mcp = FastMCP("AI Sticky Notes")  # use as an example MCP server

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")


def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            f.write("")


@mcp.tool()
def add_note(mesage: str) -> str:
    """"
    Add a note to the sticky notes file.

    Args:
        message: str: The message to add to the sticky note

    Returns:
      str: Confirmation message indicating that the note has been added.
    """
    ensure_file()
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(mesage + "\n")
    return "Note added successfully!"


@mcp.tool()
def read_notes() -> str:
    """
    Read all and return notes from the sticky notes file.

    Returns:
        str: The content of the sticky notes file.
    """
    ensure_file()
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()

    return content if content else "No notes found."


@mcp.resource("notes://latest")
def get_latest_notes() -> str:
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()

    return lines[-1].strip() if lines else "No notes found."


@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Generate a prompt asking the AI to summarize all the current notes.

    Returns:
        str: A prompt string that includes all notes and asks for a summary.
            If no notes are found, it returns a message indicating that.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()

    if not content:
        return "No notes found."
    return f"Summarize the current notes: {content}"


app = Starlette(
    debug=True,
    routes=[
        Route("/sse", endpoint=handle_sse),
        Mount("/messages/", app=sse.handle_post_message)
    ],
)

if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=3000)
