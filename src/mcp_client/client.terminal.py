#!/usr/bin/env python
# coding: utf-8

import os
import asyncio
import httpx
from dotenv import load_dotenv, find_dotenv
from mcp_use import MCPAgent, MCPClient
from langchain_openai import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# 1) Patch HTTPX pour forcer UTF-8 sur les en-têtes (Windows)
_orig_headers_init = httpx.Headers.__init__
def _headers_init(self, headers=None, encoding=None, **kwargs):
    return _orig_headers_init(self, headers=headers, encoding="utf-8", **kwargs)
httpx.Headers.__init__ = _headers_init

# 2) Charger la clé OPENAI_API_KEY depuis .env
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def main():
    # 3) Instanciation du client MCP depuis config.json
    client = MCPClient.from_config_file("config.json")

    # 4) Création de l’LLM avec streaming activé
    llm = ChatOpenAI(
        model="gpt-4.1-nano-2025-04-14",
        temperature=0.2,
        api_key=OPENAI_API_KEY,
        streaming=True,  # <— active le streaming des tokens
        callbacks=[StreamingStdOutCallbackHandler()]  # <— affiche chaque jeton
    )

    # 5) Assemblage de l’agent
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=20,
        auto_initialize=True,
        memory_enabled=True
    )
    # --- Interface de discussion interactive ---
    print("\n=== Chat interactif avec l'agent MCP ===")
    print("Tapez 'quit' ou 'exit' pour quitter\n")
    
    while True:
        try:
            # Demander à l'utilisateur de saisir une question
            user_input = input("Vous: ").strip()
            
            # Vérifier si l'utilisateur veut quitter
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Au revoir !")
                break
            
            # Ignorer les entrées vides
            if not user_input:
                continue
            
            print("\nAgent: ", end="", flush=True)
            
            # Utiliser le streaming pour afficher la réponse en temps réel
            async for chunk in agent.astream(user_input):
                # Les chunks peuvent contenir 'messages' ou 'output'
                out = chunk.get("messages") or chunk.get("output")
                if out:
                    # Affiche sans saut de ligne supplémentaire
                    print(out, end="", flush=True)
            
            print("\n")  # Nouvelle ligne après la réponse complète
            
        except KeyboardInterrupt:
            print("\n\nInterruption détectée. Au revoir !")
            break
        except Exception as e:
            print(f"\nErreur: {e}")
            continue

if __name__ == "__main__":
    # 6) S’assurer que Python utilise UTF-8 en sortie
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    asyncio.run(main())
