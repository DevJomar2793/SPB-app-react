# SPB App

## Backend setup

The backend is a FastAPI application using SQLAlchemy and PostgreSQL.

```sh
cd backend
cp .env.example .env
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Set `DATABASE_URL` in `.env` to match your PostgreSQL instance. Open
`http://127.0.0.1:8000/` to check the API and
`http://127.0.0.1:8000/health/db` to check PostgreSQL connectivity.
