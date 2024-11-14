# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class CompaniesModel(Base):

    __tablename__ = "companies"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional
    # classDiagram
    # Companies "0..1" --> "0..*" Employees
    
    employees = relationship('EmployeesModel', back_populates='companies')

    # 5. One to Many Bidirectional
    # classDiagram
    # Companies "0..1" --> "0..*" Licenses
    
    licenses = relationship('LicensesModel', back_populates='companies')

    # 5. One to Many Bidirectional
    # classDiagram
    # Companies "0..1" --> "0..*" Systems
    
    systems = relationship('SystemsModel', back_populates='companies')

    # 5. One to Many Bidirectional
    # classDiagram
    # Companies "0..1" --> "0..*" SocialNetworks
    
    social_networks = relationship('SocialNetworksModel', back_populates='companies')
