# Trying to impliment Singleton pattern for a simple db connection 
# using a dectorator pattern to have several instances of db connections maybe 

from sqlalchemy.ext.declarative import declarative_base
from contextlib import asynccontextmanager
from typing import Optional, AsyncGenerator

from sqlalchemy import create_engine,pool
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.orm import sessionmaker,Session,scoped_session

Base = declarative_base()

class SingletonDBManager(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DataBaseError(Exception):
    pass

