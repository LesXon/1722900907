from models.DistrictsTypesModel import DistrictsTypesModel
from schemas.DistrictsTypesSchema import DistrictsTypesSchema

class DistrictsTypesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getDistrictsTypes(self):
      result = self.db.query(DistrictsTypesModel).all()
      return result

    def getDistrictsType(self, id):
      result = self.db.query(DistrictsTypesModel).filter(DistrictsTypesModel.id == id).first()
      return result

    def createDistrictsTypes(self, districtstypesSchema: DistrictsTypesSchema):
      districtsTypesModel = DistrictsTypesModel(**districtstypesSchema.dict())
      self.db.add(districtsTypesModel)
      self.db.commit()
      return

    def deleteDistrictsTypes(self, id: int):
      self.db.query(DistrictsTypesModel).filter(DistrictsTypesModel.id == id).delete()
      self.db.commit()
      return

    def updateDistrictsTypes(self, id: int, data: DistrictsTypesSchema):
      districtsTypes = self.db.query(DistrictsTypesModel).filter(DistrictsTypesModel.id == id).first()
      districtsTypes.name = data.name
