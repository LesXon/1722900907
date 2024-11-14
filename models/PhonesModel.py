# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class PhonesModel(Base):

    __tablename__ = "phones"

    id = Column(Integer, primary_key = True)

    number = Column(Integer) # type: int

    # 5. One to Many Bidirectional
    # classDiagram
    # Phones "0..1" --> "0..*" CellPhones
    
    cell_phones = relationship('CellPhonesModel', back_populates='phones')
