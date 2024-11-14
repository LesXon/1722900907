from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.ContinentsModel import ContinentsModel
from schemas.ContinentsSchema import ContinentsSchema
from services.ContinentsServices import ContinentsServices

continents_router = APIRouter()

@continents_router.get('/continents', tags=['Continents'], response_model=List[ContinentsSchema], status_code=200)
def getContinents() -> List[ContinentsSchema]:

    db = Session()
    result = ContinentsServices(db).getContinents()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@continents_router.get('/continents/{id}', tags=['Continents'], response_model=ContinentsSchema)
def getContinents(id: int) -> ContinentsSchema:

    db = Session()
    result = ContinentsServices(db).getContinents()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@continents_router.post('/continents', tags=['Continents'], response_model=dict, status_code=201)
def createContinents(continentsSchema: ContinentsSchema) -> dict:

    db = Session()
    ContinentsServices(db).createContinents(continentsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@continents_router.put('/continents/{id}', tags=['Continents'], response_model=dict, status_code=200)
def updateContinents(id: int, continentsSchema: ContinentsSchema)-> dict:

    db = Session()
    result = ContinentsServices(db).getContinents(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    ContinentsServices(db).updateContinents(id, continentsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@continents_router.delete('/continents/{id}', tags=['Continents'], response_model=dict, status_code=200)
def deleteContinents(id: int)-> dict:

    db = Session()
    result: ContinentsModel = db.query(ContinentsModel).filter(ContinentsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    ContinentsServices(db).deleteContinents(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
