from models.NeighborhoodsModel import NeighborhoodsModel
from schemas.NeighborhoodsSchema import NeighborhoodsSchema

class NeighborhoodsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getNeighborhoods(self):
      result = self.db.query(NeighborhoodsModel).all()
      return result

    def getNeighborhood(self, id):
      result = self.db.query(NeighborhoodsModel).filter(NeighborhoodsModel.id == id).first()
      return result

    def createNeighborhoods(self, neighborhoodsSchema: NeighborhoodsSchema):
      neighborhoodsModel = NeighborhoodsModel(**neighborhoodsSchema.dict())
      self.db.add(neighborhoodsModel)
      self.db.commit()
      return

    def deleteNeighborhoods(self, id: int):
      self.db.query(NeighborhoodsModel).filter(NeighborhoodsModel.id == id).delete()
      self.db.commit()
      return

    def updateNeighborhoods(self, id: int, data: NeighborhoodsSchema):
      neighborhoods = self.db.query(NeighborhoodsModel).filter(NeighborhoodsModel.id == id).first()
      neighborhoods.name = data.name
