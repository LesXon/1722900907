from models.AppMenusTypesModel import AppMenusTypesModel
from schemas.AppMenusTypesSchema import AppMenusTypesSchema

class AppMenusTypesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getAppMenusTypes(self):
      result = self.db.query(AppMenusTypesModel).all()
      return result

    def getAppMenusType(self, id):
      result = self.db.query(AppMenusTypesModel).filter(AppMenusTypesModel.id == id).first()
      return result

    def createAppMenusTypes(self, appmenustypesSchema: AppMenusTypesSchema):
      appMenusTypesModel = AppMenusTypesModel(**appmenustypesSchema.dict())
      self.db.add(appMenusTypesModel)
      self.db.commit()
      return

    def deleteAppMenusTypes(self, id: int):
      self.db.query(AppMenusTypesModel).filter(AppMenusTypesModel.id == id).delete()
      self.db.commit()
      return

    def updateAppMenusTypes(self, id: int, data: AppMenusTypesSchema):
      appMenusTypes = self.db.query(AppMenusTypesModel).filter(AppMenusTypesModel.id == id).first()
      appMenusTypes.name = data.name
