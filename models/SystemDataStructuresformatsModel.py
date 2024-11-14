# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class SystemDataStructuresformatsModel(Base):

    __tablename__ = "system_data_structuresformats"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=False) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # DataDictionaries "0..1" --> "0..*" SystemDataStructuresformats
    
    idDataDictionaries = Column(Integer, ForeignKey('data_dictionaries.id'), nullable=True)    
    data_dictionaries = relationship('DataDictionariesModel', back_populates='system_data_structuresformats')

    # 5. One to Many Bidirectional
    # classDiagram
    # SystemDataStructuresformats "0..1" --> "0..*" DataStructures
    
    data_structures = relationship('DataStructuresModel', back_populates='system_data_structuresformats')
