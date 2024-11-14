from models.StatesModel import StatesModel
from schemas.StatesSchema import StatesSchema

class StatesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getStates(self):
      result = self.db.query(StatesModel).all()
      return result

    def getState(self, id):
      result = self.db.query(StatesModel).filter(StatesModel.id == id).first()
      return result

    def createStates(self, statesSchema: StatesSchema):
      statesModel = StatesModel(**statesSchema.dict())
      self.db.add(statesModel)
      self.db.commit()
      return

    def deleteStates(self, id: int):
      self.db.query(StatesModel).filter(StatesModel.id == id).delete()
      self.db.commit()
      return

    def updateStates(self, id: int, data: StatesSchema):
      states = self.db.query(StatesModel).filter(StatesModel.id == id).first()
      states.name = data.name
