# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class NavigationBarsModel(Base):

    __tablename__ = "navigation_bars"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Apps "0..1" --> "0..*" NavigationBars
    
    idApps = Column(Integer, ForeignKey('apps.id'), nullable=True)    
    apps = relationship('AppsModel', back_populates='navigation_bars')

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # AppMenus "0..1" --> "0..*" NavigationBars
    
    idAppMenus = Column(Integer, ForeignKey('app_menus.id'), nullable=True)    
    app_menus = relationship('AppMenusModel', back_populates='navigation_bars')

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # NavigationBarsTypes "0..1" --> "0..*" NavigationBars
    
    idNavigationBarsTypes = Column(Integer, ForeignKey('navigation_bars_types.id'), nullable=True)    
    navigation_bars_types = relationship('NavigationBarsTypesModel', back_populates='navigation_bars')
