from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.DiagramsModel import DiagramsModel
from schemas.DiagramsSchema import DiagramsSchema
from services.DiagramsServices import DiagramsServices

diagrams_router = APIRouter()

@diagrams_router.get('/diagrams', tags=['Diagrams'], response_model=List[DiagramsSchema], status_code=200)
def getDiagrams() -> List[DiagramsSchema]:

    db = Session()
    result = DiagramsServices(db).getDiagrams()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@diagrams_router.get('/diagrams/{id}', tags=['Diagrams'], response_model=DiagramsSchema)
def getDiagrams(id: int) -> DiagramsSchema:

    db = Session()
    result = DiagramsServices(db).getDiagrams()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@diagrams_router.post('/diagrams', tags=['Diagrams'], response_model=dict, status_code=201)
def createDiagrams(diagramsSchema: DiagramsSchema) -> dict:

    db = Session()
    DiagramsServices(db).createDiagrams(diagramsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@diagrams_router.put('/diagrams/{id}', tags=['Diagrams'], response_model=dict, status_code=200)
def updateDiagrams(id: int, diagramsSchema: DiagramsSchema)-> dict:

    db = Session()
    result = DiagramsServices(db).getDiagrams(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DiagramsServices(db).updateDiagrams(id, diagramsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@diagrams_router.delete('/diagrams/{id}', tags=['Diagrams'], response_model=dict, status_code=200)
def deleteDiagrams(id: int)-> dict:

    db = Session()
    result: DiagramsModel = db.query(DiagramsModel).filter(DiagramsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    DiagramsServices(db).deleteDiagrams(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
