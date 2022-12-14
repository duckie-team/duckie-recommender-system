# Import Libraries
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
from recommender_system.config.connect import DB_URL


@contextmanager
def session_scope():
    global DB_URL
    engine = create_engine(
        DB_URL,
        encoding="utf-8"
    )
    Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


Base = declarative_base()