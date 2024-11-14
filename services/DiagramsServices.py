from models.DiagramsModel import DiagramsModel
from schemas.DiagramsSchema import DiagramsSchema

class DiagramsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getDiagrams(self):
      result = self.db.query(DiagramsModel).all()
      return result

    def getDiagram(self, id):
      result = self.db.query(DiagramsModel).filter(DiagramsModel.id == id).first()
      return result

    def createDiagrams(self, diagramsSchema: DiagramsSchema):
      diagramsModel = DiagramsModel(**diagramsSchema.dict())
      self.db.add(diagramsModel)
      self.db.commit()
      return

    def deleteDiagrams(self, id: int):
      self.db.query(DiagramsModel).filter(DiagramsModel.id == id).delete()
      self.db.commit()
      return

    def updateDiagrams(self, id: int, data: DiagramsSchema):
      diagrams = self.db.query(DiagramsModel).filter(DiagramsModel.id == id).first()
      diagrams.name = data.name
