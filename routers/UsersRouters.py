from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.UsersModel import UsersModel
from schemas.UsersSchema import UsersSchema
from services.UsersServices import UsersServices

users_router = APIRouter()

@users_router.get('/users', tags=['Users'], response_model=List[UsersSchema], status_code=200)
def getUsers() -> List[UsersSchema]:

    db = Session()
    result = UsersServices(db).getUsers()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@users_router.get('/users/{id}', tags=['Users'], response_model=UsersSchema)
def getUsers(id: int) -> UsersSchema:

    db = Session()
    result = UsersServices(db).getUsers()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@users_router.post('/users', tags=['Users'], response_model=dict, status_code=201)
def createUsers(usersSchema: UsersSchema) -> dict:

    db = Session()
    UsersServices(db).createUsers(usersSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@users_router.put('/users/{id}', tags=['Users'], response_model=dict, status_code=200)
def updateUsers(id: int, usersSchema: UsersSchema)-> dict:

    db = Session()
    result = UsersServices(db).getUsers(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    UsersServices(db).updateUsers(id, usersSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@users_router.delete('/users/{id}', tags=['Users'], response_model=dict, status_code=200)
def deleteUsers(id: int)-> dict:

    db = Session()
    result: UsersModel = db.query(UsersModel).filter(UsersModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    UsersServices(db).deleteUsers(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
