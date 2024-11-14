# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class IdsModel(Base):

    __tablename__ = "ids"

    id = Column(Integer, primary_key = True)

    number = Column(String(20), nullable=False, unique=True) # type: string
    issueDate = Column(TIMESTAMP, nullable=True, unique=False) # type: timestamp

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # IdsTypes "0..1" --> "0..*" Ids
    
    idIdsTypes = Column(Integer, ForeignKey('ids_types.id'), nullable=True)    
    ids_types = relationship('IdsTypesModel', back_populates='ids')
