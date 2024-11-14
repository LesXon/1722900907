from models.AppMenusModel import AppMenusModel
from schemas.AppMenusSchema import AppMenusSchema

class AppMenusServices():

    def __init__(self, db) -> None:
      self.db = db

    def getAppMenus(self):
      result = self.db.query(AppMenusModel).all()
      return result

    def getAppMenu(self, id):
      result = self.db.query(AppMenusModel).filter(AppMenusModel.id == id).first()
      return result

    def createAppMenus(self, appmenusSchema: AppMenusSchema):
      appMenusModel = AppMenusModel(**appmenusSchema.dict())
      self.db.add(appMenusModel)
      self.db.commit()
      return

    def deleteAppMenus(self, id: int):
      self.db.query(AppMenusModel).filter(AppMenusModel.id == id).delete()
      self.db.commit()
      return

    def updateAppMenus(self, id: int, data: AppMenusSchema):
      appMenus = self.db.query(AppMenusModel).filter(AppMenusModel.id == id).first()
      appMenus.name = data.name
