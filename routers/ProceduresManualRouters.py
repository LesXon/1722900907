from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.ProceduresManualModel import ProceduresManualModel
from schemas.ProceduresManualSchema import ProceduresManualSchema
from services.ProceduresManualServices import ProceduresManualServices

proceduresManual_router = APIRouter()

@proceduresManual_router.get('/proceduresmanual', tags=['ProceduresManual'], response_model=List[ProceduresManualSchema], status_code=200)
def getProceduresManual() -> List[ProceduresManualSchema]:

    db = Session()
    result = ProceduresManualServices(db).getProceduresManual()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@proceduresManual_router.get('/proceduresmanual/{id}', tags=['ProceduresManual'], response_model=ProceduresManualSchema)
def getProceduresManual(id: int) -> ProceduresManualSchema:

    db = Session()
    result = ProceduresManualServices(db).getProceduresManual()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@proceduresManual_router.post('/proceduresmanual', tags=['ProceduresManual'], response_model=dict, status_code=201)
def createProceduresManual(proceduresManualSchema: ProceduresManualSchema) -> dict:

    db = Session()
    ProceduresManualServices(db).createProceduresManual(proceduresManualSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@proceduresManual_router.put('/proceduresmanual/{id}', tags=['ProceduresManual'], response_model=dict, status_code=200)
def updateProceduresManual(id: int, proceduresManualSchema: ProceduresManualSchema)-> dict:

    db = Session()
    result = ProceduresManualServices(db).getProceduresManual(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    ProceduresManualServices(db).updateProceduresManual(id, proceduresManualSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@proceduresManual_router.delete('/proceduresmanual/{id}', tags=['ProceduresManual'], response_model=dict, status_code=200)
def deleteProceduresManual(id: int)-> dict:

    db = Session()
    result: ProceduresManualModel = db.query(ProceduresManualModel).filter(ProceduresManualModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    ProceduresManualServices(db).deleteProceduresManual(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
