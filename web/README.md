# Warehouse Website
A web application that allows its employees to keep track of its physical inventory.
Able to define the layout of a warehouse.
Then associate an item’s storage shelf with a physical location.

Website - https://warehouse-app-lxap.onrender.com/  
Contact - sean.p.hershey@gmail.com  

## Setup
1. Clone repository or download files
2. Open the web directory in a new VSCode window
3. Create a new terminal (Ctrl+Shift+`)
4. Type and run: npm install (download NodeJS if not already installed)
5. Type and run: npm run dev
6. Access the site in Chrome with the URL (Local: \<URL\>)
7. To point the web to the local server
    - In src/main.tsx change the ApolloClient URI
    - Update it to the local server URL from local server (URL/graphql)
    - Don't forget to add the /graphql

**Frontend**
- React
- TypeScript
- Apollo Client

Using Vite provided a minimal setup to get React + TypeScript working in Vite with HMR and some ESLint rules.  
I then added ApolloClient to send GraphQL queries and mutations.  
I created React components for GetShelves, CreateWarehouse, CreateShelf, GetStatus, and Reset.  
I did simple CSS styling for the App as a whole.  
