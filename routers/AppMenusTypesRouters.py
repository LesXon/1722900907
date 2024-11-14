from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.AppMenusTypesModel import AppMenusTypesModel
from schemas.AppMenusTypesSchema import AppMenusTypesSchema
from services.AppMenusTypesServices import AppMenusTypesServices

appMenusTypes_router = APIRouter()

@appMenusTypes_router.get('/appmenustypes', tags=['AppMenusTypes'], response_model=List[AppMenusTypesSchema], status_code=200)
def getAppMenusTypes() -> List[AppMenusTypesSchema]:

    db = Session()
    result = AppMenusTypesServices(db).getAppMenusTypes()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@appMenusTypes_router.get('/appmenustypes/{id}', tags=['AppMenusTypes'], response_model=AppMenusTypesSchema)
def getAppMenusTypes(id: int) -> AppMenusTypesSchema:

    db = Session()
    result = AppMenusTypesServices(db).getAppMenusTypes()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@appMenusTypes_router.post('/appmenustypes', tags=['AppMenusTypes'], response_model=dict, status_code=201)
def createAppMenusTypes(appMenusTypesSchema: AppMenusTypesSchema) -> dict:

    db = Session()
    AppMenusTypesServices(db).createAppMenusTypes(appMenusTypesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@appMenusTypes_router.put('/appmenustypes/{id}', tags=['AppMenusTypes'], response_model=dict, status_code=200)
def updateAppMenusTypes(id: int, appMenusTypesSchema: AppMenusTypesSchema)-> dict:

    db = Session()
    result = AppMenusTypesServices(db).getAppMenusTypes(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AppMenusTypesServices(db).updateAppMenusTypes(id, appMenusTypesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@appMenusTypes_router.delete('/appmenustypes/{id}', tags=['AppMenusTypes'], response_model=dict, status_code=200)
def deleteAppMenusTypes(id: int)-> dict:

    db = Session()
    result: AppMenusTypesModel = db.query(AppMenusTypesModel).filter(AppMenusTypesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AppMenusTypesServices(db).deleteAppMenusTypes(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
