<div align="center">
   <h1>Slickdeals Frontpage Scraper</h1>

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-orange.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![Requests](https://img.shields.io/badge/Requests-2.0-brightgreen.svg)](https://docs.python-requests.org/en/master/)

</div>

This Python script is designed to scrape the frontpage deals from [Slickdeals.net](https://slickdeals.net/).
Utilizing BeautifulSoup for HTML parsing and requests for fetching the content, the script extracts key information
such as deal titles, sale prices, and original prices. The data is then organized and written to a text file
(`frontpage.txt`) in a readable format.

## Usage

1. Ensure you have the required libraries installed:
   ```bash
   pip install beautifulsoup4 requests
   ```
2. To run the script
   ```bash
   python main.py
   ```
