from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.dataFlowformatsModel import dataFlowformatsModel
from schemas.dataFlowformatsSchema import dataFlowformatsSchema
from services.dataFlowformatsServices import dataFlowformatsServices

dataFlowformats_router = APIRouter()

@dataFlowformats_router.get('/dataflowformats', tags=['dataFlowformats'], response_model=List[dataFlowformatsSchema], status_code=200)
def getdataFlowformats() -> List[dataFlowformatsSchema]:

    db = Session()
    result = dataFlowformatsServices(db).getdataFlowformats()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@dataFlowformats_router.get('/dataflowformats/{id}', tags=['dataFlowformats'], response_model=dataFlowformatsSchema)
def getdataFlowformats(id: int) -> dataFlowformatsSchema:

    db = Session()
    result = dataFlowformatsServices(db).getdataFlowformats()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@dataFlowformats_router.post('/dataflowformats', tags=['dataFlowformats'], response_model=dict, status_code=201)
def createdataFlowformats(dataFlowformatsSchema: dataFlowformatsSchema) -> dict:

    db = Session()
    dataFlowformatsServices(db).createdataFlowformats(dataFlowformatsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@dataFlowformats_router.put('/dataflowformats/{id}', tags=['dataFlowformats'], response_model=dict, status_code=200)
def updatedataFlowformats(id: int, dataFlowformatsSchema: dataFlowformatsSchema)-> dict:

    db = Session()
    result = dataFlowformatsServices(db).getdataFlowformats(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    dataFlowformatsServices(db).updatedataFlowformats(id, dataFlowformatsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@dataFlowformats_router.delete('/dataflowformats/{id}', tags=['dataFlowformats'], response_model=dict, status_code=200)
def deletedataFlowformats(id: int)-> dict:

    db = Session()
    result: dataFlowformatsModel = db.query(dataFlowformatsModel).filter(dataFlowformatsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    dataFlowformatsServices(db).deletedataFlowformats(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
