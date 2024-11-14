from models.FieldDescriptionFormatsModel import FieldDescriptionFormatsModel
from schemas.FieldDescriptionFormatsSchema import FieldDescriptionFormatsSchema

class FieldDescriptionFormatsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getFieldDescriptionFormats(self):
      result = self.db.query(FieldDescriptionFormatsModel).all()
      return result

    def getFieldDescriptionFormat(self, id):
      result = self.db.query(FieldDescriptionFormatsModel).filter(FieldDescriptionFormatsModel.id == id).first()
      return result

    def createFieldDescriptionFormats(self, fielddescriptionformatsSchema: FieldDescriptionFormatsSchema):
      fieldDescriptionFormatsModel = FieldDescriptionFormatsModel(**fielddescriptionformatsSchema.dict())
      self.db.add(fieldDescriptionFormatsModel)
      self.db.commit()
      return

    def deleteFieldDescriptionFormats(self, id: int):
      self.db.query(FieldDescriptionFormatsModel).filter(FieldDescriptionFormatsModel.id == id).delete()
      self.db.commit()
      return

    def updateFieldDescriptionFormats(self, id: int, data: FieldDescriptionFormatsSchema):
      fieldDescriptionFormats = self.db.query(FieldDescriptionFormatsModel).filter(FieldDescriptionFormatsModel.id == id).first()
      fieldDescriptionFormats.name = data.name
