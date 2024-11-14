# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class PermissionsModel(Base):

    __tablename__ = "permissions"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Roles "0..1" --> "0..*" Permissions
    
    idRoles = Column(Integer, ForeignKey('roles.id'), nullable=True)    
    roles = relationship('RolesModel', back_populates='permissions')

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # AppMenus "0..1" --> "0..*" Permissions
    
    idAppMenus = Column(Integer, ForeignKey('app_menus.id'), nullable=True)    
    app_menus = relationship('AppMenusModel', back_populates='permissions')
