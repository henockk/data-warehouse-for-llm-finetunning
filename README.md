# data-warehouse-for-llm-finetunning
# Amharic Data ware house for LLM finetunning

This project aims to enhance NLP capabilities for Amharic by collecting, processing, and storing text and audio data from various online sources.

## Project Structure
```
data-warehouse-for-llm-finetunning/
├── data_collection/
│ ├── spiders/
│ │ ├── blogs_spider.py
│ │ ├── news_spider.py
│ │ ├── telegram_scrapper.py
│ ├── items.py
│ ├── middlewares.py
│ ├── pipelines.py
│ ├── settings.py
├── data_processing/
│ ├── clean_data.py
│ ├── preprocess_data.py
├── database/
│ ├── schema/
│ ├── db_config.py
│ ├── database_manager.py
├── deployment/
├── api/
│ ├── app.py
│ ├── routes.py
│ ├── models.py
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ ├── App.js
│ │ ├── index.js
│ ├── package.json
├── tests/
├── docs/
├── LICENCE
└── README.md
```


## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- Node.js
- Docker

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/username/AmharicNLPDataCollection.git
    cd AmharicNLPDataCollection
    ```

2. **Install Python dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Install Node.js dependencies:**

    ```sh
    cd frontend
    npm install
    cd ..
    ```

4. **Set up the database:**

    ```sh
    python database/create_tables.py
    ```

5. **Run the project with Docker:**

    ```sh
    docker-compose up
    ```

## Usage

### Data Collection

- **Blogs:** `data_collection/spiders/blogs_spider.py`
- **Telegram:** `data_collection/spiders/telegram_spider.py`
- **Facebook:** `data_collection/spiders/facebook_spider.py`

### Data Processing

- **Cleaning and Preprocessing:** `data_processing/clean_data.py`, `data_processing/preprocess_data.py`

### API

- **Start the API server:** 

    ```sh
    cd api
    python app.py
    ```

### Frontend

- **Start the React app:**

    ```sh
    cd frontend
    npm start
    ```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Contributers