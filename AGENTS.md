# Repository Guidelines

## Project Structure & Module Organization

This repository has two applications. `frontend/` contains the React 19 client built with Vite: components and styles live in `frontend/src/`, imported images in `frontend/src/assets/`, and directly served files in `frontend/public/`. `backend/` contains the FastAPI service. Add routes in `main.py`, SQLAlchemy models in `model.py`, and database/session configuration in `database.py`.

## Build, Test, and Development Commands

Run frontend commands from `frontend/`:

- `npm install` installs locked JavaScript dependencies.
- `npm run dev` starts Vite with hot module replacement.
- `npm run build` creates the production bundle in `dist/`.
- `npm run lint` checks JavaScript and JSX with ESLint.
- `npm run preview` serves the production bundle locally.

For the API, run `cd backend`, copy `.env.example` to `.env`, activate a virtual environment, and install dependencies with `python -m pip install -r requirements.txt`. Start development with `uvicorn main:app --reload`. Check `/` for API availability and `/health/db` for PostgreSQL connectivity.

## Coding Style & Naming Conventions

Follow existing files: use two-space indentation and single quotes in JavaScript/JSX, and four-space indentation with standard PEP 8 conventions in Python. Name React components in PascalCase (`MenuCard.jsx`), JavaScript variables and functions in camelCase, and Python modules/functions in snake_case. Keep route handlers small and place persistent data definitions in SQLAlchemy models. Run `npm run lint` before submitting frontend changes. No Python formatter is currently configured.

## Testing Guidelines

No automated test framework or coverage threshold is configured yet. At minimum, run the frontend lint and production build, then smoke-test affected API endpoints. When introducing tests, place backend tests in `backend/tests/` using `test_*.py`; colocate frontend tests with their components using `*.test.jsx`. Add the corresponding test command and dependency configuration in the same change.

## Commit & Pull Request Guidelines

History follows Conventional Commit-style subjects such as `feat:`, `docs:`, `refactor:`, and `chore:`; use a concise, imperative description after the prefix. Pull requests should explain the change, list validation performed, and link relevant issues. Include before/after screenshots for visual updates and note database or environment changes explicitly.

## Security & Configuration

Never commit `backend/.env`, credentials, or production connection strings. Use `.env.example` as the documented template and keep local PostgreSQL settings machine-specific.
