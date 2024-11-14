from models.SystemDataStructuresformatsModel import SystemDataStructuresformatsModel
from schemas.SystemDataStructuresformatsSchema import SystemDataStructuresformatsSchema

class SystemDataStructuresformatsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getSystemDataStructuresformats(self):
      result = self.db.query(SystemDataStructuresformatsModel).all()
      return result

    def getSystemDataStructuresformat(self, id):
      result = self.db.query(SystemDataStructuresformatsModel).filter(SystemDataStructuresformatsModel.id == id).first()
      return result

    def createSystemDataStructuresformats(self, systemdatastructuresformatsSchema: SystemDataStructuresformatsSchema):
      systemDataStructuresformatsModel = SystemDataStructuresformatsModel(**systemdatastructuresformatsSchema.dict())
      self.db.add(systemDataStructuresformatsModel)
      self.db.commit()
      return

    def deleteSystemDataStructuresformats(self, id: int):
      self.db.query(SystemDataStructuresformatsModel).filter(SystemDataStructuresformatsModel.id == id).delete()
      self.db.commit()
      return

    def updateSystemDataStructuresformats(self, id: int, data: SystemDataStructuresformatsSchema):
      systemDataStructuresformats = self.db.query(SystemDataStructuresformatsModel).filter(SystemDataStructuresformatsModel.id == id).first()
      systemDataStructuresformats.name = data.name
