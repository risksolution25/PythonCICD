# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install venv module (for slim images)
RUN apt-get update && apt-get install -y python3-venv && rm -rf /var/lib/apt/lists/*

# Create virtual environment inside container
RUN python3 -m venv /app/venv

# Activate venv and upgrade pip
RUN /app/venv/bin/pip install --upgrade pip

# Copy project files
COPY . .

# Install dependencies INSIDE virtual env
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Expose app port
EXPOSE 4000

# Run using venv Python
CMD ["/app/venv/bin/python", "app.py"]
