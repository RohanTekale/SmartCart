# # Base image
# FROM python:3.10-slim

# # Set environment variables to avoid bytecode creation and ensure log flushing
# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1

# # Set working directory
# WORKDIR /app

# # Install system dependencies and clean up
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     libpq-dev gcc && \
#     apt-get clean && rm -rf /var/lib/apt/lists/*

# # Copy and install Python dependencies
# COPY requirements.txt .
# RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# # Copy project files into the container
# COPY . .

# # Ensure correct permissions for entrypoint execution
# RUN chmod +x ./entrypoint.sh

# # Expose Django app port
# EXPOSE 8000

# # Use entrypoint.sh to manage setup tasks
# ENTRYPOINT ["./entrypoint.sh"]
# Base image
# FROM python:3.10-slim

# # Set environment variables to avoid bytecode creation and ensure log flushing
# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1

# # Set working directory
# WORKDIR /app

# # Install system dependencies and netcat (use netcat-openbsd)
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     libpq-dev gcc netcat-openbsd && \
#     apt-get clean && rm -rf /var/lib/apt/lists/*


# # Copy and install Python dependencies
# COPY requirements.txt .
# RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# # Copy project files into the container
# COPY . .

# # Ensure correct permissions for entrypoint execution
# RUN chmod +x ./entrypoint.sh

# # Expose Django app port
# EXPOSE 8000

# # Use entrypoint.sh to manage setup tasks
# ENTRYPOINT ["./entrypoint.sh"]


FROM python:3.10-slim

# Set environment variables to avoid bytecode creation and ensure log flushing
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies required for WeasyPrint and netcat
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev gcc netcat-openbsd \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libffi-dev \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libxml2 \
    libx11-6 \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Ensure correct permissions for entrypoint execution
RUN chmod +x ./entrypoint.sh

# Expose Django app port
EXPOSE 8000

# Use entrypoint.sh to manage setup tasks
ENTRYPOINT ["./entrypoint.sh"]
