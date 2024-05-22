from pathlib import Path
from telethon import TelegramClient
from dotenv import load_dotenv
import os
import datetime

from database.database_manager import DatabaseManager

env_path = Path('.env')
load_dotenv(env_path)
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

db_manager = DatabaseManager()

def scrape_telegram(channel_username: str, url: str) -> None:
    client = TelegramClient(channel_username, api_id, api_hash)
    async def main() -> None:
        await client.start()
        source_id = db_manager.insert_data_source(source_name= channel_username, last_scraped=datetime.datetime.now(), source_url=url )
        entity = await client.get_entity(channel_username)
        async for message in client.iter_messages(entity):
            db_manager.insert_raw_text_data(content=message.message,source_id=source_id, date_collected= datetime.now())

    with client:
        client.loop.run_until_complete(main())

