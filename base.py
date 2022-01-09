import os
import sys
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Float, Boolean, asc, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base() #use as basis for models
engine = create_engine('sqlite:///ConnectFourAI.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession() #use as basis for database modification

Query = session.query #makes life easier
