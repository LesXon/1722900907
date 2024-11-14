from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.RolesModel import RolesModel
from schemas.RolesSchema import RolesSchema
from services.RolesServices import RolesServices

roles_router = APIRouter()

@roles_router.get('/roles', tags=['Roles'], response_model=List[RolesSchema], status_code=200)
def getRoles() -> List[RolesSchema]:

    db = Session()
    result = RolesServices(db).getRoles()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@roles_router.get('/roles/{id}', tags=['Roles'], response_model=RolesSchema)
def getRoles(id: int) -> RolesSchema:

    db = Session()
    result = RolesServices(db).getRoles()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@roles_router.post('/roles', tags=['Roles'], response_model=dict, status_code=201)
def createRoles(rolesSchema: RolesSchema) -> dict:

    db = Session()
    RolesServices(db).createRoles(rolesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@roles_router.put('/roles/{id}', tags=['Roles'], response_model=dict, status_code=200)
def updateRoles(id: int, rolesSchema: RolesSchema)-> dict:

    db = Session()
    result = RolesServices(db).getRoles(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    RolesServices(db).updateRoles(id, rolesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@roles_router.delete('/roles/{id}', tags=['Roles'], response_model=dict, status_code=200)
def deleteRoles(id: int)-> dict:

    db = Session()
    result: RolesModel = db.query(RolesModel).filter(RolesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    RolesServices(db).deleteRoles(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
