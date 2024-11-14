from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.systemFormatsModel import systemFormatsModel
from schemas.systemFormatsSchema import systemFormatsSchema
from services.systemFormatsServices import systemFormatsServices

systemFormats_router = APIRouter()

@systemFormats_router.get('/systemformats', tags=['systemFormats'], response_model=List[systemFormatsSchema], status_code=200)
def getsystemFormats() -> List[systemFormatsSchema]:

    db = Session()
    result = systemFormatsServices(db).getsystemFormats()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@systemFormats_router.get('/systemformats/{id}', tags=['systemFormats'], response_model=systemFormatsSchema)
def getsystemFormats(id: int) -> systemFormatsSchema:

    db = Session()
    result = systemFormatsServices(db).getsystemFormats()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@systemFormats_router.post('/systemformats', tags=['systemFormats'], response_model=dict, status_code=201)
def createsystemFormats(systemFormatsSchema: systemFormatsSchema) -> dict:

    db = Session()
    systemFormatsServices(db).createsystemFormats(systemFormatsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@systemFormats_router.put('/systemformats/{id}', tags=['systemFormats'], response_model=dict, status_code=200)
def updatesystemFormats(id: int, systemFormatsSchema: systemFormatsSchema)-> dict:

    db = Session()
    result = systemFormatsServices(db).getsystemFormats(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    systemFormatsServices(db).updatesystemFormats(id, systemFormatsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@systemFormats_router.delete('/systemformats/{id}', tags=['systemFormats'], response_model=dict, status_code=200)
def deletesystemFormats(id: int)-> dict:

    db = Session()
    result: systemFormatsModel = db.query(systemFormatsModel).filter(systemFormatsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    systemFormatsServices(db).deletesystemFormats(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
