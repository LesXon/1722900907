# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship
from .PersonsAddressesModel import persons_addresses
from .PersonsPhonesModel import persons_phones

class PersonsModel(Base):

    __tablename__ = "persons"

    id = Column(Integer, primary_key = True)

    firstName1 = Column(String(250), nullable=False, unique=False) # type: string
    firstName2 = Column(String(250), nullable=True, unique=False) # type: string
    lastName1 = Column(String(250), nullable=False, unique=False) # type: string
    lastName2 = Column(String(250), nullable=True, unique=False) # type: string
    genre = Column(String(250), nullable=False, unique=False) # type: string
    dateBirth = Column(TIMESTAMP, nullable=True, unique=False) # type: timestamp
    isAlive = Column(Boolean) # type: boolean
    email = Column(String, nullable=True, unique=False) # type: mail

    # 2.One to One Bidirectional
    # classDiagram
    # Persons "1..1" --> "0..1" Employees
    
    idEmployees = Column(Integer, ForeignKey('employees.id'), nullable=False)    
    employees = relationship('EmployeesModel', back_populates='persons')

    # 2.One to One Bidirectional
    # classDiagram
    # Persons "1..1" --> "1..1" Ids
    
    idIds = Column(Integer, ForeignKey('ids.id'), nullable=False)    
    ids = relationship('IdsModel', back_populates='persons')

    # 7. Many to Many Bidirectional
    # classDiagram
    # Persons "0..*" --> "0..*" Addresses

    # 5. One to Many Bidirectional
    # classDiagram
    # Persons "0..1" --> "0..*" cellPhones
    
    phones = relationship('cellPhonesModel', back_populates='persons')

    # 7. Many to Many Bidirectional
    # classDiagram
    # Persons "0..*" --> "0..*" Phones

    # 5. One to Many Bidirectional
    # classDiagram
    # Persons "0..1" --> "0..*" SocialNetworks
    
    social_networks = relationship('SocialNetworksModel', back_populates='persons')
