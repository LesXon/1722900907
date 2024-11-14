from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.SystemDataStructuresformatsModel import SystemDataStructuresformatsModel
from schemas.SystemDataStructuresformatsSchema import SystemDataStructuresformatsSchema
from services.SystemDataStructuresformatsServices import SystemDataStructuresformatsServices

systemDataStructuresformats_router = APIRouter()

@systemDataStructuresformats_router.get('/systemdatastructuresformats', tags=['SystemDataStructuresformats'], response_model=List[SystemDataStructuresformatsSchema], status_code=200)
def getSystemDataStructuresformats() -> List[SystemDataStructuresformatsSchema]:

    db = Session()
    result = SystemDataStructuresformatsServices(db).getSystemDataStructuresformats()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@systemDataStructuresformats_router.get('/systemdatastructuresformats/{id}', tags=['SystemDataStructuresformats'], response_model=SystemDataStructuresformatsSchema)
def getSystemDataStructuresformats(id: int) -> SystemDataStructuresformatsSchema:

    db = Session()
    result = SystemDataStructuresformatsServices(db).getSystemDataStructuresformats()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@systemDataStructuresformats_router.post('/systemdatastructuresformats', tags=['SystemDataStructuresformats'], response_model=dict, status_code=201)
def createSystemDataStructuresformats(systemDataStructuresformatsSchema: SystemDataStructuresformatsSchema) -> dict:

    db = Session()
    SystemDataStructuresformatsServices(db).createSystemDataStructuresformats(systemDataStructuresformatsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@systemDataStructuresformats_router.put('/systemdatastructuresformats/{id}', tags=['SystemDataStructuresformats'], response_model=dict, status_code=200)
def updateSystemDataStructuresformats(id: int, systemDataStructuresformatsSchema: SystemDataStructuresformatsSchema)-> dict:

    db = Session()
    result = SystemDataStructuresformatsServices(db).getSystemDataStructuresformats(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SystemDataStructuresformatsServices(db).updateSystemDataStructuresformats(id, systemDataStructuresformatsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@systemDataStructuresformats_router.delete('/systemdatastructuresformats/{id}', tags=['SystemDataStructuresformats'], response_model=dict, status_code=200)
def deleteSystemDataStructuresformats(id: int)-> dict:

    db = Session()
    result: SystemDataStructuresformatsModel = db.query(SystemDataStructuresformatsModel).filter(SystemDataStructuresformatsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SystemDataStructuresformatsServices(db).deleteSystemDataStructuresformats(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
