FROM python:3.13-bookworm

ENV PYTHONUNBUFFERED=1
WORKDIR /app/
COPY --from=ghcr.io/astral-sh/uv:0.5.4 /uv /uvx /bin/
ENV PATH="/app/.venv/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

ENV PYTHONPATH=/app/src

COPY ./pyproject.toml .
COPY ./uv.lock .
COPY ./src /app/src

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen


CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:80","--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]



