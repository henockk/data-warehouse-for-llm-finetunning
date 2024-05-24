FROM python:3.12-slim
FROM apache/airflow:2.9.1


WORKDIR /app
RUN pip install --no-cache-dir scrapy

ENV AIRFLOW_HOME=/opt/airflow

COPY dags/ dags/

CMD ["webserver", "scheduler"]
