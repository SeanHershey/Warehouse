from fastapi import APIRouter
import sqlalchemy
from src import database as db

router = APIRouter()

@router.post("/warehouse/", tags=["warehouse"])
def create_warehouse():
    # Creates a new warehouse

    with db.engine.begin() as connection:
        id = connection.execute(sqlalchemy.text(
            """
                INSERT INTO warehouses (id) VALUES(DEFAULT) RETURNING id
            """)).scalar_one()

    return id


@router.get("/warehouses/", tags=["warehouse"])
def get_warehouses():
    # Gets all warehouse ids

    with db.engine.begin() as connection:
        result = connection.execute(sqlalchemy.text(
            """
                SELECT * FROM warehouses
            """))

    json = []
    for item in result:
        json.append(
            {
                "id": item.id})

    return json