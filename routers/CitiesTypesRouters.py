from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.CitiesTypesModel import CitiesTypesModel
from schemas.CitiesTypesSchema import CitiesTypesSchema
from services.CitiesTypesServices import CitiesTypesServices

citiesTypes_router = APIRouter()

@citiesTypes_router.get('/citiestypes', tags=['CitiesTypes'], response_model=List[CitiesTypesSchema], status_code=200)
def getCitiesTypes() -> List[CitiesTypesSchema]:

    db = Session()
    result = CitiesTypesServices(db).getCitiesTypes()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@citiesTypes_router.get('/citiestypes/{id}', tags=['CitiesTypes'], response_model=CitiesTypesSchema)
def getCitiesTypes(id: int) -> CitiesTypesSchema:

    db = Session()
    result = CitiesTypesServices(db).getCitiesTypes()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@citiesTypes_router.post('/citiestypes', tags=['CitiesTypes'], response_model=dict, status_code=201)
def createCitiesTypes(citiesTypesSchema: CitiesTypesSchema) -> dict:

    db = Session()
    CitiesTypesServices(db).createCitiesTypes(citiesTypesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@citiesTypes_router.put('/citiestypes/{id}', tags=['CitiesTypes'], response_model=dict, status_code=200)
def updateCitiesTypes(id: int, citiesTypesSchema: CitiesTypesSchema)-> dict:

    db = Session()
    result = CitiesTypesServices(db).getCitiesTypes(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    CitiesTypesServices(db).updateCitiesTypes(id, citiesTypesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@citiesTypes_router.delete('/citiestypes/{id}', tags=['CitiesTypes'], response_model=dict, status_code=200)
def deleteCitiesTypes(id: int)-> dict:

    db = Session()
    result: CitiesTypesModel = db.query(CitiesTypesModel).filter(CitiesTypesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    CitiesTypesServices(db).deleteCitiesTypes(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
