#!/bin/bash
alembic upgrade head && uvicorn app.main:app --port 8000 --reload --log-level trace