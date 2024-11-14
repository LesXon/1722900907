from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.PositionsModel import PositionsModel
from schemas.PositionsSchema import PositionsSchema
from services.PositionsServices import PositionsServices

positions_router = APIRouter()

@positions_router.get('/positions', tags=['Positions'], response_model=List[PositionsSchema], status_code=200)
def getPositions() -> List[PositionsSchema]:

    db = Session()
    result = PositionsServices(db).getPositions()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@positions_router.get('/positions/{id}', tags=['Positions'], response_model=PositionsSchema)
def getPositions(id: int) -> PositionsSchema:

    db = Session()
    result = PositionsServices(db).getPositions()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@positions_router.post('/positions', tags=['Positions'], response_model=dict, status_code=201)
def createPositions(positionsSchema: PositionsSchema) -> dict:

    db = Session()
    PositionsServices(db).createPositions(positionsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@positions_router.put('/positions/{id}', tags=['Positions'], response_model=dict, status_code=200)
def updatePositions(id: int, positionsSchema: PositionsSchema)-> dict:

    db = Session()
    result = PositionsServices(db).getPositions(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    PositionsServices(db).updatePositions(id, positionsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@positions_router.delete('/positions/{id}', tags=['Positions'], response_model=dict, status_code=200)
def deletePositions(id: int)-> dict:

    db = Session()
    result: PositionsModel = db.query(PositionsModel).filter(PositionsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    PositionsServices(db).deletePositions(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
