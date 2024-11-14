from models.PositionsModel import PositionsModel
from schemas.PositionsSchema import PositionsSchema

class PositionsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getPositions(self):
      result = self.db.query(PositionsModel).all()
      return result

    def getPosition(self, id):
      result = self.db.query(PositionsModel).filter(PositionsModel.id == id).first()
      return result

    def createPositions(self, positionsSchema: PositionsSchema):
      positionsModel = PositionsModel(**positionsSchema.dict())
      self.db.add(positionsModel)
      self.db.commit()
      return

    def deletePositions(self, id: int):
      self.db.query(PositionsModel).filter(PositionsModel.id == id).delete()
      self.db.commit()
      return

    def updatePositions(self, id: int, data: PositionsSchema):
      positions = self.db.query(PositionsModel).filter(PositionsModel.id == id).first()
      positions.name = data.name
