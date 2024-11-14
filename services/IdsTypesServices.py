from models.IdsTypesModel import IdsTypesModel
from schemas.IdsTypesSchema import IdsTypesSchema

class IdsTypesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getIdsTypes(self):
      result = self.db.query(IdsTypesModel).all()
      return result

    def getIdsType(self, id):
      result = self.db.query(IdsTypesModel).filter(IdsTypesModel.id == id).first()
      return result

    def createIdsTypes(self, idstypesSchema: IdsTypesSchema):
      idsTypesModel = IdsTypesModel(**idstypesSchema.dict())
      self.db.add(idsTypesModel)
      self.db.commit()
      return

    def deleteIdsTypes(self, id: int):
      self.db.query(IdsTypesModel).filter(IdsTypesModel.id == id).delete()
      self.db.commit()
      return

    def updateIdsTypes(self, id: int, data: IdsTypesSchema):
      idsTypes = self.db.query(IdsTypesModel).filter(IdsTypesModel.id == id).first()
      idsTypes.name = data.name
