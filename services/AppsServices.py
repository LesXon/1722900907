from models.AppsModel import AppsModel
from schemas.AppsSchema import AppsSchema

class AppsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getApps(self):
      result = self.db.query(AppsModel).all()
      return result

    def getApp(self, id):
      result = self.db.query(AppsModel).filter(AppsModel.id == id).first()
      return result

    def createApps(self, appsSchema: AppsSchema):
      appsModel = AppsModel(**appsSchema.dict())
      self.db.add(appsModel)
      self.db.commit()
      return

    def deleteApps(self, id: int):
      self.db.query(AppsModel).filter(AppsModel.id == id).delete()
      self.db.commit()
      return

    def updateApps(self, id: int, data: AppsSchema):
      apps = self.db.query(AppsModel).filter(AppsModel.id == id).first()
      apps.name = data.name
