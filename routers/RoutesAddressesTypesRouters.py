from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.RoutesAddressesTypesModel import RoutesAddressesTypesModel
from schemas.RoutesAddressesTypesSchema import RoutesAddressesTypesSchema
from services.RoutesAddressesTypesServices import RoutesAddressesTypesServices

routesAddressesTypes_router = APIRouter()

@routesAddressesTypes_router.get('/routesaddressestypes', tags=['RoutesAddressesTypes'], response_model=List[RoutesAddressesTypesSchema], status_code=200)
def getRoutesAddressesTypes() -> List[RoutesAddressesTypesSchema]:

    db = Session()
    result = RoutesAddressesTypesServices(db).getRoutesAddressesTypes()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@routesAddressesTypes_router.get('/routesaddressestypes/{id}', tags=['RoutesAddressesTypes'], response_model=RoutesAddressesTypesSchema)
def getRoutesAddressesTypes(id: int) -> RoutesAddressesTypesSchema:

    db = Session()
    result = RoutesAddressesTypesServices(db).getRoutesAddressesTypes()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@routesAddressesTypes_router.post('/routesaddressestypes', tags=['RoutesAddressesTypes'], response_model=dict, status_code=201)
def createRoutesAddressesTypes(routesAddressesTypesSchema: RoutesAddressesTypesSchema) -> dict:

    db = Session()
    RoutesAddressesTypesServices(db).createRoutesAddressesTypes(routesAddressesTypesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@routesAddressesTypes_router.put('/routesaddressestypes/{id}', tags=['RoutesAddressesTypes'], response_model=dict, status_code=200)
def updateRoutesAddressesTypes(id: int, routesAddressesTypesSchema: RoutesAddressesTypesSchema)-> dict:

    db = Session()
    result = RoutesAddressesTypesServices(db).getRoutesAddressesTypes(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    RoutesAddressesTypesServices(db).updateRoutesAddressesTypes(id, routesAddressesTypesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@routesAddressesTypes_router.delete('/routesaddressestypes/{id}', tags=['RoutesAddressesTypes'], response_model=dict, status_code=200)
def deleteRoutesAddressesTypes(id: int)-> dict:

    db = Session()
    result: RoutesAddressesTypesModel = db.query(RoutesAddressesTypesModel).filter(RoutesAddressesTypesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    RoutesAddressesTypesServices(db).deleteRoutesAddressesTypes(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
