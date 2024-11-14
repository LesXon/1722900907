from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.EntitiesModel import EntitiesModel
from schemas.EntitiesSchema import EntitiesSchema
from services.EntitiesServices import EntitiesServices

entities_router = APIRouter()

@entities_router.get('/entities', tags=['Entities'], response_model=List[EntitiesSchema], status_code=200)
def getEntities() -> List[EntitiesSchema]:

    db = Session()
    result = EntitiesServices(db).getEntities()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@entities_router.get('/entities/{id}', tags=['Entities'], response_model=EntitiesSchema)
def getEntities(id: int) -> EntitiesSchema:

    db = Session()
    result = EntitiesServices(db).getEntities()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@entities_router.post('/entities', tags=['Entities'], response_model=dict, status_code=201)
def createEntities(entitiesSchema: EntitiesSchema) -> dict:

    db = Session()
    EntitiesServices(db).createEntities(entitiesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@entities_router.put('/entities/{id}', tags=['Entities'], response_model=dict, status_code=200)
def updateEntities(id: int, entitiesSchema: EntitiesSchema)-> dict:

    db = Session()
    result = EntitiesServices(db).getEntities(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    EntitiesServices(db).updateEntities(id, entitiesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@entities_router.delete('/entities/{id}', tags=['Entities'], response_model=dict, status_code=200)
def deleteEntities(id: int)-> dict:

    db = Session()
    result: EntitiesModel = db.query(EntitiesModel).filter(EntitiesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    EntitiesServices(db).deleteEntities(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
