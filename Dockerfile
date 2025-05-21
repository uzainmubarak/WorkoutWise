FROM python:3.12-slim

RUN pip install uv

WORKDIR /app
COPY . .

# Install dependencies using lockfile
RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "fastapi", "dev"]
