import psycopg2
import json

conn = psycopg2.connect(
    dbname="datawarehouse",
    user="postgres",
    password="secret",
    host="localhost"
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
