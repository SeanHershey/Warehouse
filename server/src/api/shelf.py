from fastapi import APIRouter
import sqlalchemy
from src import database as db

router = APIRouter()

@router.post("/shelf/", tags=["shelf"])
def create_shelf(warehouse: int, name:str, zone:int):
    # Creates a new shelf

    with db.engine.begin() as connection:
        # a zone 1-12
        if zone < 1 or zone > 12:
            return {"error":"zone must be a number 1 through 12"}

        # zone not at capacity
        count = connection.execute(sqlalchemy.text(
            """
                SELECT count(zone) FROM shelves WHERE zone=:zone
            """), {"zone":zone}).scalar_one()
        if count >= 10:
            return {"error":"zone is at capacity of 10"}
        
        # insert
        id = connection.execute(sqlalchemy.text(
            """
                INSERT INTO shelves (id, warehouse, name, zone) VALUES(DEFAULT, :warehouse, :name, :zone) RETURNING id
            """),{"warehouse":warehouse, "name":name, "zone":zone}).scalar_one()

    return id


@router.get("/shelves/", tags=["shelf"])
def get_shelves():
    # Gets all shelves

    with db.engine.begin() as connection:
        result = connection.execute(sqlalchemy.text(
            """
                SELECT * FROM shelves
            """))

    json = []
    for item in result:
        json.append(
            {
                "id": item.id,
                "name": item.name,
                "zone": item.zone})

    return json