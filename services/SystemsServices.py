from models.SystemsModel import SystemsModel
from schemas.SystemsSchema import SystemsSchema

class SystemsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getSystems(self):
      result = self.db.query(SystemsModel).all()
      return result

    def getSystem(self, id):
      result = self.db.query(SystemsModel).filter(SystemsModel.id == id).first()
      return result

    def createSystems(self, systemsSchema: SystemsSchema):
      systemsModel = SystemsModel(**systemsSchema.dict())
      self.db.add(systemsModel)
      self.db.commit()
      return

    def deleteSystems(self, id: int):
      self.db.query(SystemsModel).filter(SystemsModel.id == id).delete()
      self.db.commit()
      return

    def updateSystems(self, id: int, data: SystemsSchema):
      systems = self.db.query(SystemsModel).filter(SystemsModel.id == id).first()
      systems.name = data.name
