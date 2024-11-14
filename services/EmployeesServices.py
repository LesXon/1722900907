from models.EmployeesModel import EmployeesModel
from schemas.EmployeesSchema import EmployeesSchema

class EmployeesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getEmployees(self):
      result = self.db.query(EmployeesModel).all()
      return result

    def getEmployee(self, id):
      result = self.db.query(EmployeesModel).filter(EmployeesModel.id == id).first()
      return result

    def createEmployees(self, employeesSchema: EmployeesSchema):
      employeesModel = EmployeesModel(**employeesSchema.dict())
      self.db.add(employeesModel)
      self.db.commit()
      return

    def deleteEmployees(self, id: int):
      self.db.query(EmployeesModel).filter(EmployeesModel.id == id).delete()
      self.db.commit()
      return

    def updateEmployees(self, id: int, data: EmployeesSchema):
      employees = self.db.query(EmployeesModel).filter(EmployeesModel.id == id).first()
      employees.code = data.code
