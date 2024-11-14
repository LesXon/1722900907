from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.StoragesModel import StoragesModel
from schemas.StoragesSchema import StoragesSchema
from services.StoragesServices import StoragesServices

storages_router = APIRouter()

@storages_router.get('/storages', tags=['Storages'], response_model=List[StoragesSchema], status_code=200)
def getStorages() -> List[StoragesSchema]:

    db = Session()
    result = StoragesServices(db).getStorages()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@storages_router.get('/storages/{id}', tags=['Storages'], response_model=StoragesSchema)
def getStorages(id: int) -> StoragesSchema:

    db = Session()
    result = StoragesServices(db).getStorages()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@storages_router.post('/storages', tags=['Storages'], response_model=dict, status_code=201)
def createStorages(storagesSchema: StoragesSchema) -> dict:

    db = Session()
    StoragesServices(db).createStorages(storagesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@storages_router.put('/storages/{id}', tags=['Storages'], response_model=dict, status_code=200)
def updateStorages(id: int, storagesSchema: StoragesSchema)-> dict:

    db = Session()
    result = StoragesServices(db).getStorages(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    StoragesServices(db).updateStorages(id, storagesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@storages_router.delete('/storages/{id}', tags=['Storages'], response_model=dict, status_code=200)
def deleteStorages(id: int)-> dict:

    db = Session()
    result: StoragesModel = db.query(StoragesModel).filter(StoragesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    StoragesServices(db).deleteStorages(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
