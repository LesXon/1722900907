from models.PhonesModel import PhonesModel
from schemas.PhonesSchema import PhonesSchema

class PhonesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getPhones(self):
      result = self.db.query(PhonesModel).all()
      return result

    def getPhone(self, id):
      result = self.db.query(PhonesModel).filter(PhonesModel.id == id).first()
      return result

    def createPhones(self, phonesSchema: PhonesSchema):
      phonesModel = PhonesModel(**phonesSchema.dict())
      self.db.add(phonesModel)
      self.db.commit()
      return

    def deletePhones(self, id: int):
      self.db.query(PhonesModel).filter(PhonesModel.id == id).delete()
      self.db.commit()
      return

    def updatePhones(self, id: int, data: PhonesSchema):
      phones = self.db.query(PhonesModel).filter(PhonesModel.id == id).first()
      phones.number = data.number
