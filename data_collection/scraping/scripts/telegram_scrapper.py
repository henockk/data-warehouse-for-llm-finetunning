from pathlib import Path
from telethon import TelegramClient
from dotenv import load_dotenv
import os
import sys
from datetime import datetime  # Import datetime class

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from database.database_manager import DatabaseManager

env_path = Path('.env')
load_dotenv(env_path)
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

db_manager = DatabaseManager()

def scrape_telegram(channel_username: str = 'tikvahethiopia', url: str = '/tikvaheth') -> None:
    client = TelegramClient(channel_username, api_id, api_hash)
    async def main() -> None:
        await client.start()
        source_id = db_manager.insert_data_source(source_name=channel_username, last_scraped=datetime.now(), source_url=url) 
        entity = await client.get_entity(channel_username)
        async for message in client.iter_messages(entity):
            db_manager.insert_raw_text_data(content=message.message, source_id=source_id, date_collected=datetime.now()) 

    with client:
        client.loop.run_until_complete(main())

# Call the scrape_telegram function when the script is executed
if __name__ == "__main__":
    scrape_telegram()
