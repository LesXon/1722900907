from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.TypePositionsModel import TypePositionsModel
from schemas.TypePositionsSchema import TypePositionsSchema
from services.TypePositionsServices import TypePositionsServices

typePositions_router = APIRouter()

@typePositions_router.get('/typepositions', tags=['TypePositions'], response_model=List[TypePositionsSchema], status_code=200)
def getTypePositions() -> List[TypePositionsSchema]:

    db = Session()
    result = TypePositionsServices(db).getTypePositions()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@typePositions_router.get('/typepositions/{id}', tags=['TypePositions'], response_model=TypePositionsSchema)
def getTypePositions(id: int) -> TypePositionsSchema:

    db = Session()
    result = TypePositionsServices(db).getTypePositions()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@typePositions_router.post('/typepositions', tags=['TypePositions'], response_model=dict, status_code=201)
def createTypePositions(typePositionsSchema: TypePositionsSchema) -> dict:

    db = Session()
    TypePositionsServices(db).createTypePositions(typePositionsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@typePositions_router.put('/typepositions/{id}', tags=['TypePositions'], response_model=dict, status_code=200)
def updateTypePositions(id: int, typePositionsSchema: TypePositionsSchema)-> dict:

    db = Session()
    result = TypePositionsServices(db).getTypePositions(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    TypePositionsServices(db).updateTypePositions(id, typePositionsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@typePositions_router.delete('/typepositions/{id}', tags=['TypePositions'], response_model=dict, status_code=200)
def deleteTypePositions(id: int)-> dict:

    db = Session()
    result: TypePositionsModel = db.query(TypePositionsModel).filter(TypePositionsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    TypePositionsServices(db).deleteTypePositions(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
