from models.AddressesTypesModel import AddressesTypesModel
from schemas.AddressesTypesSchema import AddressesTypesSchema

class AddressesTypesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getAddressesTypes(self):
      result = self.db.query(AddressesTypesModel).all()
      return result

    def getAddressesType(self, id):
      result = self.db.query(AddressesTypesModel).filter(AddressesTypesModel.id == id).first()
      return result

    def createAddressesTypes(self, addressestypesSchema: AddressesTypesSchema):
      addressesTypesModel = AddressesTypesModel(**addressestypesSchema.dict())
      self.db.add(addressesTypesModel)
      self.db.commit()
      return

    def deleteAddressesTypes(self, id: int):
      self.db.query(AddressesTypesModel).filter(AddressesTypesModel.id == id).delete()
      self.db.commit()
      return

    def updateAddressesTypes(self, id: int, data: AddressesTypesSchema):
      addressesTypes = self.db.query(AddressesTypesModel).filter(AddressesTypesModel.id == id).first()
      addressesTypes.name = data.name
