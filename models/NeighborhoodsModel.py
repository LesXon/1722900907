# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class NeighborhoodsModel(Base):

    __tablename__ = "neighborhoods"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=False) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Districts "0..1" --> "0..*" Neighborhoods
    
    idDistricts = Column(Integer, ForeignKey('districts.id'), nullable=True)    
    districts = relationship('DistrictsModel', back_populates='neighborhoods')

    # 5. One to Many Bidirectional
    # classDiagram
    # Neighborhoods "0..1" --> "0..*" Addresses
    
    addresses = relationship('AddressesModel', back_populates='neighborhoods')
