from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.CitiesModel import CitiesModel
from schemas.CitiesSchema import CitiesSchema
from services.CitiesServices import CitiesServices

cities_router = APIRouter()

@cities_router.get('/cities', tags=['Cities'], response_model=List[CitiesSchema], status_code=200)
def getCities() -> List[CitiesSchema]:

    db = Session()
    result = CitiesServices(db).getCities()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@cities_router.get('/cities/{id}', tags=['Cities'], response_model=CitiesSchema)
def getCities(id: int) -> CitiesSchema:

    db = Session()
    result = CitiesServices(db).getCities()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@cities_router.post('/cities', tags=['Cities'], response_model=dict, status_code=201)
def createCities(citiesSchema: CitiesSchema) -> dict:

    db = Session()
    CitiesServices(db).createCities(citiesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@cities_router.put('/cities/{id}', tags=['Cities'], response_model=dict, status_code=200)
def updateCities(id: int, citiesSchema: CitiesSchema)-> dict:

    db = Session()
    result = CitiesServices(db).getCities(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    CitiesServices(db).updateCities(id, citiesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@cities_router.delete('/cities/{id}', tags=['Cities'], response_model=dict, status_code=200)
def deleteCities(id: int)-> dict:

    db = Session()
    result: CitiesModel = db.query(CitiesModel).filter(CitiesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    CitiesServices(db).deleteCities(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
