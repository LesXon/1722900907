from models.ContinentsModel import ContinentsModel
from schemas.ContinentsSchema import ContinentsSchema

class ContinentsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getContinents(self):
      result = self.db.query(ContinentsModel).all()
      return result

    def getContinent(self, id):
      result = self.db.query(ContinentsModel).filter(ContinentsModel.id == id).first()
      return result

    def createContinents(self, continentsSchema: ContinentsSchema):
      continentsModel = ContinentsModel(**continentsSchema.dict())
      self.db.add(continentsModel)
      self.db.commit()
      return

    def deleteContinents(self, id: int):
      self.db.query(ContinentsModel).filter(ContinentsModel.id == id).delete()
      self.db.commit()
      return

    def updateContinents(self, id: int, data: ContinentsSchema):
      continents = self.db.query(ContinentsModel).filter(ContinentsModel.id == id).first()
      continents.name = data.name
