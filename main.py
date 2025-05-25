# main.py
import click
import asyncio
from src.mcp_clients.core.client_terminal import run_terminal_client

@click.group()
def cli(): pass

@cli.command()
def terminal():
    asyncio.run(run_terminal_client())

@cli.command()
def api():
    import uvicorn
    uvicorn.run("src.mcp_clients.api.app:app", host="0.0.0.0", port=2000)

if __name__ == "__main__":
    api()
