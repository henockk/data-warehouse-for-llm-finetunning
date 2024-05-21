import psycopg2
import json
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')


conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)
cur = conn.cursor()

with open('../../data_collection/raw_data/amharic_news.json', 'r') as f:
    data = json.load(f)
    for item in data:
        cur.execute("""
            INSERT INTO amharic_news (title, content, date)
            VALUES (%s, %s, %s)
        """, (item['title'], item['content'], item['date']))

conn.commit()
cur.close()
conn.close()
