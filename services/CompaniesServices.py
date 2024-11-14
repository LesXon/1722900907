from models.CompaniesModel import CompaniesModel
from schemas.CompaniesSchema import CompaniesSchema

class CompaniesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getCompanies(self):
      result = self.db.query(CompaniesModel).all()
      return result

    def getCompanie(self, id):
      result = self.db.query(CompaniesModel).filter(CompaniesModel.id == id).first()
      return result

    def createCompanies(self, companiesSchema: CompaniesSchema):
      companiesModel = CompaniesModel(**companiesSchema.dict())
      self.db.add(companiesModel)
      self.db.commit()
      return

    def deleteCompanies(self, id: int):
      self.db.query(CompaniesModel).filter(CompaniesModel.id == id).delete()
      self.db.commit()
      return

    def updateCompanies(self, id: int, data: CompaniesSchema):
      companies = self.db.query(CompaniesModel).filter(CompaniesModel.id == id).first()
      companies.name = data.name
