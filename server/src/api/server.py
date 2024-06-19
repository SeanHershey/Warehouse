from fastapi import FastAPI, exceptions
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from src.api import admin, warehouse, shelf
import json
import logging
import sys
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
    description="The `JSON` scalar type represents JSON values as specified by ECMA-404",
    serialize=lambda v: v,
    parse_value=lambda v: v,
)

@strawberry.type
class Warehouse:
    id: int

@strawberry.type
class Warehouses:
    results: JSON

@strawberry.type
class Query:
    @strawberry.field
    def warehouse(self) -> Warehouse:
        with db.engine.begin() as connection:
            id = connection.execute(sqlalchemy.text(
                """
                    INSERT INTO warehouses (id) VALUES(DEFAULT) RETURNING id
                """)).scalar_one()
        return Warehouse(id=id)
    
    @strawberry.field
    def warehouses(self) -> Warehouses:
        with db.engine.begin() as connection:
            results = connection.execute(sqlalchemy.text(
                """
                    SELECT name, zone, COALESCE(shelves.warehouse, warehouses.id) AS warehouse
                    FROM warehouses
                    FULL JOIN shelves ON shelves.warehouse = warehouses.id;
                """))

        json = []
        for item in results:
            json.append(
                {
                    "name": item.name,
                    "zone": item.zone,
                    "warehouse": item.warehouse})

        return Warehouses(results=json)

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

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
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