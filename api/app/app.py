from flask import Flask, request, jsonify
from models.data_models import Base, Language, Source, RawTextData, CleanedTextData, AudioData, DataSource
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_PORT')

app = Flask(__name__)


DATABASE_URL = 'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/languages', methods=['GET'])
def get_languages():
    query = session.query(Language)
    search = request.args.get('search')
    sort = request.args.get('sort', 'id')
    order = request.args.get('order', 'asc')

    if search:
        query = query.filter(Language.language_name.ilike(f'%{search}%'))

    if order == 'asc':
        query = query.order_by(asc(getattr(Language, sort, 'id')))
    else:
        query = query.order_by(desc(getattr(Language, sort, 'id')))

    languages = query.all()
    return jsonify([lang.language_name for lang in languages])

@app.route('/sources', methods=['GET'])
def get_sources():
    query = session.query(Source)
    search = request.args.get('search')
    sort = request.args.get('sort', 'id')
    order = request.args.get('order', 'asc')

    if search:
        query = query.filter(Source.source_name.ilike(f'%{search}%'))

    if order == 'asc':
        query = query.order_by(asc(getattr(Source, sort, 'id')))
    else:
        query = query.order_by(desc(getattr(Source, sort, 'id')))

    sources = query.all()
    return jsonify([{'source_name': src.source_name, 'source_type': src.source_type} for src in sources])

@app.route('/raw_text_data', methods=['GET'])
def get_raw_text_data():
    query = session.query(RawTextData)
    search = request.args.get('search')
    sort = request.args.get('sort', 'id')
    order = request.args.get('order', 'asc')

    if search:
        query = query.filter(RawTextData.content.ilike(f'%{search}%'))

    if order == 'asc':
        query = query.order_by(asc(getattr(RawTextData, sort, 'id')))
    else:
        query = query.order_by(desc(getattr(RawTextData, sort, 'id')))

    raw_text_data = query.all()
    return jsonify([{'content': data.content, 'date_collected': data.date_collected} for data in raw_text_data])

@app.route('/cleaned_text_data', methods=['GET'])
def get_cleaned_text_data():
    query = session.query(CleanedTextData)
    search = request.args.get('search')
    sort = request.args.get('sort', 'id')
    order = request.args.get('order', 'asc')

    if search:
        query = query.filter(CleanedTextData.content.ilike(f'%{search}%'))

    if order == 'asc':
        query = query.order_by(asc(getattr(CleanedTextData, sort, 'id')))
    else:
        query = query.order_by(desc(getattr(CleanedTextData, sort, 'id')))

    cleaned_text_data = query.all()
    return jsonify([{'content': data.content, 'cleaned_at': data.cleaned_at} for data in cleaned_text_data])

@app.route('/audio_data', methods=['GET'])
def get_audio_data():
    query = session.query(AudioData)
    search = request.args.get('search')
    sort = request.args.get('sort', 'id')
    order = request.args.get('order', 'asc')

    if search:
        query = query.filter(AudioData.transcript.ilike(f'%{search}%'))

    if order == 'asc':
        query = query.order_by(asc(getattr(AudioData, sort, 'id')))
    else:
        query = query.order_by(desc(getattr(AudioData, sort, 'id')))

    audio_data = query.all()
    return jsonify([{'audio_path': data.audio_path, 'transcript': data.transcript, 'date_collected': data.date_collected} for data in audio_data])

@app.route('/data_sources', methods=['GET'])
def get_data_sources():
    query = session.query(DataSource)
    search = request.args.get('search')
    sort = request.args.get('sort', 'id')
    order = request.args.get('order', 'asc')

    if search:
        query = query.filter(DataSource.source_name.ilike(f'%{search}%'))

    if order == 'asc':
        query = query.order_by(asc(getattr(DataSource, sort, 'id')))
    else:
        query = query.order_by(desc(getattr(DataSource, sort, 'id')))

    data_sources = query.all()
    return jsonify([{'source_name': data.source_name, 'source_url': data.source_url, 'last_scraped': data.last_scraped} for data in data_sources])

if __name__ == '__main__':
    app.run(debug=True)
