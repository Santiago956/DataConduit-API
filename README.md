# DataConduit-API

Lightweight Python API for managing quality rules and related resources.

## Overview

This repository provides a small FastAPI-based service that exposes endpoints to manage quality rules backed by SQLite (via SQLAlchemy). The code is organized into `src/` with controllers, services, repositories, models, schemas and gateways.

## Quickstart

- Create and activate a virtual environment:

  ```bash
  python -m venv .venv
  source .venv/bin/activate  # or .venv\\Scripts\\Activate.ps1 on Windows
  ```

- Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

- Run the app (development):

  ```bash
  uvicorn src.app:app --reload
  ```

## Project Layout

- `src/` — application package
  - `app.py` — FastAPI app bootstrap
  - `controller/` — route handlers
  - `service/` — business logic
  - `repository/` — data persistence implementations
  - `gateway/` — database client and setup
  - `model/` and `schema/` — SQLAlchemy models and Pydantic schemas

## Next Steps

Two planned next steps for the project:

- Unit tests: Add a test suite (e.g., `pytest`) to validate services and repositories.
- Dependency injection: Introduce DI (for example `fastapi.Depends` or a DI library) to decouple components and make testing easier.

## License

This project does not include a license file. Add one if you intend to publish or share the code.
