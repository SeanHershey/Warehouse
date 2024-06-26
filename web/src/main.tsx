import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client';


const client = new ApolloClient({
    uri: 'https://warehouse-pcmv.onrender.com/graphql',
    cache: new InMemoryCache()
});

ReactDOM.createRoot(document.getElementById('root')!).render(
    <ApolloProvider client={client}>
    <App />
    </ApolloProvider>,
)