# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class StatesModel(Base):

    __tablename__ = "states"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Countries "0..1" --> "0..*" States
    
    idCountries = Column(Integer, ForeignKey('countries.id'), nullable=True)    
    countries = relationship('CountriesModel', back_populates='states')

    # 5. One to Many Bidirectional
    # classDiagram
    # States "0..1" --> "0..*" Cities
    
    cities = relationship('CitiesModel', back_populates='states')
