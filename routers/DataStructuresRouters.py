from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.DataStructuresModel import DataStructuresModel
from schemas.DataStructuresSchema import DataStructuresSchema
from services.DataStructuresServices import DataStructuresServices

dataStructures_router = APIRouter()

@dataStructures_router.get('/datastructures', tags=['DataStructures'], response_model=List[DataStructuresSchema], status_code=200)
def getDataStructures() -> List[DataStructuresSchema]:

    db = Session()
    result = DataStructuresServices(db).getDataStructures()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@dataStructures_router.get('/datastructures/{id}', tags=['DataStructures'], response_model=DataStructuresSchema)
def getDataStructures(id: int) -> DataStructuresSchema:

    db = Session()
    result = DataStructuresServices(db).getDataStructures()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@dataStructures_router.post('/datastructures', tags=['DataStructures'], response_model=dict, status_code=201)
def createDataStructures(dataStructuresSchema: DataStructuresSchema) -> dict:

    db = Session()
    DataStructuresServices(db).createDataStructures(dataStructuresSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@dataStructures_router.put('/datastructures/{id}', tags=['DataStructures'], response_model=dict, status_code=200)
def updateDataStructures(id: int, dataStructuresSchema: DataStructuresSchema)-> dict:

    db = Session()
    result = DataStructuresServices(db).getDataStructures(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DataStructuresServices(db).updateDataStructures(id, dataStructuresSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@dataStructures_router.delete('/datastructures/{id}', tags=['DataStructures'], response_model=dict, status_code=200)
def deleteDataStructures(id: int)-> dict:

    db = Session()
    result: DataStructuresModel = db.query(DataStructuresModel).filter(DataStructuresModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DataStructuresServices(db).deleteDataStructures(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
