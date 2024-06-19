import { GetWarehouses } from "./components/GetWarehouses"

function App() {
  return (
    <>
    <h1> Warehouses </h1>
    <GetWarehouses/>
    <form>
        <input type="submit" value="New Warehouse" />
    </form>
    <br/>
    <h1> Shelves </h1>
    <form>
        <label>
            Name:
            <input type="text" name="name" />
        </label>
        <br/>
        <label>
            Warehouse:
            <input type="text" name="warehouse" />
        </label>
        <br/>
        <label>
            Zone:
            <input type="text" name="zone" />
        </label>
        <input type="submit" value="Submit" />
    </form>
    </>
  )
}

export default App
