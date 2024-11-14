from models.UsersModel import UsersModel
from schemas.UsersSchema import UsersSchema

class UsersServices():

    def __init__(self, db) -> None:
      self.db = db

    def getUsers(self):
      result = self.db.query(UsersModel).all()
      return result

    def getUser(self, id):
      result = self.db.query(UsersModel).filter(UsersModel.id == id).first()
      return result

    def createUsers(self, usersSchema: UsersSchema):
      usersModel = UsersModel(**usersSchema.dict())
      self.db.add(usersModel)
      self.db.commit()
      return

    def deleteUsers(self, id: int):
      self.db.query(UsersModel).filter(UsersModel.id == id).delete()
      self.db.commit()
      return

    def updateUsers(self, id: int, data: UsersSchema):
      users = self.db.query(UsersModel).filter(UsersModel.id == id).first()
      users.name = data.name
      users.password = data.password
      users.mail = data.mail
