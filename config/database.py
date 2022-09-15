from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/pi_data03"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo = True)

# Each instance of SessionLocal class will be database session
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# The class itself is not a database session yet.
# Once we create an instance of the SessionLocal class, this instance will be the actual database session.
# We use declarative_base to return a class which we will inherit from to be create database models
Base = declarative_base()