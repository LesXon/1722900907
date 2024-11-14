from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.SystemProcessesFormatsModel import SystemProcessesFormatsModel
from schemas.SystemProcessesFormatsSchema import SystemProcessesFormatsSchema
from services.SystemProcessesFormatsServices import SystemProcessesFormatsServices

systemProcessesFormats_router = APIRouter()

@systemProcessesFormats_router.get('/systemprocessesformats', tags=['SystemProcessesFormats'], response_model=List[SystemProcessesFormatsSchema], status_code=200)
def getSystemProcessesFormats() -> List[SystemProcessesFormatsSchema]:

    db = Session()
    result = SystemProcessesFormatsServices(db).getSystemProcessesFormats()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@systemProcessesFormats_router.get('/systemprocessesformats/{id}', tags=['SystemProcessesFormats'], response_model=SystemProcessesFormatsSchema)
def getSystemProcessesFormats(id: int) -> SystemProcessesFormatsSchema:

    db = Session()
    result = SystemProcessesFormatsServices(db).getSystemProcessesFormats()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@systemProcessesFormats_router.post('/systemprocessesformats', tags=['SystemProcessesFormats'], response_model=dict, status_code=201)
def createSystemProcessesFormats(systemProcessesFormatsSchema: SystemProcessesFormatsSchema) -> dict:

    db = Session()
    SystemProcessesFormatsServices(db).createSystemProcessesFormats(systemProcessesFormatsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@systemProcessesFormats_router.put('/systemprocessesformats/{id}', tags=['SystemProcessesFormats'], response_model=dict, status_code=200)
def updateSystemProcessesFormats(id: int, systemProcessesFormatsSchema: SystemProcessesFormatsSchema)-> dict:

    db = Session()
    result = SystemProcessesFormatsServices(db).getSystemProcessesFormats(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SystemProcessesFormatsServices(db).updateSystemProcessesFormats(id, systemProcessesFormatsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@systemProcessesFormats_router.delete('/systemprocessesformats/{id}', tags=['SystemProcessesFormats'], response_model=dict, status_code=200)
def deleteSystemProcessesFormats(id: int)-> dict:

    db = Session()
    result: SystemProcessesFormatsModel = db.query(SystemProcessesFormatsModel).filter(SystemProcessesFormatsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SystemProcessesFormatsServices(db).deleteSystemProcessesFormats(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
