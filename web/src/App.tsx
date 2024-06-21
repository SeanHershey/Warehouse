import { GetShelves } from "./components/GetShelves"
import CreateWarehouse from "./components/CreateWarehouse";
import CreateShelf from "./components/CreateShelf";
import { GetStatus } from "./components/GetStatus";
import Reset from "./components/Reset";
import "./App.css"

function App() {
    return (
        <div className="float-container">
            <div className="float-child">
                <div id="shelves">
                    <GetShelves/>
                    <CreateWarehouse/>
                </div>
            </div>
            <div className="float-child">
                <div id="new">
                    <CreateShelf/>
                    <GetStatus/>
                    <Reset/>
                </div>
            </div>
        </div>
    )
}

export default App