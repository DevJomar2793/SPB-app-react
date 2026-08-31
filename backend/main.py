from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from database import get_db


app = FastAPI(title="SPB API")


@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}


@app.get("/health/db")
def database_health(db: Session = Depends(get_db)):
    """Check whether the API can connect to PostgreSQL."""

    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=503,
            detail="Database is unavailable",
        ) from error

    return {"status": "ok", "database": "reachable"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
