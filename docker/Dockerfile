FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    can-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy source
COPY . /app/

# Install with web extras
RUN pip install --no-cache-dir ".[web]"

# Data volume for SQLite DB, backups, and generated config files
VOLUME /data
WORKDIR /data

EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/api/live-status')" || exit 1

CMD ["open3e-web"]
