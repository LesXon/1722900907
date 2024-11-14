# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship
from .UsersRolesModel import users_roles

class UsersModel(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string
    password = Column(String(250), nullable=False, unique=False) # type: string
    mail = Column(String, nullable=False, unique=True) # type: mail

    # 7. Many to Many Bidirectional
    # classDiagram
    # Users "0..*" --> "0..*" Roles

    # 2.One to One Bidirectional.INVERSE
    # classDiagram
    # Employees "0..1" --> "0..1" Users
    
    idEmployees = Column(Integer, ForeignKey('employees.id'), nullable=True)    
    employees = relationship('EmployeesModel', back_populates='users')
