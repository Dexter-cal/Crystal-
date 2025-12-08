import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database directory and file
DB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'database')
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

DATABASE_URL = f"sqlite:///{os.path.join(DB_DIR, 'crystal.db')}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our models to inherit from
Base = declarative_base()

def get_db():
    """
    Dependency to get a database session.
    Yields a session to the caller and ensures it's closed afterward.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """
    Initializes the database by creating all tables defined by the models.
    This should be called once at application startup.
    """
    # Import all models here so that they are registered on the metadata.
    # Otherwise, `Base.metadata.create_all(bind=engine)` won't find them.
    # Example: from crystal.models.user import User
    Base.metadata.create_all(bind=engine)
