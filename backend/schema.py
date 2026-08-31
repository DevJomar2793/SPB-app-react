"""Pydantic response schemas exposed by the API."""

from typing import Literal

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Application process health response."""

    status: Literal["ok"] = "ok"


class DatabaseHealthResponse(BaseModel):
    """Database connectivity health response."""

    status: Literal["ok", "error"]
    database: Literal["reachable", "unreachable"]
