from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.EmployeesModel import EmployeesModel
from schemas.EmployeesSchema import EmployeesSchema
from services.EmployeesServices import EmployeesServices

employees_router = APIRouter()

@employees_router.get('/employees', tags=['Employees'], response_model=List[EmployeesSchema], status_code=200)
def getEmployees() -> List[EmployeesSchema]:

    db = Session()
    result = EmployeesServices(db).getEmployees()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@employees_router.get('/employees/{id}', tags=['Employees'], response_model=EmployeesSchema)
def getEmployees(id: int) -> EmployeesSchema:

    db = Session()
    result = EmployeesServices(db).getEmployees()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@employees_router.post('/employees', tags=['Employees'], response_model=dict, status_code=201)
def createEmployees(employeesSchema: EmployeesSchema) -> dict:

    db = Session()
    EmployeesServices(db).createEmployees(employeesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@employees_router.put('/employees/{id}', tags=['Employees'], response_model=dict, status_code=200)
def updateEmployees(id: int, employeesSchema: EmployeesSchema)-> dict:

    db = Session()
    result = EmployeesServices(db).getEmployees(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    EmployeesServices(db).updateEmployees(id, employeesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@employees_router.delete('/employees/{id}', tags=['Employees'], response_model=dict, status_code=200)
def deleteEmployees(id: int)-> dict:

    db = Session()
    result: EmployeesModel = db.query(EmployeesModel).filter(EmployeesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    EmployeesServices(db).deleteEmployees(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
