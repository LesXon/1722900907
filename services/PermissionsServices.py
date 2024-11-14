from models.PermissionsModel import PermissionsModel
from schemas.PermissionsSchema import PermissionsSchema

class PermissionsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getPermissions(self):
      result = self.db.query(PermissionsModel).all()
      return result

    def getPermission(self, id):
      result = self.db.query(PermissionsModel).filter(PermissionsModel.id == id).first()
      return result

    def createPermissions(self, permissionsSchema: PermissionsSchema):
      permissionsModel = PermissionsModel(**permissionsSchema.dict())
      self.db.add(permissionsModel)
      self.db.commit()
      return

    def deletePermissions(self, id: int):
      self.db.query(PermissionsModel).filter(PermissionsModel.id == id).delete()
      self.db.commit()
      return

    def updatePermissions(self, id: int, data: PermissionsSchema):
      permissions = self.db.query(PermissionsModel).filter(PermissionsModel.id == id).first()
      permissions.name = data.name
