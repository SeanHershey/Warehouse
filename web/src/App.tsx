import { useState } from "react";
import { GetShelves } from "./components/GetShelves"
import { useLazyQuery, gql, useMutation } from '@apollo/client';


const CREATE_WAREHOUSE = gql`
    {createWarehouse{id}}
`;

const CREATE_SHELF = gql`
    mutation Shelf($name: String!, $zone: Int!, $warehouse: Int!) {
        createShelf(name:$name, zone:$zone, warehouse:$warehouse) {
            id message}}
`;

function App() {
    const [createWarehouse, {}] = useLazyQuery(CREATE_WAREHOUSE);
    
    const [formState, setFormState] = useState({
        name: '',
        zone: '',
        warehouse: ''
    });

    const [createLink] = useMutation(CREATE_SHELF, {
        variables: {
            name: formState.name,
            zone: Number(formState.zone),
            warehouse: Number(formState.warehouse)
        }
    });

    return (
        <>
        <h1> Warehouses </h1>
        <GetShelves/>
        <form>
            <input type="submit"
                   value="New Warehouse"
                   onClick={() => createWarehouse()}/>
        </form>
        
        <br/>

        <h1> Shelves </h1>
        <form onSubmit={(e) => {
                e.preventDefault();
                createLink();}}>
            <label>
                Name:
                <input type="text"
                       name="name"
                       id="name"
                       onChange={(e) =>
                            setFormState({
                            ...formState,
                            name: e.target.value
                            })
                       }/>
            </label>
            <br/>
            <label>
                Warehouse:
                <input type="text"
                       name="warehouse"
                       id="warehouse"
                       onChange={(e) =>
                            setFormState({
                            ...formState,
                            zone: e.target.value
                            })
                       }/>
            </label>
            <br/>
            <label>
                Zone:
                <input type="text"
                       name="zone"
                       id="zone"
                       onChange={(e) =>
                            setFormState({
                            ...formState,
                            zone: e.target.value
                            })
                       }/>
            </label>
            <input type="submit" value="Submit"/>
        </form>
        </>
    )
}

export default App
