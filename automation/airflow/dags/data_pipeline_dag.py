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
import logging


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

def collect_data(source_type, url, **kwargs):
    if source_type == 'news':
        logging.info(f"Starting scraping news from {url}")
        scraper = AmharicNewsSpider(url=url)
        news_data = scraper.parse()
        logging.info(f"Scraped {len(news_data)} articles")
        kwargs['ti'].xcom_push(key='news_data', value=news_data)
    elif source_type == 'blogs':
        logging.info(f"Starting scraping blogs from {url}")
        scraper = BlogSpider(url=url)
        blogs_data = scraper.parse()
        logging.info(f"Scraped {len(blogs_data)} articles")
        kwargs['ti'].xcom_push(key='blogs_data', value=blogs_data)
    elif source_type == 'telegram':
        logging.info(f"Starting scraping telegram from {url}")
        telegram_data = scrape_telegram()
        logging.info(f"Scraped {len(telegram_data)} articles")
        kwargs['ti'].xcom_push(key='telegram_data', value=telegram_data)
    else:
        logging.error(f"Unknown source type: {source_type}")
    


#def scrape_news(url, **kwargs):
    #logging.info(f"Starting scraping news from {url}")
    #scraper = AmharicNewsSpider(url=url)
    #news_data = parse()
    #logging.info(f"Scraped {len(news_data)} articles")
    # Push the result to XCom
    #kwargs['ti'].xcom_push(key='news_data', value=news_data)

#def scrape_blogs(url, **kwargs):
    #logging.info(f"Starting scraping blogs from {url}")
    #scraper = BlogSpider(url=url)
    #blogs_data = scraper.parse()
    #logging.info(f"Scraped {len(blogs_data)} articles")
    # Push the result to XCom
    #kwargs['ti'].xcom_push(key='blogs_data', value=blogs_data)

#def telegram_scraping(url, **kwargs):
    #logging.info(f"Starting scraping telegram from {url}")
    #telegram_data = scrape_telegram()
    #logging.info(f"Scraped {len(telegram_data)} articles")
    # Push the result to XCom
    #kwargs['ti'].xcom_push(key='news_data', value=telegram_data)


def process_data():
    # Implement data processing logic here
    news_data = kwargs['ti'].xcom_pull(task_ids='scrape_news_task', key='news_data')
    if not news_data:
        logging.error("No news data found")
        return

    session = SessionLocal()
    try:
        for article in news_data:
            db_data = create_data(session, article)
            session.add(db_data)
        session.commit()
        logging.info("News data saved to database successfully")
    except Exception as e:
        session.rollback()
        logging.error(f"Error saving to database: {e}")
        raise e
    finally:
        session.close()


collect_task = PythonOperator(
    task_id='collect_data',
    python_callable=collect_data,
    op_kwargs={'source_type': 'news', 'url': 'http://example.com/news'},
    provide_context=True,
    dag=dag,
)

process_task = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag,
)

collect_task >> process_task
