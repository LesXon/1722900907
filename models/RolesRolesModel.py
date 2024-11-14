# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer,ForeignKey,Table

#Intermediate table
roles_roles = Table(
    'roles_roles',
    Base.metadata,
    Column('id1Roles', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('id2Roles', Integer, ForeignKey('roles.id'), primary_key=True),
)
