# Dev container base image
FROM python:3.12-slim

# Set working directory
WORKDIR /workspace

# Install Python dependencies when container starts
COPY requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
