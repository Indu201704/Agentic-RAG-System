import requests
from bs4 import BeautifulSoup
import logging

def scrape_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return ' '.join([p.get_text() for p in paragraphs])
    except Exception as e:
        logging.error(f"Error scraping {url}: {e}")
        return None