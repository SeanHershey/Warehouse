from fastapi import FastAPI, exceptions
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from src.api import admin, warehouse, shelf
import json
import logging
import sys
from starlette.middleware.cors import CORSMiddleware

description = """
Warehouse is an application that allows its employees to keep track of its physical inventory
"""

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
