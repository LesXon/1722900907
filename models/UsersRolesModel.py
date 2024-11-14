# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer,ForeignKey,Table

#Intermediate table
users_roles = Table(
    'users_roles',
    Base.metadata,
    Column('idUsers', Integer, ForeignKey('users.id'), primary_key=True),
    Column('idRoles', Integer, ForeignKey('roles.id'), primary_key=True),
)
