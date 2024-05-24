from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey, TIMESTAMP, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_PORT')

Base = declarative_base()

class Language(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    language_name = Column(Text, unique=True, nullable=False)

    sources = relationship("Source", back_populates="language")

class Source(Base):
    __tablename__ = 'sources'

    id = Column(Integer, primary_key=True)
    source_name = Column(Text, nullable=False)
    source_type = Column(Text, nullable=False)
    language_id = Column(Integer, ForeignKey('languages.id'))

    language = relationship("Language", back_populates="sources")
    raw_text_data = relationship("RawTextData", back_populates="source")
    audio_data = relationship("AudioData", back_populates="source")

class RawTextData(Base):
    __tablename__ = 'raw_text_data'

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    source_id = Column(Integer, ForeignKey('sources.id'))
    date_collected = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')

    source = relationship("Source", back_populates="raw_text_data")
    cleaned_text_data = relationship("CleanedTextData", back_populates="raw_text_data")

class CleanedTextData(Base):
    __tablename__ = 'cleaned_text_data'

    id = Column(Integer, primary_key=True)
    raw_id = Column(Integer, ForeignKey('raw_text_data.id'))
    content = Column(Text)
    cleaned_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')

    raw_text_data = relationship("RawTextData", back_populates="cleaned_text_data")

class AudioData(Base):
    __tablename__ = 'audio_data'

    id = Column(Integer, primary_key=True)
    audio_path = Column(Text)
    transcript = Column(Text)
    source_id = Column(Integer, ForeignKey('sources.id'))
    date_collected = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, default='CURRENT_TIMESTAMP')

    source = relationship("Source", back_populates="audio_data")

class DataSource(Base):
    __tablename__ = 'data_sources'

    id = Column(Integer, primary_key=True)
    source_name = Column(Text, unique=True)
    source_url = Column(Text, unique=True)
    last_scraped = Column(TIMESTAMP)

if __name__ == "__main__":
    engine = create_engine('postgresql://{db_user}:{db_password}@{db_host}/{db_name}')
    Base.metadata.create_all(engine)

    # Creating a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Data models initiated successfuly!")
