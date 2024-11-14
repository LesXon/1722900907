from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.CountriesModel import CountriesModel
from schemas.CountriesSchema import CountriesSchema
from services.CountriesServices import CountriesServices

countries_router = APIRouter()

@countries_router.get('/countries', tags=['Countries'], response_model=List[CountriesSchema], status_code=200)
def getCountries() -> List[CountriesSchema]:

    db = Session()
    result = CountriesServices(db).getCountries()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@countries_router.get('/countries/{id}', tags=['Countries'], response_model=CountriesSchema)
def getCountries(id: int) -> CountriesSchema:

    db = Session()
    result = CountriesServices(db).getCountries()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@countries_router.post('/countries', tags=['Countries'], response_model=dict, status_code=201)
def createCountries(countriesSchema: CountriesSchema) -> dict:

    db = Session()
    CountriesServices(db).createCountries(countriesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@countries_router.put('/countries/{id}', tags=['Countries'], response_model=dict, status_code=200)
def updateCountries(id: int, countriesSchema: CountriesSchema)-> dict:

    db = Session()
    result = CountriesServices(db).getCountries(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    CountriesServices(db).updateCountries(id, countriesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@countries_router.delete('/countries/{id}', tags=['Countries'], response_model=dict, status_code=200)
def deleteCountries(id: int)-> dict:

    db = Session()
    result: CountriesModel = db.query(CountriesModel).filter(CountriesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    CountriesServices(db).deleteCountries(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
