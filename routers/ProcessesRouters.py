from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.ProcessesModel import ProcessesModel
from schemas.ProcessesSchema import ProcessesSchema
from services.ProcessesServices import ProcessesServices

processes_router = APIRouter()

@processes_router.get('/processes', tags=['Processes'], response_model=List[ProcessesSchema], status_code=200)
def getProcesses() -> List[ProcessesSchema]:

    db = Session()
    result = ProcessesServices(db).getProcesses()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@processes_router.get('/processes/{id}', tags=['Processes'], response_model=ProcessesSchema)
def getProcesses(id: int) -> ProcessesSchema:

    db = Session()
    result = ProcessesServices(db).getProcesses()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@processes_router.post('/processes', tags=['Processes'], response_model=dict, status_code=201)
def createProcesses(processesSchema: ProcessesSchema) -> dict:

    db = Session()
    ProcessesServices(db).createProcesses(processesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@processes_router.put('/processes/{id}', tags=['Processes'], response_model=dict, status_code=200)
def updateProcesses(id: int, processesSchema: ProcessesSchema)-> dict:

    db = Session()
    result = ProcessesServices(db).getProcesses(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    ProcessesServices(db).updateProcesses(id, processesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@processes_router.delete('/processes/{id}', tags=['Processes'], response_model=dict, status_code=200)
def deleteProcesses(id: int)-> dict:

    db = Session()
    result: ProcessesModel = db.query(ProcessesModel).filter(ProcessesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    ProcessesServices(db).deleteProcesses(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
