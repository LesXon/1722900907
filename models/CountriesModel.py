# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class CountriesModel(Base):

    __tablename__ = "countries"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Continents "0..1" --> "0..*" Countries
    
    idContinents = Column(Integer, ForeignKey('continents.id'), nullable=True)    
    continents = relationship('ContinentsModel', back_populates='countries')

    # 5. One to Many Bidirectional
    # classDiagram
    # Countries "0..1" --> "0..*" States
    
    states = relationship('StatesModel', back_populates='countries')

    # 5. One to Many Bidirectional
    # classDiagram
    # Countries "0..1" --> "0..*" cellPhones
    
    phones = relationship('cellPhonesModel', back_populates='countries')
