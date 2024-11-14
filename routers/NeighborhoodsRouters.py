from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.NeighborhoodsModel import NeighborhoodsModel
from schemas.NeighborhoodsSchema import NeighborhoodsSchema
from services.NeighborhoodsServices import NeighborhoodsServices

neighborhoods_router = APIRouter()

@neighborhoods_router.get('/neighborhoods', tags=['Neighborhoods'], response_model=List[NeighborhoodsSchema], status_code=200)
def getNeighborhoods() -> List[NeighborhoodsSchema]:

    db = Session()
    result = NeighborhoodsServices(db).getNeighborhoods()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@neighborhoods_router.get('/neighborhoods/{id}', tags=['Neighborhoods'], response_model=NeighborhoodsSchema)
def getNeighborhoods(id: int) -> NeighborhoodsSchema:

    db = Session()
    result = NeighborhoodsServices(db).getNeighborhoods()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@neighborhoods_router.post('/neighborhoods', tags=['Neighborhoods'], response_model=dict, status_code=201)
def createNeighborhoods(neighborhoodsSchema: NeighborhoodsSchema) -> dict:

    db = Session()
    NeighborhoodsServices(db).createNeighborhoods(neighborhoodsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@neighborhoods_router.put('/neighborhoods/{id}', tags=['Neighborhoods'], response_model=dict, status_code=200)
def updateNeighborhoods(id: int, neighborhoodsSchema: NeighborhoodsSchema)-> dict:

    db = Session()
    result = NeighborhoodsServices(db).getNeighborhoods(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    NeighborhoodsServices(db).updateNeighborhoods(id, neighborhoodsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@neighborhoods_router.delete('/neighborhoods/{id}', tags=['Neighborhoods'], response_model=dict, status_code=200)
def deleteNeighborhoods(id: int)-> dict:

    db = Session()
    result: NeighborhoodsModel = db.query(NeighborhoodsModel).filter(NeighborhoodsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    NeighborhoodsServices(db).deleteNeighborhoods(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
