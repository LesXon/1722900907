from models.RouteNamesModel import RouteNamesModel
from schemas.RouteNamesSchema import RouteNamesSchema

class RouteNamesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getRouteNames(self):
      result = self.db.query(RouteNamesModel).all()
      return result

    def getRouteName(self, id):
      result = self.db.query(RouteNamesModel).filter(RouteNamesModel.id == id).first()
      return result

    def createRouteNames(self, routenamesSchema: RouteNamesSchema):
      routeNamesModel = RouteNamesModel(**routenamesSchema.dict())
      self.db.add(routeNamesModel)
      self.db.commit()
      return

    def deleteRouteNames(self, id: int):
      self.db.query(RouteNamesModel).filter(RouteNamesModel.id == id).delete()
      self.db.commit()
      return

    def updateRouteNames(self, id: int, data: RouteNamesSchema):
      routeNames = self.db.query(RouteNamesModel).filter(RouteNamesModel.id == id).first()
      routeNames.name = data.name
