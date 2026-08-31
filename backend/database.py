"""PostgreSQL connection and database session setup."""

import os
from collections.abc import Generator
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


# Load values from backend/.env before reading DATABASE_URL.
ENV_FILE = Path(__file__).with_name(".env")
load_dotenv(ENV_FILE)

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(f"DATABASE_URL is missing from {ENV_FILE}")


class Base(DeclarativeBase):
    """Base class shared by all database models."""


# The engine manages connections to PostgreSQL.
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Each API request receives its own database session.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


def get_db() -> Generator[Session, None, None]:
    """Open a database session for one request and close it afterward."""

    with SessionLocal() as session:
        yield session
