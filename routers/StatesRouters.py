from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.StatesModel import StatesModel
from schemas.StatesSchema import StatesSchema
from services.StatesServices import StatesServices

states_router = APIRouter()

@states_router.get('/states', tags=['States'], response_model=List[StatesSchema], status_code=200)
def getStates() -> List[StatesSchema]:

    db = Session()
    result = StatesServices(db).getStates()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@states_router.get('/states/{id}', tags=['States'], response_model=StatesSchema)
def getStates(id: int) -> StatesSchema:

    db = Session()
    result = StatesServices(db).getStates()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@states_router.post('/states', tags=['States'], response_model=dict, status_code=201)
def createStates(statesSchema: StatesSchema) -> dict:

    db = Session()
    StatesServices(db).createStates(statesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@states_router.put('/states/{id}', tags=['States'], response_model=dict, status_code=200)
def updateStates(id: int, statesSchema: StatesSchema)-> dict:

    db = Session()
    result = StatesServices(db).getStates(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    StatesServices(db).updateStates(id, statesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@states_router.delete('/states/{id}', tags=['States'], response_model=dict, status_code=200)
def deleteStates(id: int)-> dict:

    db = Session()
    result: StatesModel = db.query(StatesModel).filter(StatesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    StatesServices(db).deleteStates(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
