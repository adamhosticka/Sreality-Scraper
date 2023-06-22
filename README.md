# Sreality Scraper

This project is a web scraping application built using Docker, consisting of multiple services:

-   **PostgreSQL Database**: Stores scraped flat data.
-   **Scrapy Framework Scraper**: Scrapes flat listings from Sreality.cz.
-   **Flask API Server**: Provides an API to display the scraped flat data.

## Prerequisites

-   Docker must be installed on your system.

## Getting Started

1.  Clone the project repository:

```bash
git clone https://github.com/adamhosticka/Sreality-Scraper.git
cd Sreality-Scraper
```

2.  Build and run the project:

```bash
docker-compose up --build
```

This command will build the Docker images and start the services.

3.  Access the Flask API server:

Once the services are up and running, you can access the Flask API server at [http://localhost:8080](http://localhost:8080/). This is where the scraped flat data will be displayed.


## Usage

-   **Scraping Flats**: The Scrapy scraper service will automatically start scraping flat listings from Sreality.cz. api. The scraped data will be stored in the PostgreSQL database.

-   **Accessing Scraped Data**: The Flask API server provides endpoints to access the scraped flat data. You can make HTTP requests to retrieve the flat data as per your requirements.
