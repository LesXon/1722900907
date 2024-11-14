from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.SocialNetworksModel import SocialNetworksModel
from schemas.SocialNetworksSchema import SocialNetworksSchema
from services.SocialNetworksServices import SocialNetworksServices

socialNetworks_router = APIRouter()

@socialNetworks_router.get('/socialnetworks', tags=['SocialNetworks'], response_model=List[SocialNetworksSchema], status_code=200)
def getSocialNetworks() -> List[SocialNetworksSchema]:

    db = Session()
    result = SocialNetworksServices(db).getSocialNetworks()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@socialNetworks_router.get('/socialnetworks/{id}', tags=['SocialNetworks'], response_model=SocialNetworksSchema)
def getSocialNetworks(id: int) -> SocialNetworksSchema:

    db = Session()
    result = SocialNetworksServices(db).getSocialNetworks()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@socialNetworks_router.post('/socialnetworks', tags=['SocialNetworks'], response_model=dict, status_code=201)
def createSocialNetworks(socialNetworksSchema: SocialNetworksSchema) -> dict:

    db = Session()
    SocialNetworksServices(db).createSocialNetworks(socialNetworksSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@socialNetworks_router.put('/socialnetworks/{id}', tags=['SocialNetworks'], response_model=dict, status_code=200)
def updateSocialNetworks(id: int, socialNetworksSchema: SocialNetworksSchema)-> dict:

    db = Session()
    result = SocialNetworksServices(db).getSocialNetworks(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SocialNetworksServices(db).updateSocialNetworks(id, socialNetworksSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@socialNetworks_router.delete('/socialnetworks/{id}', tags=['SocialNetworks'], response_model=dict, status_code=200)
def deleteSocialNetworks(id: int)-> dict:

    db = Session()
    result: SocialNetworksModel = db.query(SocialNetworksModel).filter(SocialNetworksModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    SocialNetworksServices(db).deleteSocialNetworks(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
