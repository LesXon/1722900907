from models.PersonsModel import PersonsModel
from schemas.PersonsSchema import PersonsSchema

class PersonsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getPersons(self):
      result = self.db.query(PersonsModel).all()
      return result

    def getPerson(self, id):
      result = self.db.query(PersonsModel).filter(PersonsModel.id == id).first()
      return result

    def createPersons(self, personsSchema: PersonsSchema):
      personsModel = PersonsModel(**personsSchema.dict())
      self.db.add(personsModel)
      self.db.commit()
      return

    def deletePersons(self, id: int):
      self.db.query(PersonsModel).filter(PersonsModel.id == id).delete()
      self.db.commit()
      return

    def updatePersons(self, id: int, data: PersonsSchema):
      persons = self.db.query(PersonsModel).filter(PersonsModel.id == id).first()
      persons.firstName1 = data.firstName1
      persons.firstName2 = data.firstName2
      persons.lastName1 = data.lastName1
      persons.lastName2 = data.lastName2
      persons.genre = data.genre
      persons.dateBirth = data.dateBirth
      persons.isAlive = data.isAlive
      persons.email = data.email