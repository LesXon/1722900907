from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.FlowsModel import FlowsModel
from schemas.FlowsSchema import FlowsSchema
from services.FlowsServices import FlowsServices

flows_router = APIRouter()

@flows_router.get('/flows', tags=['Flows'], response_model=List[FlowsSchema], status_code=200)
def getFlows() -> List[FlowsSchema]:

    db = Session()
    result = FlowsServices(db).getFlows()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@flows_router.get('/flows/{id}', tags=['Flows'], response_model=FlowsSchema)
def getFlows(id: int) -> FlowsSchema:

    db = Session()
    result = FlowsServices(db).getFlows()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@flows_router.post('/flows', tags=['Flows'], response_model=dict, status_code=201)
def createFlows(flowsSchema: FlowsSchema) -> dict:

    db = Session()
    FlowsServices(db).createFlows(flowsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@flows_router.put('/flows/{id}', tags=['Flows'], response_model=dict, status_code=200)
def updateFlows(id: int, flowsSchema: FlowsSchema)-> dict:

    db = Session()
    result = FlowsServices(db).getFlows(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    FlowsServices(db).updateFlows(id, flowsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@flows_router.delete('/flows/{id}', tags=['Flows'], response_model=dict, status_code=200)
def deleteFlows(id: int)-> dict:

    db = Session()
    result: FlowsModel = db.query(FlowsModel).filter(FlowsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    FlowsServices(db).deleteFlows(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
