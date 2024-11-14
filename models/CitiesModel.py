# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class CitiesModel(Base):

    __tablename__ = "cities"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=False) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # States "0..1" --> "0..*" Cities
    
    idStates = Column(Integer, ForeignKey('states.id'), nullable=True)    
    states = relationship('StatesModel', back_populates='cities')

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # CitiesTypes "0..1" --> "0..*" Cities
    
    idCitiesTypes = Column(Integer, ForeignKey('cities_types.id'), nullable=True)    
    cities_types = relationship('CitiesTypesModel', back_populates='cities')

    # 5. One to Many Bidirectional
    # classDiagram
    # Cities "0..1" --> "0..*" Districts
    
    districts = relationship('DistrictsModel', back_populates='cities')

    # 5. One to Many Bidirectional
    # classDiagram
    # Cities "0..1" --> "0..*" Persons
    
    persons = relationship('PersonsModel', back_populates='cities')

    # 5. One to Many Bidirectional
    # classDiagram
    # Cities "0..1" --> "0..*" Ids
    
    ids = relationship('IdsModel', back_populates='cities')
