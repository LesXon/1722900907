from models.RoutesAddressesTypesModel import RoutesAddressesTypesModel
from schemas.RoutesAddressesTypesSchema import RoutesAddressesTypesSchema

class RoutesAddressesTypesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getRoutesAddressesTypes(self):
      result = self.db.query(RoutesAddressesTypesModel).all()
      return result

    def getRoutesAddressesType(self, id):
      result = self.db.query(RoutesAddressesTypesModel).filter(RoutesAddressesTypesModel.id == id).first()
      return result

    def createRoutesAddressesTypes(self, routesaddressestypesSchema: RoutesAddressesTypesSchema):
      routesAddressesTypesModel = RoutesAddressesTypesModel(**routesaddressestypesSchema.dict())
      self.db.add(routesAddressesTypesModel)
      self.db.commit()
      return

    def deleteRoutesAddressesTypes(self, id: int):
      self.db.query(RoutesAddressesTypesModel).filter(RoutesAddressesTypesModel.id == id).delete()
      self.db.commit()
      return

    def updateRoutesAddressesTypes(self, id: int, data: RoutesAddressesTypesSchema):
      routesAddressesTypes = self.db.query(RoutesAddressesTypesModel).filter(RoutesAddressesTypesModel.id == id).first()
      routesAddressesTypes.name = data.name
