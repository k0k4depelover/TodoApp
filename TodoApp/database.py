from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://deply_database_user:lYq5e3NQNdbXfYtm96YuZ86ycxyiQPyN@dpg-d15rfe6mcj7s73dnehb0-a/deply_database'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

