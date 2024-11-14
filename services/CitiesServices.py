from models.CitiesModel import CitiesModel
from schemas.CitiesSchema import CitiesSchema

class CitiesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getCities(self):
      result = self.db.query(CitiesModel).all()
      return result

    def getCitie(self, id):
      result = self.db.query(CitiesModel).filter(CitiesModel.id == id).first()
      return result

    def createCities(self, citiesSchema: CitiesSchema):
      citiesModel = CitiesModel(**citiesSchema.dict())
      self.db.add(citiesModel)
      self.db.commit()
      return

    def deleteCities(self, id: int):
      self.db.query(CitiesModel).filter(CitiesModel.id == id).delete()
      self.db.commit()
      return

    def updateCities(self, id: int, data: CitiesSchema):
      cities = self.db.query(CitiesModel).filter(CitiesModel.id == id).first()
      cities.name = data.name
