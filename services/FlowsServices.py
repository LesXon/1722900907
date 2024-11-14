from models.FlowsModel import FlowsModel
from schemas.FlowsSchema import FlowsSchema

class FlowsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getFlows(self):
      result = self.db.query(FlowsModel).all()
      return result

    def getFlow(self, id):
      result = self.db.query(FlowsModel).filter(FlowsModel.id == id).first()
      return result

    def createFlows(self, flowsSchema: FlowsSchema):
      flowsModel = FlowsModel(**flowsSchema.dict())
      self.db.add(flowsModel)
      self.db.commit()
      return

    def deleteFlows(self, id: int):
      self.db.query(FlowsModel).filter(FlowsModel.id == id).delete()
      self.db.commit()
      return

    def updateFlows(self, id: int, data: FlowsSchema):
      flows = self.db.query(FlowsModel).filter(FlowsModel.id == id).first()
      flows.name = data.name
