from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.CellPhonesModel import CellPhonesModel
from schemas.CellPhonesSchema import CellPhonesSchema
from services.CellPhonesServices import CellPhonesServices

cellPhones_router = APIRouter()

@cellPhones_router.get('/cellphones', tags=['CellPhones'], response_model=List[CellPhonesSchema], status_code=200)
def getCellPhones() -> List[CellPhonesSchema]:

    db = Session()
    result = CellPhonesServices(db).getCellPhones()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@cellPhones_router.get('/cellphones/{id}', tags=['CellPhones'], response_model=CellPhonesSchema)
def getCellPhones(id: int) -> CellPhonesSchema:

    db = Session()
    result = CellPhonesServices(db).getCellPhones()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@cellPhones_router.post('/cellphones', tags=['CellPhones'], response_model=dict, status_code=201)
def createCellPhones(cellPhonesSchema: CellPhonesSchema) -> dict:

    db = Session()
    CellPhonesServices(db).createCellPhones(cellPhonesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@cellPhones_router.put('/cellphones/{id}', tags=['CellPhones'], response_model=dict, status_code=200)
def updateCellPhones(id: int, cellPhonesSchema: CellPhonesSchema)-> dict:

    db = Session()
    result = CellPhonesServices(db).getCellPhones(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    CellPhonesServices(db).updateCellPhones(id, cellPhonesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@cellPhones_router.delete('/cellphones/{id}', tags=['CellPhones'], response_model=dict, status_code=200)
def deleteCellPhones(id: int)-> dict:

    db = Session()
    result: CellPhonesModel = db.query(CellPhonesModel).filter(CellPhonesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    CellPhonesServices(db).deleteCellPhones(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
