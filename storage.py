summaries = {}

def store_summary(url, summary):
    summaries[url] = summary

def fetch_summaries():
    return "\n".join([f"{url}: {summary}" for url, summary in summaries.items()])