from models.EntitiesModel import EntitiesModel
from schemas.EntitiesSchema import EntitiesSchema

class EntitiesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getEntities(self):
      result = self.db.query(EntitiesModel).all()
      return result

    def getEntitie(self, id):
      result = self.db.query(EntitiesModel).filter(EntitiesModel.id == id).first()
      return result

    def createEntities(self, entitiesSchema: EntitiesSchema):
      entitiesModel = EntitiesModel(**entitiesSchema.dict())
      self.db.add(entitiesModel)
      self.db.commit()
      return

    def deleteEntities(self, id: int):
      self.db.query(EntitiesModel).filter(EntitiesModel.id == id).delete()
      self.db.commit()
      return

    def updateEntities(self, id: int, data: EntitiesSchema):
      entities = self.db.query(EntitiesModel).filter(EntitiesModel.id == id).first()
      entities.name = data.name
