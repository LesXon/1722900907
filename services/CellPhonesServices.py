from models.CellPhonesModel import CellPhonesModel
from schemas.CellPhonesSchema import CellPhonesSchema

class CellPhonesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getCellPhones(self):
      result = self.db.query(CellPhonesModel).all()
      return result

    def getCellPhone(self, id):
      result = self.db.query(CellPhonesModel).filter(CellPhonesModel.id == id).first()
      return result

    def createCellPhones(self, cellphonesSchema: CellPhonesSchema):
      cellPhonesModel = CellPhonesModel(**cellphonesSchema.dict())
      self.db.add(cellPhonesModel)
      self.db.commit()
      return

    def deleteCellPhones(self, id: int):
      self.db.query(CellPhonesModel).filter(CellPhonesModel.id == id).delete()
      self.db.commit()
      return

    def updateCellPhones(self, id: int, data: CellPhonesSchema):
      cellPhones = self.db.query(CellPhonesModel).filter(CellPhonesModel.id == id).first()
      cellPhones.number = data.number
