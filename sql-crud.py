from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")

base = declarative_base()


# Instead of connecting to a database directly we will ask for a session
# Create a new instance of sessionmaker, then point to our engine (the db)

Session = sessionmaker(db)

# Opens an actual session by calling the session()

session = Session()

# Creating db using declarative_base subclass

base.metadata.create_all(db)

