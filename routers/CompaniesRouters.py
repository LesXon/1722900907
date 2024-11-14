from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.CompaniesModel import CompaniesModel
from schemas.CompaniesSchema import CompaniesSchema
from services.CompaniesServices import CompaniesServices

companies_router = APIRouter()

@companies_router.get('/companies', tags=['Companies'], response_model=List[CompaniesSchema], status_code=200)
def getCompanies() -> List[CompaniesSchema]:

    db = Session()
    result = CompaniesServices(db).getCompanies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@companies_router.get('/companies/{id}', tags=['Companies'], response_model=CompaniesSchema)
def getCompanies(id: int) -> CompaniesSchema:

    db = Session()
    result = CompaniesServices(db).getCompanies()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@companies_router.post('/companies', tags=['Companies'], response_model=dict, status_code=201)
def createCompanies(companiesSchema: CompaniesSchema) -> dict:

    db = Session()
    CompaniesServices(db).createCompanies(companiesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@companies_router.put('/companies/{id}', tags=['Companies'], response_model=dict, status_code=200)
def updateCompanies(id: int, companiesSchema: CompaniesSchema)-> dict:

    db = Session()
    result = CompaniesServices(db).getCompanies(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    CompaniesServices(db).updateCompanies(id, companiesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@companies_router.delete('/companies/{id}', tags=['Companies'], response_model=dict, status_code=200)
def deleteCompanies(id: int)-> dict:

    db = Session()
    result: CompaniesModel = db.query(CompaniesModel).filter(CompaniesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    CompaniesServices(db).deleteCompanies(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
