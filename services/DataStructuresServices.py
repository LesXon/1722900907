from models.DataStructuresModel import DataStructuresModel
from schemas.DataStructuresSchema import DataStructuresSchema

class DataStructuresServices():

    def __init__(self, db) -> None:
      self.db = db

    def getDataStructures(self):
      result = self.db.query(DataStructuresModel).all()
      return result

    def getDataStructure(self, id):
      result = self.db.query(DataStructuresModel).filter(DataStructuresModel.id == id).first()
      return result

    def createDataStructures(self, datastructuresSchema: DataStructuresSchema):
      dataStructuresModel = DataStructuresModel(**datastructuresSchema.dict())
      self.db.add(dataStructuresModel)
      self.db.commit()
      return

    def deleteDataStructures(self, id: int):
      self.db.query(DataStructuresModel).filter(DataStructuresModel.id == id).delete()
      self.db.commit()
      return

    def updateDataStructures(self, id: int, data: DataStructuresSchema):
      dataStructures = self.db.query(DataStructuresModel).filter(DataStructuresModel.id == id).first()
      dataStructures.name = data.name
