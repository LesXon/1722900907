from models.ProcessesModel import ProcessesModel
from schemas.ProcessesSchema import ProcessesSchema

class ProcessesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getProcesses(self):
      result = self.db.query(ProcessesModel).all()
      return result

    def getProcesse(self, id):
      result = self.db.query(ProcessesModel).filter(ProcessesModel.id == id).first()
      return result

    def createProcesses(self, processesSchema: ProcessesSchema):
      processesModel = ProcessesModel(**processesSchema.dict())
      self.db.add(processesModel)
      self.db.commit()
      return

    def deleteProcesses(self, id: int):
      self.db.query(ProcessesModel).filter(ProcessesModel.id == id).delete()
      self.db.commit()
      return

    def updateProcesses(self, id: int, data: ProcessesSchema):
      processes = self.db.query(ProcessesModel).filter(ProcessesModel.id == id).first()
      processes.name = data.name
