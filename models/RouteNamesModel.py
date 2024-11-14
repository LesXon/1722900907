# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class RouteNamesModel(Base):

    __tablename__ = "route_names"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional
    # classDiagram
    # RouteNames "0..1" --> "0..*" RoutesAddresses
    
    routes_addresses = relationship('RoutesAddressesModel', back_populates='route_names')
