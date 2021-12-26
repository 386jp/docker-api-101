poetry update
poetry export -f requirements.txt --output requirements.txt

# alembic revision -m "YOUR_MEMO" --autogenerate
# alembic upgrade head