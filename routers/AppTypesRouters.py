from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.AppTypesModel import AppTypesModel
from schemas.AppTypesSchema import AppTypesSchema
from services.AppTypesServices import AppTypesServices

appTypes_router = APIRouter()

@appTypes_router.get('/apptypes', tags=['AppTypes'], response_model=List[AppTypesSchema], status_code=200)
def getAppTypes() -> List[AppTypesSchema]:

    db = Session()
    result = AppTypesServices(db).getAppTypes()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@appTypes_router.get('/apptypes/{id}', tags=['AppTypes'], response_model=AppTypesSchema)
def getAppTypes(id: int) -> AppTypesSchema:

    db = Session()
    result = AppTypesServices(db).getAppTypes()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@appTypes_router.post('/apptypes', tags=['AppTypes'], response_model=dict, status_code=201)
def createAppTypes(appTypesSchema: AppTypesSchema) -> dict:

    db = Session()
    AppTypesServices(db).createAppTypes(appTypesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@appTypes_router.put('/apptypes/{id}', tags=['AppTypes'], response_model=dict, status_code=200)
def updateAppTypes(id: int, appTypesSchema: AppTypesSchema)-> dict:

    db = Session()
    result = AppTypesServices(db).getAppTypes(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AppTypesServices(db).updateAppTypes(id, appTypesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@appTypes_router.delete('/apptypes/{id}', tags=['AppTypes'], response_model=dict, status_code=200)
def deleteAppTypes(id: int)-> dict:

    db = Session()
    result: AppTypesModel = db.query(AppTypesModel).filter(AppTypesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AppTypesServices(db).deleteAppTypes(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
