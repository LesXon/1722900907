from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.DataDictionariesModel import DataDictionariesModel
from schemas.DataDictionariesSchema import DataDictionariesSchema
from services.DataDictionariesServices import DataDictionariesServices

dataDictionaries_router = APIRouter()

@dataDictionaries_router.get('/datadictionaries', tags=['DataDictionaries'], response_model=List[DataDictionariesSchema], status_code=200)
def getDataDictionaries() -> List[DataDictionariesSchema]:

    db = Session()
    result = DataDictionariesServices(db).getDataDictionaries()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@dataDictionaries_router.get('/datadictionaries/{id}', tags=['DataDictionaries'], response_model=DataDictionariesSchema)
def getDataDictionaries(id: int) -> DataDictionariesSchema:

    db = Session()
    result = DataDictionariesServices(db).getDataDictionaries()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@dataDictionaries_router.post('/datadictionaries', tags=['DataDictionaries'], response_model=dict, status_code=201)
def createDataDictionaries(dataDictionariesSchema: DataDictionariesSchema) -> dict:

    db = Session()
    DataDictionariesServices(db).createDataDictionaries(dataDictionariesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@dataDictionaries_router.put('/datadictionaries/{id}', tags=['DataDictionaries'], response_model=dict, status_code=200)
def updateDataDictionaries(id: int, dataDictionariesSchema: DataDictionariesSchema)-> dict:

    db = Session()
    result = DataDictionariesServices(db).getDataDictionaries(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DataDictionariesServices(db).updateDataDictionaries(id, dataDictionariesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@dataDictionaries_router.delete('/datadictionaries/{id}', tags=['DataDictionaries'], response_model=dict, status_code=200)
def deleteDataDictionaries(id: int)-> dict:

    db = Session()
    result: DataDictionariesModel = db.query(DataDictionariesModel).filter(DataDictionariesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DataDictionariesServices(db).deleteDataDictionaries(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
