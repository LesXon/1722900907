from models.ProceduresManualModel import ProceduresManualModel
from schemas.ProceduresManualSchema import ProceduresManualSchema

class ProceduresManualServices():

    def __init__(self, db) -> None:
      self.db = db

    def getProceduresManual(self):
      result = self.db.query(ProceduresManualModel).all()
      return result

    def getProceduresManua(self, id):
      result = self.db.query(ProceduresManualModel).filter(ProceduresManualModel.id == id).first()
      return result

    def createProceduresManual(self, proceduresmanualSchema: ProceduresManualSchema):
      proceduresManualModel = ProceduresManualModel(**proceduresmanualSchema.dict())
      self.db.add(proceduresManualModel)
      self.db.commit()
      return

    def deleteProceduresManual(self, id: int):
      self.db.query(ProceduresManualModel).filter(ProceduresManualModel.id == id).delete()
      self.db.commit()
      return

    def updateProceduresManual(self, id: int, data: ProceduresManualSchema):
      proceduresManual = self.db.query(ProceduresManualModel).filter(ProceduresManualModel.id == id).first()
      proceduresManual.name = data.name
