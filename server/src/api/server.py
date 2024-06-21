from fastapi import FastAPI, exceptions
from fastapi.responses import JSONResponse
from pydantic import ValidationError
import json
import logging
from starlette.middleware.cors import CORSMiddleware
import strawberry
from strawberry.asgi import GraphQL
from src import database as db
import sqlalchemy
from typing import Any, NewType

description = """
Warehouse is an application that allows its employees to keep track of its physical inventory
"""

def log(status):
    with db.engine.begin() as connection:
        connection.execute(sqlalchemy.text(
                """
                    INSERT INTO status_log (status) VALUES(:status)
                """), {"status":status})

JSON = strawberry.scalar(
    NewType("JSON", object),
    description="Scalar representing JSON values (ECMA-404)",
    serialize=lambda v: v,
    parse_value=lambda v: v,
)

@strawberry.type
class Warehouse:
    id: int

@strawberry.type
class Shelves:
    results: JSON

@strawberry.type
class Message:
    message: str

@strawberry.type
class Shelf:
    id: int

@strawberry.type
class Query:
    @strawberry.field
    def createWarehouse(self) -> Warehouse:
        with db.engine.begin() as connection:
            id = connection.execute(sqlalchemy.text(
                """
                    INSERT INTO warehouses (id) VALUES(DEFAULT) RETURNING id
                """)).scalar_one()
            
            log("Created warehouse " + str(id) + ".")
        
        return Warehouse(id=id)
    
    @strawberry.field
    def getShelves(self) -> Shelves:
        with db.engine.begin() as connection:
            results = connection.execute(sqlalchemy.text(
                """
                    SELECT name, zone, COALESCE(shelves.warehouse, warehouses.id) AS warehouse
                    FROM warehouses
                    FULL JOIN shelves ON shelves.warehouse = warehouses.id
                    ORDER BY warehouse;
                """))

        # build json from results
        json = []
        for item in results:
            json.append({
                "name": item.name,
                "zone": item.zone,
                "warehouse": item.warehouse})

        return Shelves(results=json)
    
    @strawberry.field
    def getStatus(self) -> Message:
        with db.engine.begin() as connection:
            message = connection.execute(sqlalchemy.text(
                """
                    SELECT status FROM status_log WHERE id IN (SELECT MAX(id) FROM status_log)
                """)).scalar_one()
        
        return Message(message=message)

    @strawberry.field
    def reset(self) -> Message:
        with db.engine.begin() as connection:
            connection.execute(sqlalchemy.text(
                """
                    TRUNCATE TABLE warehouses, shelves RESTART IDENTITY;
                """))
            
            log("Reset warehouse shelves.")
        
        return Message(message="Success")


@strawberry.type
class Mutation:
    @strawberry.mutation
    def createShelf(self, name:str, warehouse: int, zone:int) -> Shelf:
        with db.engine.begin() as connection:
            # valid name
            if not name:
                log("Please enter a valid name.")
                return Shelf(id=-1)

            # warehouse exists
            warehouses = connection.execute(sqlalchemy.text(
                """
                    SELECT id FROM warehouses
                """)).scalars()
            if warehouse not in warehouses:
                log("Please enter a valid warehouse.")
                return Shelf(id=-1)
            
            # zone is 1-12
            if zone < 1 or zone > 12:
                log("Please enter a zone number 1 through 12.")
                return Shelf(id=-1)

            # zone capacity
            count = connection.execute(sqlalchemy.text(
                """
                    SELECT count(zone) FROM shelves WHERE zone=:zone AND warehouse=:warehouse
                """), {"zone":zone, "warehouse":warehouse}).scalar_one()
            if count >= 10:
                log("Zone " + str(zone) + " is at capacity of 10, please try another zone.")
                return Shelf(id=-1)
            
            # insert shelf
            try:
                id = connection.execute(sqlalchemy.text(
                    """
                        INSERT INTO shelves (id, warehouse, name, zone) VALUES(DEFAULT, :warehouse, :name, :zone) RETURNING id
                    """),{"warehouse":warehouse, "name":name, "zone":zone}).scalar_one()
            # unique name
            except:
                log("Please provide a unique shelf name.")
                return Shelf(id=-1)
            
            log("Created shelf " + name + ".")

        return Shelf(id=id)


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQL(schema)

app = FastAPI(
    title="Warehouse",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Sean Hershey",
        "email": "shershey@calpoly.edu",
    },
)

origins = [
    "https://warehouse-app-lxap.onrender.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # dev (prod=origins)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.exception_handler(exceptions.RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    logging.error(f"The client sent invalid data!: {exc}")
    exc_json = json.loads(exc.json())
    response = {"message": [], "data": None}
    for error in exc_json:
        response['message'].append(f"{error['loc']}: {error['msg']}")

    return JSONResponse(response, status_code=422)

@app.get("/")
async def root():
    return {"message": "Welcome to Warehouse."}

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)