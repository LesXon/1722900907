from models.DataStorageFormatsModel import DataStorageFormatsModel
from schemas.DataStorageFormatsSchema import DataStorageFormatsSchema

class DataStorageFormatsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getDataStorageFormats(self):
      result = self.db.query(DataStorageFormatsModel).all()
      return result

    def getDataStorageFormat(self, id):
      result = self.db.query(DataStorageFormatsModel).filter(DataStorageFormatsModel.id == id).first()
      return result

    def createDataStorageFormats(self, datastorageformatsSchema: DataStorageFormatsSchema):
      dataStorageFormatsModel = DataStorageFormatsModel(**datastorageformatsSchema.dict())
      self.db.add(dataStorageFormatsModel)
      self.db.commit()
      return

    def deleteDataStorageFormats(self, id: int):
      self.db.query(DataStorageFormatsModel).filter(DataStorageFormatsModel.id == id).delete()
      self.db.commit()
      return

    def updateDataStorageFormats(self, id: int, data: DataStorageFormatsSchema):
      dataStorageFormats = self.db.query(DataStorageFormatsModel).filter(DataStorageFormatsModel.id == id).first()
      dataStorageFormats.name = data.name
