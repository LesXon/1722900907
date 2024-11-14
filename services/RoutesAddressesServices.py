from models.RoutesAddressesModel import RoutesAddressesModel
from schemas.RoutesAddressesSchema import RoutesAddressesSchema

class RoutesAddressesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getRoutesAddresses(self):
      result = self.db.query(RoutesAddressesModel).all()
      return result

    def getRoutesAddresse(self, id):
      result = self.db.query(RoutesAddressesModel).filter(RoutesAddressesModel.id == id).first()
      return result

    def createRoutesAddresses(self, routesaddressesSchema: RoutesAddressesSchema):
      routesAddressesModel = RoutesAddressesModel(**routesaddressesSchema.dict())
      self.db.add(routesAddressesModel)
      self.db.commit()
      return

    def deleteRoutesAddresses(self, id: int):
      self.db.query(RoutesAddressesModel).filter(RoutesAddressesModel.id == id).delete()
      self.db.commit()
      return

    def updateRoutesAddresses(self, id: int, data: RoutesAddressesSchema):
      routesAddresses = self.db.query(RoutesAddressesModel).filter(RoutesAddressesModel.id == id).first()
      routesAddresses.name = data.name
