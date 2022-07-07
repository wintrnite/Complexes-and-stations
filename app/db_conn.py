from contextlib import contextmanager
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


@contextmanager
def create_session(**kwargs: Any) -> sessionmaker:
    new_session = Session(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except Exception:
        new_session.rollback()
        raise
    finally:
        new_session.close()
