# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class DataDictionariesModel(Base):

    __tablename__ = "data_dictionaries"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=False) # type: string

    # 5. One to Many Bidirectional
    # classDiagram
    # DataDictionaries "0..1" --> "0..*" SystemEntitiesFormats
    
    system_entities_formats = relationship('SystemEntitiesFormatsModel', back_populates='data_dictionaries')

    # 5. One to Many Bidirectional
    # classDiagram
    # DataDictionaries "0..1" --> "0..*" DataStorageFormats
    
    data_storage_formats = relationship('DataStorageFormatsModel', back_populates='data_dictionaries')

    # 5. One to Many Bidirectional
    # classDiagram
    # DataDictionaries "0..1" --> "0..*" SystemProcessesFormats
    
    system_processes_formats = relationship('SystemProcessesFormatsModel', back_populates='data_dictionaries')

    # 5. One to Many Bidirectional
    # classDiagram
    # DataDictionaries "0..1" --> "0..*" dataFlowformats
    
    flowformats = relationship('dataFlowformatsModel', back_populates='data_dictionaries')

    # 5. One to Many Bidirectional
    # classDiagram
    # DataDictionaries "0..1" --> "0..*" SystemDataStructuresformats
    
    system_data_structuresformats = relationship('SystemDataStructuresformatsModel', back_populates='data_dictionaries')

    # 5. One to Many Bidirectional
    # classDiagram
    # DataDictionaries "0..1" --> "0..*" systemFormats
    
    formats = relationship('systemFormatsModel', back_populates='data_dictionaries')
