# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class ProceduresManualModel(Base):

    __tablename__ = "procedures_manual"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=False) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Systems "0..1" --> "0..*" ProceduresManual
    
    idSystems = Column(Integer, ForeignKey('systems.id'), nullable=True)    
    systems = relationship('SystemsModel', back_populates='procedures_manual')

    # 5. One to Many Bidirectional
    # classDiagram
    # ProceduresManual "0..1" --> "0..*" Diagrams
    
    diagrams = relationship('DiagramsModel', back_populates='procedures_manual')
