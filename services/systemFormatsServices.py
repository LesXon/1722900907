from models.systemFormatsModel import systemFormatsModel
from schemas.systemFormatsSchema import systemFormatsSchema

class systemFormatsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getsystemFormats(self):
      result = self.db.query(systemFormatsModel).all()
      return result

    def getsystemFormat(self, id):
      result = self.db.query(systemFormatsModel).filter(systemFormatsModel.id == id).first()
      return result

    def createsystemFormats(self, systemformatsSchema: systemFormatsSchema):
      systemFormatsModel = systemFormatsModel(**systemformatsSchema.dict())
      self.db.add(systemFormatsModel)
      self.db.commit()
      return

    def deletesystemFormats(self, id: int):
      self.db.query(systemFormatsModel).filter(systemFormatsModel.id == id).delete()
      self.db.commit()
      return

    def updatesystemFormats(self, id: int, data: systemFormatsSchema):
      systemFormats = self.db.query(systemFormatsModel).filter(systemFormatsModel.id == id).first()
      systemFormats.name = data.name
