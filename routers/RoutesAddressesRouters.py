from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.RoutesAddressesModel import RoutesAddressesModel
from schemas.RoutesAddressesSchema import RoutesAddressesSchema
from services.RoutesAddressesServices import RoutesAddressesServices

routesAddresses_router = APIRouter()

@routesAddresses_router.get('/routesaddresses', tags=['RoutesAddresses'], response_model=List[RoutesAddressesSchema], status_code=200)
def getRoutesAddresses() -> List[RoutesAddressesSchema]:

    db = Session()
    result = RoutesAddressesServices(db).getRoutesAddresses()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@routesAddresses_router.get('/routesaddresses/{id}', tags=['RoutesAddresses'], response_model=RoutesAddressesSchema)
def getRoutesAddresses(id: int) -> RoutesAddressesSchema:

    db = Session()
    result = RoutesAddressesServices(db).getRoutesAddresses()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@routesAddresses_router.post('/routesaddresses', tags=['RoutesAddresses'], response_model=dict, status_code=201)
def createRoutesAddresses(routesAddressesSchema: RoutesAddressesSchema) -> dict:

    db = Session()
    RoutesAddressesServices(db).createRoutesAddresses(routesAddressesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@routesAddresses_router.put('/routesaddresses/{id}', tags=['RoutesAddresses'], response_model=dict, status_code=200)
def updateRoutesAddresses(id: int, routesAddressesSchema: RoutesAddressesSchema)-> dict:

    db = Session()
    result = RoutesAddressesServices(db).getRoutesAddresses(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    RoutesAddressesServices(db).updateRoutesAddresses(id, routesAddressesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@routesAddresses_router.delete('/routesaddresses/{id}', tags=['RoutesAddresses'], response_model=dict, status_code=200)
def deleteRoutesAddresses(id: int)-> dict:

    db = Session()
    result: RoutesAddressesModel = db.query(RoutesAddressesModel).filter(RoutesAddressesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    RoutesAddressesServices(db).deleteRoutesAddresses(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
