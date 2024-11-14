from models.SystemEntitiesFormatsModel import SystemEntitiesFormatsModel
from schemas.SystemEntitiesFormatsSchema import SystemEntitiesFormatsSchema

class SystemEntitiesFormatsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getSystemEntitiesFormats(self):
      result = self.db.query(SystemEntitiesFormatsModel).all()
      return result

    def getSystemEntitiesFormat(self, id):
      result = self.db.query(SystemEntitiesFormatsModel).filter(SystemEntitiesFormatsModel.id == id).first()
      return result

    def createSystemEntitiesFormats(self, systementitiesformatsSchema: SystemEntitiesFormatsSchema):
      systemEntitiesFormatsModel = SystemEntitiesFormatsModel(**systementitiesformatsSchema.dict())
      self.db.add(systemEntitiesFormatsModel)
      self.db.commit()
      return

    def deleteSystemEntitiesFormats(self, id: int):
      self.db.query(SystemEntitiesFormatsModel).filter(SystemEntitiesFormatsModel.id == id).delete()
      self.db.commit()
      return

    def updateSystemEntitiesFormats(self, id: int, data: SystemEntitiesFormatsSchema):
      systemEntitiesFormats = self.db.query(SystemEntitiesFormatsModel).filter(SystemEntitiesFormatsModel.id == id).first()
      systemEntitiesFormats.name = data.name
