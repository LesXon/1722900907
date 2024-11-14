# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship
from .RolesUsersModel import roles_users
from .RolesRolesModel import roles_roles

class RolesModel(Base):

    __tablename__ = "roles"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 7. Many to Many Bidirectional.INVERSE
    # classDiagram
    # Users "0..*" --> "0..*" Roles
    
    users = relationship('UsersModel', secondary=roles_users, back_populates='roles')

    # 7. Many to Many Bidirectional
    # classDiagram
    # Roles "0..*" --> "0..*" Roles
    
    # 7. Many to Many Bidirectional.INVERSE
    # classDiagram
    # Roles "0..*" --> "0..*" Roles
    
    roles = relationship('RolesModel', secondary=roles_roles, back_populates='roles')

    # 5. One to Many Bidirectional
    # classDiagram
    # Roles "0..1" --> "0..*" Permissions
    
    permissions = relationship('PermissionsModel', back_populates='roles')
