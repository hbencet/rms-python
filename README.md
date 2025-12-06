# rms-python
Review Monitoring System - Python Service

This is a simple Python microservice that performs sentiment analysis on product reviews.

It uses a multilingual BERT model from HuggingFace to classify each review as:
positive
neutral
negative

The service is designed to work together with the main Node.js backend of the Review Monitoring System.

# How it works
The Node.js server sends a list of review texts to this service.
The Python API processes each review using a pretrained BERT model.

The model returns:
sentiment label
confidence score

The result is sent back to the Node.js backend for saving and further analysis.

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn python_api:app --host 0.0.0.0 --port 8001 --reload

The API will be available at:
http://localhost:8001

Swagger documentation is available at:
http://localhost:8001/docs

# API endpoint
POST /analyze
Send a list of review texts to analyze.


# Model used

This service uses the HuggingFace model:
nlptown/bert-base-multilingual-uncased-sentiment


It supports many languages, including English and Hungarian.

# Purpose

This microservice is part of a larger project and is responsible only for the AI logic.
All database operations and API routing are handled by the Node.js backend.

# Author
Horváth Bence Tibor - APTT01