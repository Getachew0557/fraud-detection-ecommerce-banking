# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

WORKDIR /app/tests

# Expose ports for Flask, MLflow, and Dash
EXPOSE 8000 5000 8050

WORKDIR /app/tests
# Run pytest for the tests
#CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]