from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.NavigationBarsModel import NavigationBarsModel
from schemas.NavigationBarsSchema import NavigationBarsSchema
from services.NavigationBarsServices import NavigationBarsServices

navigationBars_router = APIRouter()

@navigationBars_router.get('/navigationbars', tags=['NavigationBars'], response_model=List[NavigationBarsSchema], status_code=200)
def getNavigationBars() -> List[NavigationBarsSchema]:

    db = Session()
    result = NavigationBarsServices(db).getNavigationBars()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@navigationBars_router.get('/navigationbars/{id}', tags=['NavigationBars'], response_model=NavigationBarsSchema)
def getNavigationBars(id: int) -> NavigationBarsSchema:

    db = Session()
    result = NavigationBarsServices(db).getNavigationBars()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@navigationBars_router.post('/navigationbars', tags=['NavigationBars'], response_model=dict, status_code=201)
def createNavigationBars(navigationBarsSchema: NavigationBarsSchema) -> dict:

    db = Session()
    NavigationBarsServices(db).createNavigationBars(navigationBarsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@navigationBars_router.put('/navigationbars/{id}', tags=['NavigationBars'], response_model=dict, status_code=200)
def updateNavigationBars(id: int, navigationBarsSchema: NavigationBarsSchema)-> dict:

    db = Session()
    result = NavigationBarsServices(db).getNavigationBars(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    NavigationBarsServices(db).updateNavigationBars(id, navigationBarsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@navigationBars_router.delete('/navigationbars/{id}', tags=['NavigationBars'], response_model=dict, status_code=200)
def deleteNavigationBars(id: int)-> dict:

    db = Session()
    result: NavigationBarsModel = db.query(NavigationBarsModel).filter(NavigationBarsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    NavigationBarsServices(db).deleteNavigationBars(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
