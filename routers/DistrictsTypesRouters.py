from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.DistrictsTypesModel import DistrictsTypesModel
from schemas.DistrictsTypesSchema import DistrictsTypesSchema
from services.DistrictsTypesServices import DistrictsTypesServices

districtsTypes_router = APIRouter()

@districtsTypes_router.get('/districtstypes', tags=['DistrictsTypes'], response_model=List[DistrictsTypesSchema], status_code=200)
def getDistrictsTypes() -> List[DistrictsTypesSchema]:

    db = Session()
    result = DistrictsTypesServices(db).getDistrictsTypes()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@districtsTypes_router.get('/districtstypes/{id}', tags=['DistrictsTypes'], response_model=DistrictsTypesSchema)
def getDistrictsTypes(id: int) -> DistrictsTypesSchema:

    db = Session()
    result = DistrictsTypesServices(db).getDistrictsTypes()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@districtsTypes_router.post('/districtstypes', tags=['DistrictsTypes'], response_model=dict, status_code=201)
def createDistrictsTypes(districtsTypesSchema: DistrictsTypesSchema) -> dict:

    db = Session()
    DistrictsTypesServices(db).createDistrictsTypes(districtsTypesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@districtsTypes_router.put('/districtstypes/{id}', tags=['DistrictsTypes'], response_model=dict, status_code=200)
def updateDistrictsTypes(id: int, districtsTypesSchema: DistrictsTypesSchema)-> dict:

    db = Session()
    result = DistrictsTypesServices(db).getDistrictsTypes(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DistrictsTypesServices(db).updateDistrictsTypes(id, districtsTypesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@districtsTypes_router.delete('/districtstypes/{id}', tags=['DistrictsTypes'], response_model=dict, status_code=200)
def deleteDistrictsTypes(id: int)-> dict:

    db = Session()
    result: DistrictsTypesModel = db.query(DistrictsTypesModel).filter(DistrictsTypesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DistrictsTypesServices(db).deleteDistrictsTypes(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
