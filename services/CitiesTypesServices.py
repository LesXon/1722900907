from models.CitiesTypesModel import CitiesTypesModel
from schemas.CitiesTypesSchema import CitiesTypesSchema

class CitiesTypesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getCitiesTypes(self):
      result = self.db.query(CitiesTypesModel).all()
      return result

    def getCitiesType(self, id):
      result = self.db.query(CitiesTypesModel).filter(CitiesTypesModel.id == id).first()
      return result

    def createCitiesTypes(self, citiestypesSchema: CitiesTypesSchema):
      citiesTypesModel = CitiesTypesModel(**citiestypesSchema.dict())
      self.db.add(citiesTypesModel)
      self.db.commit()
      return

    def deleteCitiesTypes(self, id: int):
      self.db.query(CitiesTypesModel).filter(CitiesTypesModel.id == id).delete()
      self.db.commit()
      return

    def updateCitiesTypes(self, id: int, data: CitiesTypesSchema):
      citiesTypes = self.db.query(CitiesTypesModel).filter(CitiesTypesModel.id == id).first()
      citiesTypes.name = data.name
