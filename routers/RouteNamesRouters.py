from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.RouteNamesModel import RouteNamesModel
from schemas.RouteNamesSchema import RouteNamesSchema
from services.RouteNamesServices import RouteNamesServices

routeNames_router = APIRouter()

@routeNames_router.get('/routenames', tags=['RouteNames'], response_model=List[RouteNamesSchema], status_code=200)
def getRouteNames() -> List[RouteNamesSchema]:

    db = Session()
    result = RouteNamesServices(db).getRouteNames()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@routeNames_router.get('/routenames/{id}', tags=['RouteNames'], response_model=RouteNamesSchema)
def getRouteNames(id: int) -> RouteNamesSchema:

    db = Session()
    result = RouteNamesServices(db).getRouteNames()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@routeNames_router.post('/routenames', tags=['RouteNames'], response_model=dict, status_code=201)
def createRouteNames(routeNamesSchema: RouteNamesSchema) -> dict:

    db = Session()
    RouteNamesServices(db).createRouteNames(routeNamesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@routeNames_router.put('/routenames/{id}', tags=['RouteNames'], response_model=dict, status_code=200)
def updateRouteNames(id: int, routeNamesSchema: RouteNamesSchema)-> dict:

    db = Session()
    result = RouteNamesServices(db).getRouteNames(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    RouteNamesServices(db).updateRouteNames(id, routeNamesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@routeNames_router.delete('/routenames/{id}', tags=['RouteNames'], response_model=dict, status_code=200)
def deleteRouteNames(id: int)-> dict:

    db = Session()
    result: RouteNamesModel = db.query(RouteNamesModel).filter(RouteNamesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    RouteNamesServices(db).deleteRouteNames(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
