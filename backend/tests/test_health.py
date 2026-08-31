"""Tests for the backend health endpoints."""

import os
from collections.abc import Generator

from fastapi.testclient import TestClient
from sqlalchemy.exc import SQLAlchemyError


os.environ.setdefault(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/spb_test",
)

from backend.database import get_db  # noqa: E402
from backend.main import app  # noqa: E402


client = TestClient(app)


class FakeSession:
    def __init__(self, error: SQLAlchemyError | None = None) -> None:
        self.error = error

    def execute(self, _statement: object) -> None:
        if self.error is not None:
            raise self.error


def successful_db_override() -> Generator[FakeSession, None, None]:
    yield FakeSession()


def failing_db_override() -> Generator[FakeSession, None, None]:
    yield FakeSession(SQLAlchemyError("contains sensitive connection details"))


def test_application_health_does_not_require_database() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_database_health_reports_reachable() -> None:
    app.dependency_overrides[get_db] = successful_db_override

    try:
        response = client.get("/health/db")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "reachable"}


def test_database_health_reports_unreachable_without_error_details() -> None:
    app.dependency_overrides[get_db] = failing_db_override

    try:
        response = client.get("/health/db")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 503
    assert response.json() == {
        "status": "error",
        "database": "unreachable",
    }
    assert "sensitive" not in response.text
