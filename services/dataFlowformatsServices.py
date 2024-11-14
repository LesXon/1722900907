from models.dataFlowformatsModel import dataFlowformatsModel
from schemas.dataFlowformatsSchema import dataFlowformatsSchema

class dataFlowformatsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getdataFlowformats(self):
      result = self.db.query(dataFlowformatsModel).all()
      return result

    def getdataFlowformat(self, id):
      result = self.db.query(dataFlowformatsModel).filter(dataFlowformatsModel.id == id).first()
      return result

    def createdataFlowformats(self, dataflowformatsSchema: dataFlowformatsSchema):
      dataFlowformatsModel = dataFlowformatsModel(**dataflowformatsSchema.dict())
      self.db.add(dataFlowformatsModel)
      self.db.commit()
      return

    def deletedataFlowformats(self, id: int):
      self.db.query(dataFlowformatsModel).filter(dataFlowformatsModel.id == id).delete()
      self.db.commit()
      return

    def updatedataFlowformats(self, id: int, data: dataFlowformatsSchema):
      dataFlowformats = self.db.query(dataFlowformatsModel).filter(dataFlowformatsModel.id == id).first()
      dataFlowformats.name = data.name
