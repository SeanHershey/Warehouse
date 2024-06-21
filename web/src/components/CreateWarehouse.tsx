import { gql, useLazyQuery } from '@apollo/client';


const CREATE_WAREHOUSE = gql`
    {createWarehouse{id}}
`;

const CreateWarehouse = () => {
    const [createWarehouse] = useLazyQuery(CREATE_WAREHOUSE);

    return (
        <form>
            <input type="submit"
                value="New Warehouse"
                onClick={(e) => {
                        e.preventDefault();
                        createWarehouse();
                        setTimeout(location.reload.bind(location), 200);}}/>
        </form>
    );
};

export default CreateWarehouse;