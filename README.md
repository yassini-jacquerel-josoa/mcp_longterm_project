# MCP-Longterm-Project

## Description
Ce projet est une application MCP (Model-Client-Process) qui permet d'interagir avec différents services via un agent IA. Il comprend deux services principaux :
- **Service météo** : Permet d'obtenir les prévisions météorologiques et les alertes pour différentes zones géographiques aux États-Unis.
- **Service todo** : Permet de gérer une liste de tâches (ajout, consultation, suppression).

## Structure du Projet
```
mcp_longterm_project/
├── src/
│   ├── mcp_server/       # Serveurs MCP
│   │   ├── weather/      # Service météo
│   │   └── todo/         # Service de liste de tâches
│   └── mcp_client/       # Clients MCP
│       └── fastapi/      # Client FastAPI
├── tests/                # Tests unitaires
├── scripts/              # Scripts utilitaires
├── common/               # Modules communs
├── uploads/              # Dossier pour les fichiers uploadés
├── .env                  # Variables d'environnement (ne pas partager)
├── .env.exemple          # Exemple de fichier .env
├── config.json           # Configuration des serveurs MCP
├── main.py               # Point d'entrée principal
└── pyproject.toml        # Dépendances et configuration du projet
```

## Prérequis
- Python 3.11 ou supérieur
- Clé API OpenAI (à configurer dans le fichier .env)
- UV (gestionnaire de paquets Python moderne)

## Installation

1. Clonez le dépôt :
```bash
git clone [URL_DU_DEPOT]
cd mcp_longterm_project
```

2. Installez UV (si ce n'est pas déjà fait) :
```bash
pip install uv
```

3. Créez un environnement virtuel et activez-le avec UV :
```bash
uv venv
.\.venv\Scripts\activate
```

4. Installez les dépendances avec UV :
```bash
uv pip install -e .
```

5. Ou, pour installer spécifiquement les dépendances depuis pyproject.toml :
```bash
uv pip install --config pyproject.toml
```

6. Configurez le fichier .env :
```
OPENAI_API_KEY=votre_clé_api_openai
```

## Utilisation

### Démarrer les serveurs MCP
Les serveurs peuvent être démarrés via la configuration dans `config.json` :

```bash
uv run python src/mcp_server/weather/weather_server.py
uv run python src/mcp_server/todo/todo_server.py
```

### Utiliser le client terminal
Pour interagir avec les services via l'interface en ligne de commande :

```bash
python src/mcp_client/client.terminal.py
```

### Lancer l'application FastAPI
Pour démarrer l'interface web FastAPI :

```bash
uv run src/mcp_client/fastapi/app.py
```

## Fonctionnalités

### Service Météo
- `get_alerts(state)` : Obtenir les alertes météo pour un État américain (code à deux lettres)
- `get_forecast(latitude, longitude)` : Obtenir les prévisions météo pour des coordonnées géographiques

### Service Todo
- `add_todo(item)` : Ajouter une tâche à la liste
- `get_todos()` : Consulter toutes les tâches
- `remove_todo(item)` : Supprimer une tâche

## Technologies Utilisées
- **FastMCP** : Framework pour créer des serveurs MCP
- **Langchain** : Bibliothèque pour intégrer des LLM
- **OpenAI API** : Pour l'intelligence artificielle
- **FastAPI** : Pour l'API web (client)
- **httpx** : Client HTTP asynchrone
- **UV** : Gestionnaire de paquets Python moderne et rapide
```

### Lancer l'application FastAPI
Pour démarrer l'interface web FastAPI :

```bash
uv run src/mcp_client/fastapi/app.py
```
## Licence
[Spécifier la licence]
