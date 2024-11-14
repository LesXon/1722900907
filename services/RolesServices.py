from models.RolesModel import RolesModel
from schemas.RolesSchema import RolesSchema

class RolesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getRoles(self):
      result = self.db.query(RolesModel).all()
      return result

    def getRole(self, id):
      result = self.db.query(RolesModel).filter(RolesModel.id == id).first()
      return result

    def createRoles(self, rolesSchema: RolesSchema):
      rolesModel = RolesModel(**rolesSchema.dict())
      self.db.add(rolesModel)
      self.db.commit()
      return

    def deleteRoles(self, id: int):
      self.db.query(RolesModel).filter(RolesModel.id == id).delete()
      self.db.commit()
      return

    def updateRoles(self, id: int, data: RolesSchema):
      roles = self.db.query(RolesModel).filter(RolesModel.id == id).first()
      roles.name = data.name
