from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.PermissionsModel import PermissionsModel
from schemas.PermissionsSchema import PermissionsSchema
from services.PermissionsServices import PermissionsServices

permissions_router = APIRouter()

@permissions_router.get('/permissions', tags=['Permissions'], response_model=List[PermissionsSchema], status_code=200)
def getPermissions() -> List[PermissionsSchema]:

    db = Session()
    result = PermissionsServices(db).getPermissions()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@permissions_router.get('/permissions/{id}', tags=['Permissions'], response_model=PermissionsSchema)
def getPermissions(id: int) -> PermissionsSchema:

    db = Session()
    result = PermissionsServices(db).getPermissions()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@permissions_router.post('/permissions', tags=['Permissions'], response_model=dict, status_code=201)
def createPermissions(permissionsSchema: PermissionsSchema) -> dict:

    db = Session()
    PermissionsServices(db).createPermissions(permissionsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@permissions_router.put('/permissions/{id}', tags=['Permissions'], response_model=dict, status_code=200)
def updatePermissions(id: int, permissionsSchema: PermissionsSchema)-> dict:

    db = Session()
    result = PermissionsServices(db).getPermissions(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    PermissionsServices(db).updatePermissions(id, permissionsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@permissions_router.delete('/permissions/{id}', tags=['Permissions'], response_model=dict, status_code=200)
def deletePermissions(id: int)-> dict:

    db = Session()
    result: PermissionsModel = db.query(PermissionsModel).filter(PermissionsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    PermissionsServices(db).deletePermissions(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
