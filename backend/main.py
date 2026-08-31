"""FastAPI application entry point."""

import logging

from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from .database import get_db
from .schema import DatabaseHealthResponse, HealthResponse


logger = logging.getLogger(__name__)

app = FastAPI(title="SPB API")


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Report whether the API process is running."""

    return HealthResponse()


@app.get(
    "/health/db",
    response_model=DatabaseHealthResponse,
    responses={503: {"model": DatabaseHealthResponse}},
)
def database_health_check(
    db: Session = Depends(get_db),
) -> DatabaseHealthResponse | JSONResponse:
    """Report PostgreSQL connectivity without leaking connection details."""

    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError:
        logger.warning("Database health check failed", exc_info=True)
        response = DatabaseHealthResponse(
            status="error",
            database="unreachable",
        )
        return JSONResponse(status_code=503, content=response.model_dump())

    return DatabaseHealthResponse(status="ok", database="reachable")
