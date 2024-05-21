import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')

# SQL statements for creating tables
TABLES = {
    "languages": """
        CREATE TABLE IF NOT EXISTS languages (
            id SERIAL PRIMARY KEY,
            language_name TEXT UNIQUE NOT NULL
        );
    """,
    "sources": """
        CREATE TABLE IF NOT EXISTS sources (
            id SERIAL PRIMARY KEY,
            source_name TEXT NOT NULL,
            source_type TEXT NOT NULL,
            language_id INTEGER REFERENCES languages(id)
        );
    """,
    "raw_text_data": """
        CREATE TABLE IF NOT EXISTS raw_text_data (
            id SERIAL PRIMARY KEY,
            content TEXT,
            source_id INTEGER REFERENCES sources(id),
            date_collected DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """,
    "cleaned_text_data": """
        CREATE TABLE IF NOT EXISTS cleaned_text_data (
            id SERIAL PRIMARY KEY,
            raw_id INTEGER REFERENCES raw_text_data(id),
            content TEXT,
            cleaned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """,
    "audio_data": """
        CREATE TABLE IF NOT EXISTS audio_data (
            id SERIAL PRIMARY KEY,
            audio_path TEXT,
            transcript TEXT,
            source_id INTEGER REFERENCES sources(id),
            date_collected DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """,
    "data_sources": """
        CREATE TABLE IF NOT EXISTS data_sources (
            id SERIAL PRIMARY KEY,
            source_name TEXT UNIQUE,
            source_url TEXT UNIQUE,
            last_scraped TIMESTAMP
        );
    """,
    "scrape_logs": """
        CREATE TABLE IF NOT EXISTS scrape_logs (
            id SERIAL PRIMARY KEY,
            source_name TEXT,
            status TEXT,
            message TEXT,
            logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
}

def create_tables():
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cur = conn.cursor()
        
        # Create each table
        for table_name, table_sql in TABLES.items():
            cur.execute(sql.SQL(table_sql))
            print(f"Table {table_name} created successfully.")
        
        # Close communication with the PostgreSQL database server
        cur.close()
        # Commit the transaction
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    create_tables()
