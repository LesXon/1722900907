from models.LicensesModel import LicensesModel
from schemas.LicensesSchema import LicensesSchema

class LicensesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getLicenses(self):
      result = self.db.query(LicensesModel).all()
      return result

    def getLicense(self, id):
      result = self.db.query(LicensesModel).filter(LicensesModel.id == id).first()
      return result

    def createLicenses(self, licensesSchema: LicensesSchema):
      licensesModel = LicensesModel(**licensesSchema.dict())
      self.db.add(licensesModel)
      self.db.commit()
      return

    def deleteLicenses(self, id: int):
      self.db.query(LicensesModel).filter(LicensesModel.id == id).delete()
      self.db.commit()
      return

    def updateLicenses(self, id: int, data: LicensesSchema):
      licenses = self.db.query(LicensesModel).filter(LicensesModel.id == id).first()
      licenses.data = data.data
