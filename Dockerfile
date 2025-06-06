# Use official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy files
COPY ./app /app/app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
