from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.NavigationBarsTypesModel import NavigationBarsTypesModel
from schemas.NavigationBarsTypesSchema import NavigationBarsTypesSchema
from services.NavigationBarsTypesServices import NavigationBarsTypesServices

navigationBarsTypes_router = APIRouter()

@navigationBarsTypes_router.get('/navigationbarstypes', tags=['NavigationBarsTypes'], response_model=List[NavigationBarsTypesSchema], status_code=200)
def getNavigationBarsTypes() -> List[NavigationBarsTypesSchema]:

    db = Session()
    result = NavigationBarsTypesServices(db).getNavigationBarsTypes()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@navigationBarsTypes_router.get('/navigationbarstypes/{id}', tags=['NavigationBarsTypes'], response_model=NavigationBarsTypesSchema)
def getNavigationBarsTypes(id: int) -> NavigationBarsTypesSchema:

    db = Session()
    result = NavigationBarsTypesServices(db).getNavigationBarsTypes()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@navigationBarsTypes_router.post('/navigationbarstypes', tags=['NavigationBarsTypes'], response_model=dict, status_code=201)
def createNavigationBarsTypes(navigationBarsTypesSchema: NavigationBarsTypesSchema) -> dict:

    db = Session()
    NavigationBarsTypesServices(db).createNavigationBarsTypes(navigationBarsTypesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@navigationBarsTypes_router.put('/navigationbarstypes/{id}', tags=['NavigationBarsTypes'], response_model=dict, status_code=200)
def updateNavigationBarsTypes(id: int, navigationBarsTypesSchema: NavigationBarsTypesSchema)-> dict:

    db = Session()
    result = NavigationBarsTypesServices(db).getNavigationBarsTypes(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    NavigationBarsTypesServices(db).updateNavigationBarsTypes(id, navigationBarsTypesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@navigationBarsTypes_router.delete('/navigationbarstypes/{id}', tags=['NavigationBarsTypes'], response_model=dict, status_code=200)
def deleteNavigationBarsTypes(id: int)-> dict:

    db = Session()
    result: NavigationBarsTypesModel = db.query(NavigationBarsTypesModel).filter(NavigationBarsTypesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    NavigationBarsTypesServices(db).deleteNavigationBarsTypes(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
