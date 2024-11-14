from models.SocialNetworksModel import SocialNetworksModel
from schemas.SocialNetworksSchema import SocialNetworksSchema

class SocialNetworksServices():

    def __init__(self, db) -> None:
      self.db = db

    def getSocialNetworks(self):
      result = self.db.query(SocialNetworksModel).all()
      return result

    def getSocialNetwork(self, id):
      result = self.db.query(SocialNetworksModel).filter(SocialNetworksModel.id == id).first()
      return result

    def createSocialNetworks(self, socialnetworksSchema: SocialNetworksSchema):
      socialNetworksModel = SocialNetworksModel(**socialnetworksSchema.dict())
      self.db.add(socialNetworksModel)
      self.db.commit()
      return

    def deleteSocialNetworks(self, id: int):
      self.db.query(SocialNetworksModel).filter(SocialNetworksModel.id == id).delete()
      self.db.commit()
      return

    def updateSocialNetworks(self, id: int, data: SocialNetworksSchema):
      socialNetworks = self.db.query(SocialNetworksModel).filter(SocialNetworksModel.id == id).first()
      socialNetworks.name = data.name
      socialNetworks.url = data.url
