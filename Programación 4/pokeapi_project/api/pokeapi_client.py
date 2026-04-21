import requests
import time
from config import BASE_URL, TIMEOUT, RETRIES, SLEEP_BETWEEN_REQUESTS

def get(endpoint):
    url = endpoint if endpoint.startswith("http") else f"{BASE_URL}/{endpoint}"

    for attempt in range(RETRIES):
        try:
            res = requests.get(url, timeout=TIMEOUT)
            res.raise_for_status()
            time.sleep(SLEEP_BETWEEN_REQUESTS)
            return res.json()
        except requests.exceptions.RequestException as e:
            if attempt == RETRIES - 1:
                print(f"[ERROR] {url} -> {e}")
                return None