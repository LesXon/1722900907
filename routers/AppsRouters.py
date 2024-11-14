from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.AppsModel import AppsModel
from schemas.AppsSchema import AppsSchema
from services.AppsServices import AppsServices

apps_router = APIRouter()

@apps_router.get('/apps', tags=['Apps'], response_model=List[AppsSchema], status_code=200)
def getApps() -> List[AppsSchema]:

    db = Session()
    result = AppsServices(db).getApps()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@apps_router.get('/apps/{id}', tags=['Apps'], response_model=AppsSchema)
def getApps(id: int) -> AppsSchema:

    db = Session()
    result = AppsServices(db).getApps()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@apps_router.post('/apps', tags=['Apps'], response_model=dict, status_code=201)
def createApps(appsSchema: AppsSchema) -> dict:

    db = Session()
    AppsServices(db).createApps(appsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@apps_router.put('/apps/{id}', tags=['Apps'], response_model=dict, status_code=200)
def updateApps(id: int, appsSchema: AppsSchema)-> dict:

    db = Session()
    result = AppsServices(db).getApps(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AppsServices(db).updateApps(id, appsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@apps_router.delete('/apps/{id}', tags=['Apps'], response_model=dict, status_code=200)
def deleteApps(id: int)-> dict:

    db = Session()
    result: AppsModel = db.query(AppsModel).filter(AppsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AppsServices(db).deleteApps(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
