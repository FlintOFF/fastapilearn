from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings
from database import Author

# Define the database URL
DATABASE_URL = 'mysql+pymysql://root:your_password@localhost:3306'

# Create the engine
engine = create_engine(settings.MYSQL_URL)

# Connect to the engine and create the database
with engine.connect() as connection:
    connection.execute(text("CREATE DATABASE IF NOT EXISTS books"))

# Recreate the engine with the new database
engine = create_engine(settings.DB_URL)

# Create the base class for declarative class definitions
Base = declarative_base()

# Bind the engine to the metadata of the Base class
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample author to the database
new_author = Author(first_name='John', last_name='Doe')
session.add(new_author)
session.commit()

# Query the authors table
for author in session.query(Author).all():
    print(f"Author ID: {author.author_id}, First Name: {author.first_name}, Last Name: {author.last_name}")
