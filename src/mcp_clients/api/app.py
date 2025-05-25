from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import Dict, Any
from contextlib import asynccontextmanager
from src.mcp_clients.core.client import MCPUSE_CLIENT
import json

import mcp_use

mcp_use.set_debug(1)

with open("server_config.json") as f:
    config = json.load(f)
    print(f"Config: {config}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for the FastAPI application."""
    client = MCPUSE_CLIENT(config=config)
    try:
        app.state.client = client
        yield  # Yield the client for use in the app
    except Exception as e:
        print(f"Error during lifespan: {e}")
        raise e
    finally:
        await client.client.close_all_sessions()
        print("Client shutdown successfully.")

app = FastAPI(title="MCP Client API", lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development purposes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
async def process_query(request: QueryRequest):
    """Process a query using the MCP client."""
    try:
        result = await app.state.client.process_query(request.query)
        print(f"Result: {result}")
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

