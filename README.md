# Warehouse
An application that allows its employees to keep track of its physical inventory.  
Able to define the layout of a warehouse.  
Then associate an item’s storage shelf with a physical location.  

Website - https://warehouse-app-lxap.onrender.com/  
API - https://warehouse-pcmv.onrender.com/graphql  
Contact - sean.p.hershey@gmail.com  

## Setup
Clone repository or download files

**Local Server Steps**
1. Open the server directory in VSCode
2. Create a .env file and populate it with the following (API keys omitted for security but given elsewhere)
    - POSTGRES_URI= ...
    - PYTHON_VERSION=3.11.4
    - API_KEY= ...
3. Create a virtual environment
    - Open the Command Palette (Ctrl+Shift+P)
    - Search for the Python: Create Environment command
    - Select environment type: Venv
    - Select an interpreter: Python version 3.11.4 (download if not already installed)
    - Select install requirements from requirements.txt
4. Run and Debug code (Ctrl+Shift+D F5)
5. Access the site in Chrome with the URL/graphql (Uvicorn running on: URL)

**Local Web Steps**
1. Open the web directory in a new VSCode window
2. Create a new terminal (Ctrl+Shift+`)
3. Type and run: npm install (download NodeJS if not already installed)
4. Type and run: npm run dev
5. Access the site in Chrome with the URL (Local: \<URL\>)
6. To point the web to the local server
    - In src/main.tsx change the ApolloClient URI
    - Update it to the local server URL from local server step 5 (URL/graphql)
    - Don't forget to add the /graphql

## Stack

**Frontend**
- React
- TypeScript
- Apollo Client

Using Vite provided a minimal setup to get React + TypeScript working in Vite with HMR and some ESLint rules.  
I then added ApolloClient to send GraphQL queries and mutations.  
I created React components for GetShelves, CreateWarehouse, CreateShelf, GetStatus, and Reset.  
I did simple CSS styling for the App as a whole.  

**Backend**
- GraphQL
- FastAPI
- Postgres

The backend is built on FastAPI.  
I used Strawberry for GraphQL classes, which made queries easy to represent.  
Then I ran Postgres SQL with SQLalchemy to the Supabase database (The schema can be found in schema.sql).  
CORS was handled using Starlette.  

**Deployment**
- Supabase
- Render

Supabase handles the database tables and a CRON job that keeps the sites up always accessible.  
Render hosts the API server and the website.  
