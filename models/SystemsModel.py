# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class SystemsModel(Base):

    __tablename__ = "systems"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional
    # classDiagram
    # Systems "0..1" --> "0..*" ProceduresManual
    
    procedures_manual = relationship('ProceduresManualModel', back_populates='systems')

    # 5. One to Many Bidirectional
    # classDiagram
    # Systems "0..1" --> "0..*" DataDictionaries
    
    data_dictionaries = relationship('DataDictionariesModel', back_populates='systems')
