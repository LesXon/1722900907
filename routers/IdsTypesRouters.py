from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.IdsTypesModel import IdsTypesModel
from schemas.IdsTypesSchema import IdsTypesSchema
from services.IdsTypesServices import IdsTypesServices

idsTypes_router = APIRouter()

@idsTypes_router.get('/idstypes', tags=['IdsTypes'], response_model=List[IdsTypesSchema], status_code=200)
def getIdsTypes() -> List[IdsTypesSchema]:

    db = Session()
    result = IdsTypesServices(db).getIdsTypes()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@idsTypes_router.get('/idstypes/{id}', tags=['IdsTypes'], response_model=IdsTypesSchema)
def getIdsTypes(id: int) -> IdsTypesSchema:

    db = Session()
    result = IdsTypesServices(db).getIdsTypes()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@idsTypes_router.post('/idstypes', tags=['IdsTypes'], response_model=dict, status_code=201)
def createIdsTypes(idsTypesSchema: IdsTypesSchema) -> dict:

    db = Session()
    IdsTypesServices(db).createIdsTypes(idsTypesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@idsTypes_router.put('/idstypes/{id}', tags=['IdsTypes'], response_model=dict, status_code=200)
def updateIdsTypes(id: int, idsTypesSchema: IdsTypesSchema)-> dict:

    db = Session()
    result = IdsTypesServices(db).getIdsTypes(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    IdsTypesServices(db).updateIdsTypes(id, idsTypesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@idsTypes_router.delete('/idstypes/{id}', tags=['IdsTypes'], response_model=dict, status_code=200)
def deleteIdsTypes(id: int)-> dict:

    db = Session()
    result: IdsTypesModel = db.query(IdsTypesModel).filter(IdsTypesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    IdsTypesServices(db).deleteIdsTypes(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
