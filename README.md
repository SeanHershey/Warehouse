# Warehouse
An application that allows its employees to keep track of its physical inventory.
Able to define the layout of a warehouse.
Then associate an item’s storage shelf with a physical location.

Website - https://warehouse-app-lxap.onrender.com/

API - https://warehouse-pcmv.onrender.com/graphql

## Setup
Clone repository or download files

**Local Server Steps**
1. Open the server directory in VSCode
2. Create a .env file and populate it with the following (API keys omitted for security but given elsewhere)
    - POSTGRES_URI= ...
    - PYTHON_VERSION=3.11.4
    - API_KEY= ...
4. Create a virtual environment
    - Open the Command Palette (Ctrl+Shift+P)
    - Search for the Python: Create Environment command
    - Select environment type: Venv
    - Select an interpreter: Python version 3.11.4
    - Select install requirements from requirements.txt
5. Debug and Run code (Ctrl+Shift+D F5)
6. Access the site in the browser with the URL/graphql (Uvicorn running on: \<URL\>)

**Local Web Steps**
1. Open the web directory in VSCode
2. Create a new terminal (Ctrl+Shift+`)
3. Type and run: npm run dev
4. Access the site in the browser with the URL (Local: \<URL\>)
5. To point the web to the local server
    - In main.tsx change the ApolloClient URI
    - Update it to the local server URL from local server step 4 (Uvicorn running on: \<URL\>)
    - Don't forget to add the /graphql

## Stack

**Frontend**
- React
- TypeScript
- Apollo Client

**Backend**
- GraphQL
- FastAPI
- Postgres

**Deployment**
- Supabase
- Render
