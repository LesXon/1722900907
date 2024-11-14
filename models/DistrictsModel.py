# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class DistrictsModel(Base):

    __tablename__ = "districts"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=False) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Cities "0..1" --> "0..*" Districts
    
    idCities = Column(Integer, ForeignKey('cities.id'), nullable=True)    
    cities = relationship('CitiesModel', back_populates='districts')

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # DistrictsTypes "0..1" --> "0..*" Districts
    
    idDistrictsTypes = Column(Integer, ForeignKey('districts_types.id'), nullable=True)    
    districts_types = relationship('DistrictsTypesModel', back_populates='districts')

    # 5. One to Many Bidirectional
    # classDiagram
    # Districts "0..1" --> "0..*" Neighborhoods
    
    neighborhoods = relationship('NeighborhoodsModel', back_populates='districts')
