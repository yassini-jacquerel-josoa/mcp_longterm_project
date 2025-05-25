 
import httpx
import json
from src.mcp_clients.core.client import MCPUSE_CLIENT

_orig_headers_init = httpx.Headers.__init__
def _headers_init(self, headers=None, encoding=None, **kwargs):
    return _orig_headers_init(self, headers=headers, encoding="utf-8", **kwargs)
httpx.Headers.__init__ = _headers_init
 
with open("server_config.json") as f:
    config = json.load(f)
    print(f"Config: {config}")


async def run_terminal_client(): 
 
    agent = MCPUSE_CLIENT(config=config)


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

# if __name__ == "__main__":
#     # 6) S’assurer que Python utilise UTF-8 en sortie
#     os.environ.setdefault("PYTHONIOENCODING", "utf-8")
#     asyncio.run(main())
