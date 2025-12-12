# Use official Windows Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR C:\\app

# Copy files
COPY . .

# Create virtual environment
RUN python -m venv C:\app\venv

# Upgrade pip in venv
RUN C:\app\venv\Scripts\pip.exe install --upgrade pip

# Install requirements inside venv
RUN C:\app\venv\Scripts\pip.exe install -r requirements.txt

# Expose app port
EXPOSE 4000

# Run app
CMD ["C:\\app\\venv\\Scripts\\python.exe", "app.py"]
