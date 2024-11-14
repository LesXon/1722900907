from models.NavigationBarsTypesModel import NavigationBarsTypesModel
from schemas.NavigationBarsTypesSchema import NavigationBarsTypesSchema

class NavigationBarsTypesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getNavigationBarsTypes(self):
      result = self.db.query(NavigationBarsTypesModel).all()
      return result

    def getNavigationBarsType(self, id):
      result = self.db.query(NavigationBarsTypesModel).filter(NavigationBarsTypesModel.id == id).first()
      return result

    def createNavigationBarsTypes(self, navigationbarstypesSchema: NavigationBarsTypesSchema):
      navigationBarsTypesModel = NavigationBarsTypesModel(**navigationbarstypesSchema.dict())
      self.db.add(navigationBarsTypesModel)
      self.db.commit()
      return

    def deleteNavigationBarsTypes(self, id: int):
      self.db.query(NavigationBarsTypesModel).filter(NavigationBarsTypesModel.id == id).delete()
      self.db.commit()
      return

    def updateNavigationBarsTypes(self, id: int, data: NavigationBarsTypesSchema):
      navigationBarsTypes = self.db.query(NavigationBarsTypesModel).filter(NavigationBarsTypesModel.id == id).first()
      navigationBarsTypes.name = data.name
