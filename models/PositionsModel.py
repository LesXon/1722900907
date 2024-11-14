# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class PositionsModel(Base):

    __tablename__ = "positions"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Employees "0..1" --> "0..*" Positions
    
    idEmployees = Column(Integer, ForeignKey('employees.id'), nullable=True)    
    employees = relationship('EmployeesModel', back_populates='positions')

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # TypePositions "0..1" --> "0..*" Positions
    
    idTypePositions = Column(Integer, ForeignKey('type_positions.id'), nullable=True)    
    type_positions = relationship('TypePositionsModel', back_populates='positions')
