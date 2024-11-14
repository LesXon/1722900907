from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.ConstructionsTypesModel import ConstructionsTypesModel
from schemas.ConstructionsTypesSchema import ConstructionsTypesSchema
from services.ConstructionsTypesServices import ConstructionsTypesServices

constructionsTypes_router = APIRouter()

@constructionsTypes_router.get('/constructionstypes', tags=['ConstructionsTypes'], response_model=List[ConstructionsTypesSchema], status_code=200)
def getConstructionsTypes() -> List[ConstructionsTypesSchema]:

    db = Session()
    result = ConstructionsTypesServices(db).getConstructionsTypes()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@constructionsTypes_router.get('/constructionstypes/{id}', tags=['ConstructionsTypes'], response_model=ConstructionsTypesSchema)
def getConstructionsTypes(id: int) -> ConstructionsTypesSchema:

    db = Session()
    result = ConstructionsTypesServices(db).getConstructionsTypes()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@constructionsTypes_router.post('/constructionstypes', tags=['ConstructionsTypes'], response_model=dict, status_code=201)
def createConstructionsTypes(constructionsTypesSchema: ConstructionsTypesSchema) -> dict:

    db = Session()
    ConstructionsTypesServices(db).createConstructionsTypes(constructionsTypesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@constructionsTypes_router.put('/constructionstypes/{id}', tags=['ConstructionsTypes'], response_model=dict, status_code=200)
def updateConstructionsTypes(id: int, constructionsTypesSchema: ConstructionsTypesSchema)-> dict:

    db = Session()
    result = ConstructionsTypesServices(db).getConstructionsTypes(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    ConstructionsTypesServices(db).updateConstructionsTypes(id, constructionsTypesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@constructionsTypes_router.delete('/constructionstypes/{id}', tags=['ConstructionsTypes'], response_model=dict, status_code=200)
def deleteConstructionsTypes(id: int)-> dict:

    db = Session()
    result: ConstructionsTypesModel = db.query(ConstructionsTypesModel).filter(ConstructionsTypesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    ConstructionsTypesServices(db).deleteConstructionsTypes(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
