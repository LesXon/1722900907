from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.AppMenusModel import AppMenusModel
from schemas.AppMenusSchema import AppMenusSchema
from services.AppMenusServices import AppMenusServices

appMenus_router = APIRouter()

@appMenus_router.get('/appmenus', tags=['AppMenus'], response_model=List[AppMenusSchema], status_code=200)
def getAppMenus() -> List[AppMenusSchema]:

    db = Session()
    result = AppMenusServices(db).getAppMenus()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@appMenus_router.get('/appmenus/{id}', tags=['AppMenus'], response_model=AppMenusSchema)
def getAppMenus(id: int) -> AppMenusSchema:

    db = Session()
    result = AppMenusServices(db).getAppMenus()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@appMenus_router.post('/appmenus', tags=['AppMenus'], response_model=dict, status_code=201)
def createAppMenus(appMenusSchema: AppMenusSchema) -> dict:

    db = Session()
    AppMenusServices(db).createAppMenus(appMenusSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@appMenus_router.put('/appmenus/{id}', tags=['AppMenus'], response_model=dict, status_code=200)
def updateAppMenus(id: int, appMenusSchema: AppMenusSchema)-> dict:

    db = Session()
    result = AppMenusServices(db).getAppMenus(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AppMenusServices(db).updateAppMenus(id, appMenusSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@appMenus_router.delete('/appmenus/{id}', tags=['AppMenus'], response_model=dict, status_code=200)
def deleteAppMenus(id: int)-> dict:

    db = Session()
    result: AppMenusModel = db.query(AppMenusModel).filter(AppMenusModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AppMenusServices(db).deleteAppMenus(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
