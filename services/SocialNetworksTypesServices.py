from models.SocialNetworksTypesModel import SocialNetworksTypesModel
from schemas.SocialNetworksTypesSchema import SocialNetworksTypesSchema

class SocialNetworksTypesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getSocialNetworksTypes(self):
      result = self.db.query(SocialNetworksTypesModel).all()
      return result

    def getSocialNetworksType(self, id):
      result = self.db.query(SocialNetworksTypesModel).filter(SocialNetworksTypesModel.id == id).first()
      return result

    def createSocialNetworksTypes(self, socialnetworkstypesSchema: SocialNetworksTypesSchema):
      socialNetworksTypesModel = SocialNetworksTypesModel(**socialnetworkstypesSchema.dict())
      self.db.add(socialNetworksTypesModel)
      self.db.commit()
      return

    def deleteSocialNetworksTypes(self, id: int):
      self.db.query(SocialNetworksTypesModel).filter(SocialNetworksTypesModel.id == id).delete()
      self.db.commit()
      return

    def updateSocialNetworksTypes(self, id: int, data: SocialNetworksTypesSchema):
      socialNetworksTypes = self.db.query(SocialNetworksTypesModel).filter(SocialNetworksTypesModel.id == id).first()
      socialNetworksTypes.name = data.name
