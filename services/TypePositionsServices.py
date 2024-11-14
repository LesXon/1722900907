from models.TypePositionsModel import TypePositionsModel
from schemas.TypePositionsSchema import TypePositionsSchema

class TypePositionsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getTypePositions(self):
      result = self.db.query(TypePositionsModel).all()
      return result

    def getTypePosition(self, id):
      result = self.db.query(TypePositionsModel).filter(TypePositionsModel.id == id).first()
      return result

    def createTypePositions(self, typepositionsSchema: TypePositionsSchema):
      typePositionsModel = TypePositionsModel(**typepositionsSchema.dict())
      self.db.add(typePositionsModel)
      self.db.commit()
      return

    def deleteTypePositions(self, id: int):
      self.db.query(TypePositionsModel).filter(TypePositionsModel.id == id).delete()
      self.db.commit()
      return

    def updateTypePositions(self, id: int, data: TypePositionsSchema):
      typePositions = self.db.query(TypePositionsModel).filter(TypePositionsModel.id == id).first()
      typePositions.name = data.name
