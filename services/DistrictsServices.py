from models.DistrictsModel import DistrictsModel
from schemas.DistrictsSchema import DistrictsSchema

class DistrictsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getDistricts(self):
      result = self.db.query(DistrictsModel).all()
      return result

    def getDistrict(self, id):
      result = self.db.query(DistrictsModel).filter(DistrictsModel.id == id).first()
      return result

    def createDistricts(self, districtsSchema: DistrictsSchema):
      districtsModel = DistrictsModel(**districtsSchema.dict())
      self.db.add(districtsModel)
      self.db.commit()
      return

    def deleteDistricts(self, id: int):
      self.db.query(DistrictsModel).filter(DistrictsModel.id == id).delete()
      self.db.commit()
      return

    def updateDistricts(self, id: int, data: DistrictsSchema):
      districts = self.db.query(DistrictsModel).filter(DistrictsModel.id == id).first()
      districts.name = data.name
