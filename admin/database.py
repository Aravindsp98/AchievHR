from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


database_url = "postgresql://postgres:postgres@localhost:5433/achievhr_db"




Base = declarative_base()

# Define the engine and sessionmaker as None initially
engine = None
SessionLocal = None

def get_engine():
    """
    Return the SQLAlchemy engine.
    Creates the engine if not already created.
    """
    global engine
    if engine is None:
        engine = create_engine(database_url)
    return engine

def get_session():
    """
    Return a session from the SQLAlchemy sessionmaker.
    """
    global SessionLocal
    if SessionLocal is None:
        SessionLocal = sessionmaker(autoflush=False, bind=get_engine())
    return SessionLocal()

def get_db():
    """
    Context manager to provide a database session.
    """
    db = get_session()
    try:
        yield db
    finally:
        db.close()




# Function to create tables
def init_db():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
