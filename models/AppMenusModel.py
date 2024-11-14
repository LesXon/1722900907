# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class AppMenusModel(Base):

    __tablename__ = "app_menus"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # AppMenusTypes "0..1" --> "0..*" AppMenus
    
    idAppMenusTypes = Column(Integer, ForeignKey('app_menus_types.id'), nullable=True)    
    app_menus_types = relationship('AppMenusTypesModel', back_populates='app_menus')

    # 5. One to Many Bidirectional
    # classDiagram
    # AppMenus "0..1" --> "0..*" NavigationBars
    
    navigation_bars = relationship('NavigationBarsModel', back_populates='app_menus')

    # 5. One to Many Bidirectional
    # classDiagram
    # AppMenus "0..1" --> "0..*" AppMenus
    
    app_menus = relationship('AppMenusModel', back_populates='app_menus')
