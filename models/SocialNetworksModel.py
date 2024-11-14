# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class SocialNetworksModel(Base):

    __tablename__ = "social_networks"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=False) # type: string
    url = Column(String, nullable=False, unique=False) # type: url

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # SocialNetworksTypes "0..1" --> "0..*" SocialNetworks
    
    idSocialNetworksTypes = Column(Integer, ForeignKey('social_networks_types.id'), nullable=True)    
    social_networks_types = relationship('SocialNetworksTypesModel', back_populates='social_networks')
