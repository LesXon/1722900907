# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class DiagramsModel(Base):

    __tablename__ = "diagrams"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=False) # type: string

    # 5. One to Many Bidirectional
    # classDiagram
    # Diagrams "0..1" --> "0..*" Entities
    
    entities = relationship('EntitiesModel', back_populates='diagrams')

    # 5. One to Many Bidirectional
    # classDiagram
    # Diagrams "0..1" --> "0..*" Processes
    
    processes = relationship('ProcessesModel', back_populates='diagrams')

    # 5. One to Many Bidirectional
    # classDiagram
    # Diagrams "0..1" --> "0..*" Flows
    
    flows = relationship('FlowsModel', back_populates='diagrams')

    # 5. One to Many Bidirectional
    # classDiagram
    # Diagrams "0..1" --> "0..*" Storages
    
    storages = relationship('StoragesModel', back_populates='diagrams')

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # ProceduresManual "0..1" --> "0..*" Diagrams
    
    idProceduresManual = Column(Integer, ForeignKey('procedures_manual.id'), nullable=True)    
    procedures_manual = relationship('ProceduresManualModel', back_populates='diagrams')
