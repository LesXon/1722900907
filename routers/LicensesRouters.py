from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.LicensesModel import LicensesModel
from schemas.LicensesSchema import LicensesSchema
from services.LicensesServices import LicensesServices

licenses_router = APIRouter()

@licenses_router.get('/licenses', tags=['Licenses'], response_model=List[LicensesSchema], status_code=200)
def getLicenses() -> List[LicensesSchema]:

    db = Session()
    result = LicensesServices(db).getLicenses()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@licenses_router.get('/licenses/{id}', tags=['Licenses'], response_model=LicensesSchema)
def getLicenses(id: int) -> LicensesSchema:

    db = Session()
    result = LicensesServices(db).getLicenses()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@licenses_router.post('/licenses', tags=['Licenses'], response_model=dict, status_code=201)
def createLicenses(licensesSchema: LicensesSchema) -> dict:

    db = Session()
    LicensesServices(db).createLicenses(licensesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@licenses_router.put('/licenses/{id}', tags=['Licenses'], response_model=dict, status_code=200)
def updateLicenses(id: int, licensesSchema: LicensesSchema)-> dict:

    db = Session()
    result = LicensesServices(db).getLicenses(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    LicensesServices(db).updateLicenses(id, licensesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@licenses_router.delete('/licenses/{id}', tags=['Licenses'], response_model=dict, status_code=200)
def deleteLicenses(id: int)-> dict:

    db = Session()
    result: LicensesModel = db.query(LicensesModel).filter(LicensesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    LicensesServices(db).deleteLicenses(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
