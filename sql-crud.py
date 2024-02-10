from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")

base = declarative_base()

# Create a class based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)






# Instead of connecting to a database directly we will ask for a session
# Create a new instance of sessionmaker, then point to our engine (the db)

Session = sessionmaker(db)

# Opens an actual session by calling the session()

session = Session()

# Creating db using declarative_base subclass

base.metadata.create_all(db)

# Create records on our programmer table

ada_lovelace = Programmer (
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

martin_bradbury = Programmer (
    first_name = "Martin",
    last_name = "Bradbury",
    gender = "M",
    nationality = "British",
    famous_for = "CI Student"
)

donna_bradbury = Programmer (
    first_name = "Donna",
    last_name = "Bradbury",
    gender = "F",
    nationality = "British",
    famous_for = "Teaching"
)

michael_bradbury = Programmer (
    first_name = "Michael",
    last_name = "Bradbury",
    gender = "M",
    nationality = "British",
    famous_for = "Java Developer"
)

# # # Add each instance of our programmer to the session
# session.add(ada_lovelace)
# session.add(martin_bradbury)
# session.add(donna_bradbury)
# session.add(michael_bradbury)

# # # Commit our session to the database
# session.commit()



# Create a new vairable to query the database

programmers = session.query(Programmer)
for programmer in programmers:  
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
         sep=" | "
        )

