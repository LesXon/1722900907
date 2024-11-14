from models.ConstructionsTypesModel import ConstructionsTypesModel
from schemas.ConstructionsTypesSchema import ConstructionsTypesSchema

class ConstructionsTypesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getConstructionsTypes(self):
      result = self.db.query(ConstructionsTypesModel).all()
      return result

    def getConstructionsType(self, id):
      result = self.db.query(ConstructionsTypesModel).filter(ConstructionsTypesModel.id == id).first()
      return result

    def createConstructionsTypes(self, constructionstypesSchema: ConstructionsTypesSchema):
      constructionsTypesModel = ConstructionsTypesModel(**constructionstypesSchema.dict())
      self.db.add(constructionsTypesModel)
      self.db.commit()
      return

    def deleteConstructionsTypes(self, id: int):
      self.db.query(ConstructionsTypesModel).filter(ConstructionsTypesModel.id == id).delete()
      self.db.commit()
      return

    def updateConstructionsTypes(self, id: int, data: ConstructionsTypesSchema):
      constructionsTypes = self.db.query(ConstructionsTypesModel).filter(ConstructionsTypesModel.id == id).first()
      constructionsTypes.name = data.name
