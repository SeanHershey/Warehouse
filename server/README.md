# Warehouse Server
An API that allows its employees to get physical inventory.
Able to add new warehouses.
Then associate an item’s storage shelf with a physical location or zone.

API - https://warehouse-pcmv.onrender.com/graphql  
Contact - sean.p.hershey@gmail.com  

The backend is built on FastAPI.  
I used Strawberry for GraphQL classes, which made queries easy to represent.  
Then I ran Postgres SQL with SQLalchemy to the Supabase database (The schema can be found in schema.sql).  
CORS was handled using Starlette.  

## Setup
1. Clone repository or download files
2. Open the server directory in VSCode
3. Create a .env file and populate it with the following (API keys omitted for security but given elsewhere)
    - POSTGRES_URI= ...
    - PYTHON_VERSION=3.11.4
    - API_KEY= ...
4. Create a virtual environment
    - Open the Command Palette (Ctrl+Shift+P)
    - Search for the Python: Create Environment command
    - Select environment type: Venv
    - Select an interpreter: Python version 3.11.4 (download if not already installed)
    - Select install requirements from requirements.txt
5. Run and Debug code (Ctrl+Shift+D F5)
6. Access the site in Chrome with the URL/graphql (Uvicorn running on: URL)
