# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class DataStructuresModel(Base):

    __tablename__ = "data_structures"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=False) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # SystemDataStructuresformats "0..1" --> "0..*" DataStructures
    
    idSystemDataStructuresformats = Column(Integer, ForeignKey('system_data_structuresformats.id'), nullable=True)    
    system_data_structuresformats = relationship('SystemDataStructuresformatsModel', back_populates='data_structures')

    # 5. One to Many Bidirectional
    # classDiagram
    # DataStructures "0..1" --> "0..*" FieldDescriptionFormats
    
    field_description_formats = relationship('FieldDescriptionFormatsModel', back_populates='data_structures')
