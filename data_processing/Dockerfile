FROM node:18-alpine
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY preprocessing/ .

CMD ["python", "preprocess_am.py"]
