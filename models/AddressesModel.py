# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class AddressesModel(Base):

    __tablename__ = "addresses"

    id = Column(Integer, primary_key = True)

    address = Column(String(250), nullable=True, unique=True) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # ConstructionsTypes "0..1" --> "0..*" Addresses
    
    idConstructionsTypes = Column(Integer, ForeignKey('constructions_types.id'), nullable=True)    
    constructions_types = relationship('ConstructionsTypesModel', back_populates='addresses')

    # 5. One to Many Bidirectional
    # classDiagram
    # Addresses "0..1" --> "0..*" Addresses
    
    addresses = relationship('AddressesModel', back_populates='addresses')

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # AddressesTypes "0..1" --> "0..*" Addresses
    
    idAddressesTypes = Column(Integer, ForeignKey('addresses_types.id'), nullable=True)    
    addresses_types = relationship('AddressesTypesModel', back_populates='addresses')

    # 5. One to Many Bidirectional
    # classDiagram
    # Addresses "0..1" --> "0..*" RoutesAddresses
    
    routes_addresses = relationship('RoutesAddressesModel', back_populates='addresses')

    # 5. One to Many Bidirectional
    # classDiagram
    # Addresses "0..1" --> "0..*" Phones
    
    phones = relationship('PhonesModel', back_populates='addresses')
