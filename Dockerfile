FROM python:3.12-slim

# ⬇ Pull uv binary from prebuilt image (fast, reliable)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# ⬇ Copy code and install with strict mode
COPY . /app
WORKDIR /app
RUN uv sync --frozen --no-cache  # frozen = must match lockfile

# ⬇ Run FastAPI via the actual venv binary
CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]
