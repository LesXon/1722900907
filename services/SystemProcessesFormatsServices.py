from models.SystemProcessesFormatsModel import SystemProcessesFormatsModel
from schemas.SystemProcessesFormatsSchema import SystemProcessesFormatsSchema

class SystemProcessesFormatsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getSystemProcessesFormats(self):
      result = self.db.query(SystemProcessesFormatsModel).all()
      return result

    def getSystemProcessesFormat(self, id):
      result = self.db.query(SystemProcessesFormatsModel).filter(SystemProcessesFormatsModel.id == id).first()
      return result

    def createSystemProcessesFormats(self, systemprocessesformatsSchema: SystemProcessesFormatsSchema):
      systemProcessesFormatsModel = SystemProcessesFormatsModel(**systemprocessesformatsSchema.dict())
      self.db.add(systemProcessesFormatsModel)
      self.db.commit()
      return

    def deleteSystemProcessesFormats(self, id: int):
      self.db.query(SystemProcessesFormatsModel).filter(SystemProcessesFormatsModel.id == id).delete()
      self.db.commit()
      return

    def updateSystemProcessesFormats(self, id: int, data: SystemProcessesFormatsSchema):
      systemProcessesFormats = self.db.query(SystemProcessesFormatsModel).filter(SystemProcessesFormatsModel.id == id).first()
      systemProcessesFormats.name = data.name
