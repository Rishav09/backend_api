FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /usr/src/app

ENV UV_NO_DEV=1 \
    UV_NO_EDITABLE=1

COPY pyproject.toml uv.lock ./

RUN uv sync --no-install-project

COPY . .

RUN uv sync --locked

CMD [".venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
