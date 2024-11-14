from models.DataDictionariesModel import DataDictionariesModel
from schemas.DataDictionariesSchema import DataDictionariesSchema

class DataDictionariesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getDataDictionaries(self):
      result = self.db.query(DataDictionariesModel).all()
      return result

    def getDataDictionarie(self, id):
      result = self.db.query(DataDictionariesModel).filter(DataDictionariesModel.id == id).first()
      return result

    def createDataDictionaries(self, datadictionariesSchema: DataDictionariesSchema):
      dataDictionariesModel = DataDictionariesModel(**datadictionariesSchema.dict())
      self.db.add(dataDictionariesModel)
      self.db.commit()
      return

    def deleteDataDictionaries(self, id: int):
      self.db.query(DataDictionariesModel).filter(DataDictionariesModel.id == id).delete()
      self.db.commit()
      return

    def updateDataDictionaries(self, id: int, data: DataDictionariesSchema):
      dataDictionaries = self.db.query(DataDictionariesModel).filter(DataDictionariesModel.id == id).first()
      dataDictionaries.name = data.name
