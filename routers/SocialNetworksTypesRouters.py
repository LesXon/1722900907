from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.SocialNetworksTypesModel import SocialNetworksTypesModel
from schemas.SocialNetworksTypesSchema import SocialNetworksTypesSchema
from services.SocialNetworksTypesServices import SocialNetworksTypesServices

socialNetworksTypes_router = APIRouter()

@socialNetworksTypes_router.get('/socialnetworkstypes', tags=['SocialNetworksTypes'], response_model=List[SocialNetworksTypesSchema], status_code=200)
def getSocialNetworksTypes() -> List[SocialNetworksTypesSchema]:

    db = Session()
    result = SocialNetworksTypesServices(db).getSocialNetworksTypes()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@socialNetworksTypes_router.get('/socialnetworkstypes/{id}', tags=['SocialNetworksTypes'], response_model=SocialNetworksTypesSchema)
def getSocialNetworksTypes(id: int) -> SocialNetworksTypesSchema:

    db = Session()
    result = SocialNetworksTypesServices(db).getSocialNetworksTypes()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@socialNetworksTypes_router.post('/socialnetworkstypes', tags=['SocialNetworksTypes'], response_model=dict, status_code=201)
def createSocialNetworksTypes(socialNetworksTypesSchema: SocialNetworksTypesSchema) -> dict:

    db = Session()
    SocialNetworksTypesServices(db).createSocialNetworksTypes(socialNetworksTypesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@socialNetworksTypes_router.put('/socialnetworkstypes/{id}', tags=['SocialNetworksTypes'], response_model=dict, status_code=200)
def updateSocialNetworksTypes(id: int, socialNetworksTypesSchema: SocialNetworksTypesSchema)-> dict:

    db = Session()
    result = SocialNetworksTypesServices(db).getSocialNetworksTypes(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SocialNetworksTypesServices(db).updateSocialNetworksTypes(id, socialNetworksTypesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@socialNetworksTypes_router.delete('/socialnetworkstypes/{id}', tags=['SocialNetworksTypes'], response_model=dict, status_code=200)
def deleteSocialNetworksTypes(id: int)-> dict:

    db = Session()
    result: SocialNetworksTypesModel = db.query(SocialNetworksTypesModel).filter(SocialNetworksTypesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SocialNetworksTypesServices(db).deleteSocialNetworksTypes(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
