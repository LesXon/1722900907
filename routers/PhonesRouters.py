from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.PhonesModel import PhonesModel
from schemas.PhonesSchema import PhonesSchema
from services.PhonesServices import PhonesServices

phones_router = APIRouter()

@phones_router.get('/phones', tags=['Phones'], response_model=List[PhonesSchema], status_code=200)
def getPhones() -> List[PhonesSchema]:

    db = Session()
    result = PhonesServices(db).getPhones()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@phones_router.get('/phones/{id}', tags=['Phones'], response_model=PhonesSchema)
def getPhones(id: int) -> PhonesSchema:

    db = Session()
    result = PhonesServices(db).getPhones()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@phones_router.post('/phones', tags=['Phones'], response_model=dict, status_code=201)
def createPhones(phonesSchema: PhonesSchema) -> dict:

    db = Session()
    PhonesServices(db).createPhones(phonesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@phones_router.put('/phones/{id}', tags=['Phones'], response_model=dict, status_code=200)
def updatePhones(id: int, phonesSchema: PhonesSchema)-> dict:

    db = Session()
    result = PhonesServices(db).getPhones(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    PhonesServices(db).updatePhones(id, phonesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@phones_router.delete('/phones/{id}', tags=['Phones'], response_model=dict, status_code=200)
def deletePhones(id: int)-> dict:

    db = Session()
    result: PhonesModel = db.query(PhonesModel).filter(PhonesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    PhonesServices(db).deletePhones(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
