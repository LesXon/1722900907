from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.DistrictsModel import DistrictsModel
from schemas.DistrictsSchema import DistrictsSchema
from services.DistrictsServices import DistrictsServices

districts_router = APIRouter()

@districts_router.get('/districts', tags=['Districts'], response_model=List[DistrictsSchema], status_code=200)
def getDistricts() -> List[DistrictsSchema]:

    db = Session()
    result = DistrictsServices(db).getDistricts()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@districts_router.get('/districts/{id}', tags=['Districts'], response_model=DistrictsSchema)
def getDistricts(id: int) -> DistrictsSchema:

    db = Session()
    result = DistrictsServices(db).getDistricts()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@districts_router.post('/districts', tags=['Districts'], response_model=dict, status_code=201)
def createDistricts(districtsSchema: DistrictsSchema) -> dict:

    db = Session()
    DistrictsServices(db).createDistricts(districtsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@districts_router.put('/districts/{id}', tags=['Districts'], response_model=dict, status_code=200)
def updateDistricts(id: int, districtsSchema: DistrictsSchema)-> dict:

    db = Session()
    result = DistrictsServices(db).getDistricts(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DistrictsServices(db).updateDistricts(id, districtsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@districts_router.delete('/districts/{id}', tags=['Districts'], response_model=dict, status_code=200)
def deleteDistricts(id: int)-> dict:

    db = Session()
    result: DistrictsModel = db.query(DistrictsModel).filter(DistrictsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DistrictsServices(db).deleteDistricts(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
