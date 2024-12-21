# Scrapy Project for Web Scraping

This Scrapy project is designed for scraping data from websites, particularly focusing on extracting and processing data from **BooksToScrape.com**. The project includes creating spiders, extracting data using CSS selectors, handling pagination, cleaning data, and saving it in various formats and databases.

## Installation

1. Install Scrapy:
   ```bash
   pip install scrapy
   ```

2. (Optional) Install IPython for interactive shell usage:
   ```bash
   pip install ipython
   ```

## Project Setup

1. Create a new Scrapy project:
   ```bash
   scrapy startproject <project_name>
   ```

2. Generate a spider for the target website:
   ```bash
   scrapy genspider <spider_name> <url_to_crawl>
   ```

## Key Features

### Data Extraction

- Use the Scrapy shell to test and fine-tune your CSS selectors:
  ```bash
  scrapy shell
  ```
  Example usage:
  ```python
  response = fetch("https://books.toscrape.com/")
  titles = response.css("h3 a::text").getall()
  ```

- Extract data using the `parse` function in the spider file.

### Pagination Handling

- Navigate through multiple pages to scrape all data by updating the `parse` function to handle `next_page` links.

### Advanced Scraping

- Extract detailed data from individual book pages using a dedicated function (e.g., `parse_book_page`).
- Example data fields include:
  - Title, Price, URL
  - Product Type, Tax, Availability
  - Number of Reviews, Star Ratings
  - Category, Description

### Structuring Data with Scrapy Items

- Define data fields in the `items.py` file for validation and consistency during processing.

### Data Cleaning with Pipelines

- Use pipelines to preprocess and clean scraped data before saving it:
  - Strip whitespaces
  - Convert prices to numeric values
  - Extract availability and reviews as numbers
  - Standardize star ratings to numerical values

### Saving Data

- Save scraped data in CSV or JSON format:
  ```bash
  scrapy crawl <spider_name> -o data.json
  ```

- Configure `FEEDS` in `settings.py` for automated file saving.

### Database Integration

- Save data to a PostgreSQL database using a custom pipeline. Example table schema and insertion logic are provided in `pipelines.py`.

### Handling Anti-Scraping Mechanisms

- Use fake user agents and request headers to bypass blocking:
  - Enable dynamic user agents or browser headers using middleware.
  - Add the necessary API keys and configurations in `settings.py`.

## Running the Spider

1. Navigate to the spider directory:
   ```bash
   cd <project_name>/<spiders>
   ```

2. Run the spider:
   ```bash
   scrapy crawl <spider_name>
   ```

3. Save the output to a file:
   ```bash
   scrapy crawl <spider_name> -o output.json
   ```

## Customization

- Update `settings.py` for custom configurations like:
  - User agents
  - Middleware
  - Item pipelines

## License

This project is licensed under the MIT License. See the LICENSE file for details.
