# Use official Windows Python image
FROM python:3.10-slim

# Set working directory
WORKDIR C:/app

# Copy project files into container
COPY . .

# Create virtual environment
RUN python -m venv venv

# Activate venv and upgrade pip
RUN venv\Scripts\pip.exe install --upgrade pip

# Install dependencies inside virtual environment
RUN venv\Scripts\pip.exe install --no-cache-dir -r requirements.txt

# Expose the app port
EXPOSE 4000

# Run the app using venv Python
CMD ["C:\\app\\venv\\Scripts\\python.exe", "app.py"]
