from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.AddressesTypesModel import AddressesTypesModel
from schemas.AddressesTypesSchema import AddressesTypesSchema
from services.AddressesTypesServices import AddressesTypesServices

addressesTypes_router = APIRouter()

@addressesTypes_router.get('/addressestypes', tags=['AddressesTypes'], response_model=List[AddressesTypesSchema], status_code=200)
def getAddressesTypes() -> List[AddressesTypesSchema]:

    db = Session()
    result = AddressesTypesServices(db).getAddressesTypes()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@addressesTypes_router.get('/addressestypes/{id}', tags=['AddressesTypes'], response_model=AddressesTypesSchema)
def getAddressesTypes(id: int) -> AddressesTypesSchema:

    db = Session()
    result = AddressesTypesServices(db).getAddressesTypes()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@addressesTypes_router.post('/addressestypes', tags=['AddressesTypes'], response_model=dict, status_code=201)
def createAddressesTypes(addressesTypesSchema: AddressesTypesSchema) -> dict:

    db = Session()
    AddressesTypesServices(db).createAddressesTypes(addressesTypesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@addressesTypes_router.put('/addressestypes/{id}', tags=['AddressesTypes'], response_model=dict, status_code=200)
def updateAddressesTypes(id: int, addressesTypesSchema: AddressesTypesSchema)-> dict:

    db = Session()
    result = AddressesTypesServices(db).getAddressesTypes(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AddressesTypesServices(db).updateAddressesTypes(id, addressesTypesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@addressesTypes_router.delete('/addressestypes/{id}', tags=['AddressesTypes'], response_model=dict, status_code=200)
def deleteAddressesTypes(id: int)-> dict:

    db = Session()
    result: AddressesTypesModel = db.query(AddressesTypesModel).filter(AddressesTypesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AddressesTypesServices(db).deleteAddressesTypes(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
