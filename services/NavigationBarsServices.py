from models.NavigationBarsModel import NavigationBarsModel
from schemas.NavigationBarsSchema import NavigationBarsSchema

class NavigationBarsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getNavigationBars(self):
      result = self.db.query(NavigationBarsModel).all()
      return result

    def getNavigationBar(self, id):
      result = self.db.query(NavigationBarsModel).filter(NavigationBarsModel.id == id).first()
      return result

    def createNavigationBars(self, navigationbarsSchema: NavigationBarsSchema):
      navigationBarsModel = NavigationBarsModel(**navigationbarsSchema.dict())
      self.db.add(navigationBarsModel)
      self.db.commit()
      return

    def deleteNavigationBars(self, id: int):
      self.db.query(NavigationBarsModel).filter(NavigationBarsModel.id == id).delete()
      self.db.commit()
      return

    def updateNavigationBars(self, id: int, data: NavigationBarsSchema):
      navigationBars = self.db.query(NavigationBarsModel).filter(NavigationBarsModel.id == id).first()
      navigationBars.name = data.name
