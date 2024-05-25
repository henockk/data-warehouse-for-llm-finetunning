from pathlib import Path
from telethon import TelegramClient
from dotenv import load_dotenv
from datetime import datetime 
import asyncio
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from database.database_manager import DatabaseManager

env_path = Path('.env')
load_dotenv(env_path)
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

db_manager = DatabaseManager()

channels = [
    'tikvahethiopia',
    'tikvahethmagazine',
    'tikvahethsport',
    'lighthouselearningcenter',
    'Ethiobooks',
    'Bookshelf13',
    'Eliasmeserett',
    'amharic_poems',
    'alainamharic'
]

async def scrape_telegram(channel_username: str, url: str) -> None:
    async with TelegramClient(channel_username, api_id, api_hash) as client:
        async def main() -> None:
            source_id = await db_manager.insert_data_source(source_name=channel_username, last_scraped=datetime.now(), source_url=url)
            entity = await client.get_entity(channel_username)
            async for message in client.iter_messages(entity):
                db_manager.insert_raw_text_data(content=message.message, source_id=source_id, date_collected=datetime.now())

        await main()

async def main():
    for channel_username in channels:
        print(f"Scraping channel: {channel_username}")
        await scrape_telegram(channel_username=channel_username, url=channel_username)

if __name__ == "__main__":
    asyncio.run(main())


