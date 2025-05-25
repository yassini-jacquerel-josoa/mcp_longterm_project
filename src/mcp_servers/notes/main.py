
import uvicorn
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route, Mount
from starlette.responses import Response

from src.mcp_servers.notes.tools import register_tools
from src.mcp_servers.notes.resources import register_resources
from src.mcp_servers.notes.prompts import register_prompts
from src.mcp_servers.notes.storage import ensure_storage

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

mcp = FastMCP("notes")
ensure_storage()

register_tools(mcp)
register_resources(mcp)
register_prompts(mcp)




app = Starlette(
    debug=True,
    routes=[
        Route("/sse", endpoint=handle_sse),
        Mount("/messages/", app=sse.handle_post_message)
    ],
)

if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=3000)
