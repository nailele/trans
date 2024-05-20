FROM python:3.11

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install poetry
RUN poetry install --no-dev

COPY . .

CMD ["poetry", "run", "uvicorn", "translation_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
