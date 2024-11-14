from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.SystemsModel import SystemsModel
from schemas.SystemsSchema import SystemsSchema
from services.SystemsServices import SystemsServices

systems_router = APIRouter()

@systems_router.get('/systems', tags=['Systems'], response_model=List[SystemsSchema], status_code=200)
def getSystems() -> List[SystemsSchema]:

    db = Session()
    result = SystemsServices(db).getSystems()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@systems_router.get('/systems/{id}', tags=['Systems'], response_model=SystemsSchema)
def getSystems(id: int) -> SystemsSchema:

    db = Session()
    result = SystemsServices(db).getSystems()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@systems_router.post('/systems', tags=['Systems'], response_model=dict, status_code=201)
def createSystems(systemsSchema: SystemsSchema) -> dict:

    db = Session()
    SystemsServices(db).createSystems(systemsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@systems_router.put('/systems/{id}', tags=['Systems'], response_model=dict, status_code=200)
def updateSystems(id: int, systemsSchema: SystemsSchema)-> dict:

    db = Session()
    result = SystemsServices(db).getSystems(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SystemsServices(db).updateSystems(id, systemsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@systems_router.delete('/systems/{id}', tags=['Systems'], response_model=dict, status_code=200)
def deleteSystems(id: int)-> dict:

    db = Session()
    result: SystemsModel = db.query(SystemsModel).filter(SystemsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SystemsServices(db).deleteSystems(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
