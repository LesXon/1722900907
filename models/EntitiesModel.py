# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class EntitiesModel(Base):

    __tablename__ = "entities"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=False) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Diagrams "0..1" --> "0..*" Entities
    
    idDiagrams = Column(Integer, ForeignKey('diagrams.id'), nullable=True)    
    diagrams = relationship('DiagramsModel', back_populates='entities')
