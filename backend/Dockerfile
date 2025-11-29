# ===================== Stage 1: Build Stage ==================
FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

# Install system dependencies needed for building Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ===================== Stage 2: Final Stage ==================
FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy app code
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
