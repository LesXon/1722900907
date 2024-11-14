from models.CountriesModel import CountriesModel
from schemas.CountriesSchema import CountriesSchema

class CountriesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getCountries(self):
      result = self.db.query(CountriesModel).all()
      return result

    def getCountrie(self, id):
      result = self.db.query(CountriesModel).filter(CountriesModel.id == id).first()
      return result

    def createCountries(self, countriesSchema: CountriesSchema):
      countriesModel = CountriesModel(**countriesSchema.dict())
      self.db.add(countriesModel)
      self.db.commit()
      return

    def deleteCountries(self, id: int):
      self.db.query(CountriesModel).filter(CountriesModel.id == id).delete()
      self.db.commit()
      return

    def updateCountries(self, id: int, data: CountriesSchema):
      countries = self.db.query(CountriesModel).filter(CountriesModel.id == id).first()
      countries.name = data.name
