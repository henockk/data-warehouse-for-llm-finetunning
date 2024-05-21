# root/database/scripts/insert_data.py

import psycopg2
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')


def insert_data(data, table):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cur = conn.cursor()
        
        for item in data:
            cur.execute(f"""
                INSERT INTO {table} (title, content, date_collected, source)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (source) DO NOTHING
            """, (item['title'], item['content'], item['date'], item['source']))
        
        # Commit the transaction
        conn.commit()
        cur.close()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    with open('../../data_collection/raw_data/amharic_news.json', 'r') as f:
        raw_data = json.load(f)
        insert_data(raw_data, "raw_text_data")
