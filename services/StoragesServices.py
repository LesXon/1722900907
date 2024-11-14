from models.StoragesModel import StoragesModel
from schemas.StoragesSchema import StoragesSchema

class StoragesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getStorages(self):
      result = self.db.query(StoragesModel).all()
      return result

    def getStorage(self, id):
      result = self.db.query(StoragesModel).filter(StoragesModel.id == id).first()
      return result

    def createStorages(self, storagesSchema: StoragesSchema):
      storagesModel = StoragesModel(**storagesSchema.dict())
      self.db.add(storagesModel)
      self.db.commit()
      return

    def deleteStorages(self, id: int):
      self.db.query(StoragesModel).filter(StoragesModel.id == id).delete()
      self.db.commit()
      return

    def updateStorages(self, id: int, data: StoragesSchema):
      storages = self.db.query(StoragesModel).filter(StoragesModel.id == id).first()
      storages.name = data.name
