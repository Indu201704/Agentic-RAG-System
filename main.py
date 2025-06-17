import time
import logging
from history_fetcher import get_history_for_today
from scraper import scrape_website_content
from summarizer import summarize_content
from storage import store_summary, fetch_summaries

logging.basicConfig(level=logging.INFO)

def process_chrome_history():
    chrome_history = get_history_for_today()
    logging.info("Starting to process Chrome history...")
    for url_data in chrome_history:
        url = url_data['url']
        logging.info(f"Processing URL: {url}")
        content = scrape_website_content(url)
        if content:
            summary = summarize_content(content)
            if summary:
                store_summary(url, summary)
                logging.info(f"Summary for {url}: {summary}")
            else:
                logging.warning(f"Failed to summarize content for {url}")
        else:
            logging.warning(f"Failed to fetch content for {url}")
        time.sleep(1)

def answer_query(query):
    if query.lower() == "what have i learned today?":
        return fetch_summaries()
    return "Sorry, I didn't understand that query."

if __name__ == "__main__":
    process_chrome_history()
    print(answer_query("What have I learned today?"))