import { useState } from "react";
import { gql, useMutation } from '@apollo/client';


const CREATE_SHELF = gql`
    mutation Shelf($name: String!, $warehouse: Int!, $zone: Int!) {
        createShelf(name:$name, warehouse:$warehouse, zone:$zone) {
            id}}
`;

const CreateShelf = () => {
    const [formState, setFormState] = useState({
        name: '',
        warehouse: '',
        zone: ''
    });

    const [createLink] = useMutation(CREATE_SHELF, {
        variables: {
            name: formState.name,
            warehouse: Number(formState.warehouse),
            zone: Number(formState.zone)
        }
    });

    return (
        <>
        <h1> New Shelf </h1>
        <form onSubmit={(e) => {
                e.preventDefault();
                createLink();
                setTimeout(location.reload.bind(location), 200);}}>
            <label>
                Name
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
                Warehouse
                <input type="text"
                    name="warehouse"
                    id="warehouse"
                    onChange={(e) =>
                            setFormState({
                            ...formState,
                            warehouse: e.target.value
                            })
                    }/>
            </label>
            <br/>
            <label>
                Zone
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
            <input type="submit"
                    value="Submit"
                    id="submit"/>
        </form>
        </>
    );
};

export default CreateShelf;