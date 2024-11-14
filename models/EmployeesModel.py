# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class EmployeesModel(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key = True)

    code = Column(String(250), nullable=True, unique=True) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Companies "0..1" --> "0..*" Employees
    
    idCompanies = Column(Integer, ForeignKey('companies.id'), nullable=True)    
    companies = relationship('CompaniesModel', back_populates='employees')

    # 5. One to Many Bidirectional
    # classDiagram
    # Employees "0..1" --> "0..*" Positions
    
    positions = relationship('PositionsModel', back_populates='employees')
