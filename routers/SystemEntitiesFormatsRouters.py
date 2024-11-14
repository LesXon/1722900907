from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.SystemEntitiesFormatsModel import SystemEntitiesFormatsModel
from schemas.SystemEntitiesFormatsSchema import SystemEntitiesFormatsSchema
from services.SystemEntitiesFormatsServices import SystemEntitiesFormatsServices

systemEntitiesFormats_router = APIRouter()

@systemEntitiesFormats_router.get('/systementitiesformats', tags=['SystemEntitiesFormats'], response_model=List[SystemEntitiesFormatsSchema], status_code=200)
def getSystemEntitiesFormats() -> List[SystemEntitiesFormatsSchema]:

    db = Session()
    result = SystemEntitiesFormatsServices(db).getSystemEntitiesFormats()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@systemEntitiesFormats_router.get('/systementitiesformats/{id}', tags=['SystemEntitiesFormats'], response_model=SystemEntitiesFormatsSchema)
def getSystemEntitiesFormats(id: int) -> SystemEntitiesFormatsSchema:

    db = Session()
    result = SystemEntitiesFormatsServices(db).getSystemEntitiesFormats()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@systemEntitiesFormats_router.post('/systementitiesformats', tags=['SystemEntitiesFormats'], response_model=dict, status_code=201)
def createSystemEntitiesFormats(systemEntitiesFormatsSchema: SystemEntitiesFormatsSchema) -> dict:

    db = Session()
    SystemEntitiesFormatsServices(db).createSystemEntitiesFormats(systemEntitiesFormatsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@systemEntitiesFormats_router.put('/systementitiesformats/{id}', tags=['SystemEntitiesFormats'], response_model=dict, status_code=200)
def updateSystemEntitiesFormats(id: int, systemEntitiesFormatsSchema: SystemEntitiesFormatsSchema)-> dict:

    db = Session()
    result = SystemEntitiesFormatsServices(db).getSystemEntitiesFormats(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SystemEntitiesFormatsServices(db).updateSystemEntitiesFormats(id, systemEntitiesFormatsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@systemEntitiesFormats_router.delete('/systementitiesformats/{id}', tags=['SystemEntitiesFormats'], response_model=dict, status_code=200)
def deleteSystemEntitiesFormats(id: int)-> dict:

    db = Session()
    result: SystemEntitiesFormatsModel = db.query(SystemEntitiesFormatsModel).filter(SystemEntitiesFormatsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SystemEntitiesFormatsServices(db).deleteSystemEntitiesFormats(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
