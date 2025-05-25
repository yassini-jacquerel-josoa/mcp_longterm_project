import asyncio
from fastmcp import Client

async def main():
    # Connexion au serveur weather via stdio
    async with Client("src/mcp_servers/notes/notes_server.py") as client:
        tools = await client.list_tools()
        print("Outils disponibles :", tools)

        # # Exemple d'appel de get_alerts
        # resp_create_todo = await client.call_tool("add_note", {"item": "test"})
        # print("\n\n\nAlerts NY:\n", resp_create_todo) 

        # # Exemple d'appel de get_forecast
        # resp_forecast = await client.call_tool(
        #     "get_forecast",
        #     {"latitude": 38.8977, "longitude": -77.0365}
        # )
        # print("\n\n\nPrévision WA DC:\n")
        # all_texts = [tc.text for tc in resp_forecast]
        # for t in all_texts:
        #     print(t)

if __name__ == "__main__":
    asyncio.run(main())
