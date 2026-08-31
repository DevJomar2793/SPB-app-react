# SPB App

## Backend setup

The backend is a FastAPI application using SQLAlchemy and PostgreSQL.

```sh
cp backend/.env.example backend/.env
backend/.venv/bin/python -m pip install -r backend/requirements.txt
source backend/.venv/bin/activate
uvicorn main:app --reload
```

Set `DATABASE_URL` in `backend/.env` to match your PostgreSQL instance. The API
starts without opening a database connection. Check process health at
`GET /health` and database connectivity at `GET /health/db`.
