from fastapi import FastAPI, exceptions
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from src.api import admin, warehouse, shelf
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
class Shelf:
    id: int
    message: str

@strawberry.type
class Shelves:
    results: JSON

@strawberry.type
class Query:
    @strawberry.field
    def createWarehouse(self) -> Warehouse:
        with db.engine.begin() as connection:
            id = connection.execute(sqlalchemy.text(
                """
                    INSERT INTO warehouses (id) VALUES(DEFAULT) RETURNING id
                """)).scalar_one()
        
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
    def createShelf(self, warehouse: int, name:str, zone:int) -> Shelf:
        with db.engine.begin() as connection:
            # zone is 1-12
            if zone < 1 or zone > 12:
                return Shelf(id=-1, message="Please enter a zone number 1 through 12.")

            # zone capacity
            count = connection.execute(sqlalchemy.text(
                """
                    SELECT count(zone) FROM shelves WHERE zone=:zone
                """), {"zone":zone}).scalar_one()
            if count >= 10:
                return Shelf(id=-1, message="Zone is at capacity of 10, please try another zone.")
            
            # insert shelf
            try:
                id = connection.execute(sqlalchemy.text(
                    """
                        INSERT INTO shelves (id, warehouse, name, zone) VALUES(DEFAULT, :warehouse, :name, :zone) RETURNING id
                    """),{"warehouse":warehouse, "name":name, "zone":zone}).scalar_one()
            # unique name
            except:
                return Shelf(id=-1, message="Please provide a unique shelf name.")

        return Shelf(id=id, message="Success")

schema = strawberry.Schema(query=Query)

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

app.include_router(warehouse.router)
app.include_router(shelf.router)
app.include_router(admin.router)

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