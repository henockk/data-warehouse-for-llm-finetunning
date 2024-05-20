
-- Table to store language information
CREATE TABLE IF NOT EXISTS languages (
    id SERIAL PRIMARY KEY,
    language_name TEXT UNIQUE NOT NULL
);

-- Table to store data sources
CREATE TABLE IF NOT EXISTS sources (
    id SERIAL PRIMARY KEY,
    source_name TEXT NOT NULL,
    source_type TEXT NOT NULL,
    language_id INTEGER REFERENCES languages(id)
);

-- Table to store raw text data
CREATE TABLE IF NOT EXISTS raw_text_data (
    id SERIAL PRIMARY KEY,
    content TEXT,
    source_id INTEGER REFERENCES sources(id),
    date_collected DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store cleaned text data
CREATE TABLE IF NOT EXISTS cleaned_text_data (
    id SERIAL PRIMARY KEY,
    raw_id INTEGER REFERENCES raw_text_data(id),
    content TEXT,
    cleaned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store audio data
CREATE TABLE IF NOT EXISTS audio_data (
    id SERIAL PRIMARY KEY,
    audio_path TEXT,
    transcript TEXT,
    source_id INTEGER REFERENCES sources(id),
    date_collected DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store metadata about data sources
CREATE TABLE IF NOT EXISTS data_sources (
    id SERIAL PRIMARY KEY,
    source_name TEXT UNIQUE,
    source_url TEXT UNIQUE,
    last_scraped TIMESTAMP
);

-- Table to store logs
CREATE TABLE IF NOT EXISTS scrape_logs (
    id SERIAL PRIMARY KEY,
    source_name TEXT,
    status TEXT,
    message TEXT,
    logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
