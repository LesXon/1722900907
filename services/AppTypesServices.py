from models.AppTypesModel import AppTypesModel
from schemas.AppTypesSchema import AppTypesSchema

class AppTypesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getAppTypes(self):
      result = self.db.query(AppTypesModel).all()
      return result

    def getAppType(self, id):
      result = self.db.query(AppTypesModel).filter(AppTypesModel.id == id).first()
      return result

    def createAppTypes(self, apptypesSchema: AppTypesSchema):
      appTypesModel = AppTypesModel(**apptypesSchema.dict())
      self.db.add(appTypesModel)
      self.db.commit()
      return

    def deleteAppTypes(self, id: int):
      self.db.query(AppTypesModel).filter(AppTypesModel.id == id).delete()
      self.db.commit()
      return

    def updateAppTypes(self, id: int, data: AppTypesSchema):
      appTypes = self.db.query(AppTypesModel).filter(AppTypesModel.id == id).first()
      appTypes.name = data.name
