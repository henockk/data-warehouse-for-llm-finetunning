FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY scripts/ .

CMD ["python", "telegram_scraper.py"]
