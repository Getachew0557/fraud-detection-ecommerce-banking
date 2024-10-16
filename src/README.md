# Source Code (src) Folder

This folder contains the source code for the Flask API, model deployment, and utility functions.

## Files

- **serve_model.py**: The main Python script for serving the trained fraud detection models via Flask API.
- **utils.py**: Utility functions for data processing, feature engineering, and model loading.
- **Dockerfile**: Docker configuration to containerize the Flask app.

## Instructions

- To run the API, use: `python serve_model.py`
- For Docker containerization, build the Docker image and run it as described in the main `README.md`.