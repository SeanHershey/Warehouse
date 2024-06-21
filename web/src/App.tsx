import { GetWarehouses } from "./components/GetWarehouses"
import { useLazyQuery, gql } from '@apollo/client';

const CREATE_WAREHOUSE = gql`
    {createWarehouse{id}}
`;

// const CREATE_SHELF = gql`
//     {createShelf(name:$name, zone:#zone,warehouse:$warehouse){id message} }
// `;

function App() {
  const [createWarehouse, {}] = useLazyQuery(CREATE_WAREHOUSE);
//   const [createShelf, {}] = useLazyQuery(CREATE_SHELF);
  return (
    <>
    <h1> Warehouses </h1>
    <GetWarehouses/>
    <form>
        <input type="submit" value="New Warehouse" onClick={() => createWarehouse()}/>
    </form>
    
    <br/>
    <h1> Shelves </h1>
    <form>
        <label>
            Name:
            <input type="text" name="name" id="name"/>
        </label>
        <br/>
        <label>
            Warehouse:
            <input type="text" name="warehouse"  id="warehouse"/>
        </label>
        <br/>
        <label>
            Zone:
            <input type="text" name="zone"  id="zone"/>
        </label>
        {/* <input type="submit" value="Submit" onClick={() => createShelf({ variables: { name:"test16", zone:2, warehouse:3 } })}/> */}
    </form>
    </>
  )
}

export default App
