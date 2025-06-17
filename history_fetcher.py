import datetime

def get_history_for_today():
    # Simulated Chrome history fetcher
    return [
        {"url": "https://www.example.com", "timestamp": str(datetime.datetime.now())},
        {"url": "https://chat.openai.com/", "timestamp": str(datetime.datetime.now())},
    ]