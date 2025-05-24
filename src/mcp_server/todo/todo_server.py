from typing import Any
import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("todo")

# Déplie ~ et prépare le dossier
FILE_PATH = os.path.expanduser("~/OneDrive/Documents/TEST/mcp_longterm_project/todo.json")
os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

@mcp.tool()
async def add_todo(item: str) -> str:
    with open(FILE_PATH, "a+", encoding="utf-8") as f:
        f.write(f"{item}\n")
    return f"Added: {item}"

@mcp.tool()
async def get_todos() -> str:
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.read() or "No todos yet."

@mcp.tool()
async def remove_todo(item: str) -> str:
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        for line in lines:
            if line.strip() != item:
                f.write(line)
    return f"Removed: {item}"

if __name__ == "__main__":
    mcp.run(transport='stdio')
