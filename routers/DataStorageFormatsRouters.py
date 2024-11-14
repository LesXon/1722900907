from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.DataStorageFormatsModel import DataStorageFormatsModel
from schemas.DataStorageFormatsSchema import DataStorageFormatsSchema
from services.DataStorageFormatsServices import DataStorageFormatsServices

dataStorageFormats_router = APIRouter()

@dataStorageFormats_router.get('/datastorageformats', tags=['DataStorageFormats'], response_model=List[DataStorageFormatsSchema], status_code=200)
def getDataStorageFormats() -> List[DataStorageFormatsSchema]:

    db = Session()
    result = DataStorageFormatsServices(db).getDataStorageFormats()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@dataStorageFormats_router.get('/datastorageformats/{id}', tags=['DataStorageFormats'], response_model=DataStorageFormatsSchema)
def getDataStorageFormats(id: int) -> DataStorageFormatsSchema:

    db = Session()
    result = DataStorageFormatsServices(db).getDataStorageFormats()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@dataStorageFormats_router.post('/datastorageformats', tags=['DataStorageFormats'], response_model=dict, status_code=201)
def createDataStorageFormats(dataStorageFormatsSchema: DataStorageFormatsSchema) -> dict:

    db = Session()
    DataStorageFormatsServices(db).createDataStorageFormats(dataStorageFormatsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@dataStorageFormats_router.put('/datastorageformats/{id}', tags=['DataStorageFormats'], response_model=dict, status_code=200)
def updateDataStorageFormats(id: int, dataStorageFormatsSchema: DataStorageFormatsSchema)-> dict:

    db = Session()
    result = DataStorageFormatsServices(db).getDataStorageFormats(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DataStorageFormatsServices(db).updateDataStorageFormats(id, dataStorageFormatsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@dataStorageFormats_router.delete('/datastorageformats/{id}', tags=['DataStorageFormats'], response_model=dict, status_code=200)
def deleteDataStorageFormats(id: int)-> dict:

    db = Session()
    result: DataStorageFormatsModel = db.query(DataStorageFormatsModel).filter(DataStorageFormatsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DataStorageFormatsServices(db).deleteDataStorageFormats(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
