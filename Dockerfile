# Enterprise Production Dockerfile for Healthcare Clinic Backend API
FROM python:3.10-slim

# Prevent Python from writing bytecode and buffer outputs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn uvicorn

# Copy project source code
COPY . /app/

# Collect static files for production
RUN cd Backend && python manage.py collectstatic --noinput

WORKDIR /app/Backend

EXPOSE 8000

# Run Gunicorn with 4 workers for production execution
CMD ["gunicorn", "clinic_core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2"]
