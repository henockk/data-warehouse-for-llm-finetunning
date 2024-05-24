from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from database.database_manager import DatabaseManager
from api.models.database import Base
from data_collection.scraping.scripts.news_spider import AmharicNewsSpider
from data_collection.scraping.scripts.blog_spider import BlogSpider
from data_collection.scraping.scripts.telegram_scrapper import scrape_telegram


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='A simple data pipeline',
    schedule_interval=timedelta(days=1),
)

def scrape_news(url, **kwargs):
    logging.info(f"Starting scraping news from {url}")
    scraper = AmharicNewsSpider(url=url)
    news_data = parse()
    logging.info(f"Scraped {len(news_data)} articles")
    # Push the result to XCom
    kwargs['ti'].xcom_push(key='news_data', value=news_data)

def scrape_blogs(url, **kwargs):
    logging.info(f"Starting scraping blogs from {url}")
    scraper = BlogSpider(url=url)
    blogs_data = scraper.parse()
    logging.info(f"Scraped {len(blogs_data)} articles")
    # Push the result to XCom
    kwargs['ti'].xcom_push(key='blogs_data', value=blogs_data)

def telegram_scraping(url, **kwargs):
    logging.info(f"Starting scraping telegram from {url}")
    telegram_data = scrape_telegram()
    logging.info(f"Scraped {len(telegram_data)} articles")
    # Push the result to XCom
    kwargs['ti'].xcom_push(key='news_data', value=telegram_data)


def process_data():
    # Implement data processing logic here
    pass

collect_task = PythonOperator(
    task_id='collect_data',
    python_callable=collect_data,
    dag=dag,
)

process_task = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag,
)

collect_task >> process_task
