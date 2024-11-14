from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.FieldDescriptionFormatsModel import FieldDescriptionFormatsModel
from schemas.FieldDescriptionFormatsSchema import FieldDescriptionFormatsSchema
from services.FieldDescriptionFormatsServices import FieldDescriptionFormatsServices

fieldDescriptionFormats_router = APIRouter()

@fieldDescriptionFormats_router.get('/fielddescriptionformats', tags=['FieldDescriptionFormats'], response_model=List[FieldDescriptionFormatsSchema], status_code=200)
def getFieldDescriptionFormats() -> List[FieldDescriptionFormatsSchema]:

    db = Session()
    result = FieldDescriptionFormatsServices(db).getFieldDescriptionFormats()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@fieldDescriptionFormats_router.get('/fielddescriptionformats/{id}', tags=['FieldDescriptionFormats'], response_model=FieldDescriptionFormatsSchema)
def getFieldDescriptionFormats(id: int) -> FieldDescriptionFormatsSchema:

    db = Session()
    result = FieldDescriptionFormatsServices(db).getFieldDescriptionFormats()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@fieldDescriptionFormats_router.post('/fielddescriptionformats', tags=['FieldDescriptionFormats'], response_model=dict, status_code=201)
def createFieldDescriptionFormats(fieldDescriptionFormatsSchema: FieldDescriptionFormatsSchema) -> dict:

    db = Session()
    FieldDescriptionFormatsServices(db).createFieldDescriptionFormats(fieldDescriptionFormatsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@fieldDescriptionFormats_router.put('/fielddescriptionformats/{id}', tags=['FieldDescriptionFormats'], response_model=dict, status_code=200)
def updateFieldDescriptionFormats(id: int, fieldDescriptionFormatsSchema: FieldDescriptionFormatsSchema)-> dict:

    db = Session()
    result = FieldDescriptionFormatsServices(db).getFieldDescriptionFormats(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    FieldDescriptionFormatsServices(db).updateFieldDescriptionFormats(id, fieldDescriptionFormatsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@fieldDescriptionFormats_router.delete('/fielddescriptionformats/{id}', tags=['FieldDescriptionFormats'], response_model=dict, status_code=200)
def deleteFieldDescriptionFormats(id: int)-> dict:

    db = Session()
    result: FieldDescriptionFormatsModel = db.query(FieldDescriptionFormatsModel).filter(FieldDescriptionFormatsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    FieldDescriptionFormatsServices(db).deleteFieldDescriptionFormats(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
