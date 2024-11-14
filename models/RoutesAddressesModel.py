# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class RoutesAddressesModel(Base):

    __tablename__ = "routes_addresses"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # RoutesAddressesTypes "0..1" --> "0..*" RoutesAddresses
    
    idRoutesAddressesTypes = Column(Integer, ForeignKey('routes_addresses_types.id'), nullable=True)    
    routes_addresses_types = relationship('RoutesAddressesTypesModel', back_populates='routes_addresses')

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # RouteNames "0..1" --> "0..*" RoutesAddresses
    
    idRouteNames = Column(Integer, ForeignKey('route_names.id'), nullable=True)    
    route_names = relationship('RouteNamesModel', back_populates='routes_addresses')

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Addresses "0..1" --> "0..*" RoutesAddresses
    
    idAddresses = Column(Integer, ForeignKey('addresses.id'), nullable=True)    
    addresses = relationship('AddressesModel', back_populates='routes_addresses')
