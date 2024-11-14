# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class AppsModel(Base):

    __tablename__ = "apps"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # AppTypes "0..1" --> "0..*" Apps
    
    idAppTypes = Column(Integer, ForeignKey('app_types.id'), nullable=True)    
    app_types = relationship('AppTypesModel', back_populates='apps')

    # 5. One to Many Bidirectional
    # classDiagram
    # Apps "0..1" --> "0..*" NavigationBars
    
    navigation_bars = relationship('NavigationBarsModel', back_populates='apps')

    # 5. One to Many Bidirectional
    # classDiagram
    # Apps "0..1" --> "0..*" Licenses
    
    licenses = relationship('LicensesModel', back_populates='apps')

    # 5. One to Many Bidirectional
    # classDiagram
    # Apps "0..1" --> "0..*" Apps
    
    apps = relationship('AppsModel', back_populates='apps')

    # 5. One to Many Bidirectional
    # classDiagram
    # Apps "0..1" --> "0..*" Roles
    
    roles = relationship('RolesModel', back_populates='apps')
