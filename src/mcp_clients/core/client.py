import asyncio
import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# This client can connect to multiple servers based on the config file in JSON format.

class MCPUSE_CLIENT:
    def __init__(self, config: dict = None):
        # self.client = MCPClient.from_config_file(
        #     os.path.join(os.path.dirname(__file__), "config.json"))
        self.client = MCPClient.from_dict(config=config)
        self.llm = ChatOpenAI(
            model="gpt-4.1-nano-2025-04-14",
            temperature=0, 
            api_key=OPENAI_API_KEY
        )
        self.agent = MCPAgent(
            llm=self.llm,
            client=self.client,
            max_steps=10,
            use_server_manager=True,
            verbose=True,
        )

    async def process_query(self, query: str) -> str:
        result = await self.agent.run(query)
        return result
