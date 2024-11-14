# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class LicensesModel(Base):

    __tablename__ = "licenses"

    id = Column(Integer, primary_key = True)

    data = Column(String(250), nullable=False, unique=True) # type: string

    # 5. One to Many Bidirectional.INVERSE
    # classDiagram
    # Apps "0..1" --> "0..*" Licenses
    
    idApps = Column(Integer, ForeignKey('apps.id'), nullable=True)    
    apps = relationship('AppsModel', back_populates='licenses')
