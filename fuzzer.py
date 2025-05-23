import threading
import random
import string
import requests
import time

# Configuration
TARGET_URL = "http://example.com/vulnerable_endpoint"
NUM_THREADS = 10
NUM_REQUESTS_PER_THREAD = 100

# Function to generate random input
def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Fuzzing function run by each thread
def fuzz():
    for _ in range(NUM_REQUESTS_PER_THREAD):
        payload = generate_random_string(random.randint(5, 20))
        try:
            response = requests.get(TARGET_URL, params={'input': payload}, timeout=3)
            print(f"[{threading.current_thread().name}] Sent: {payload} | Status: {response.status_code}")
        except requests.RequestException as e:
            print(f"[{threading.current_thread().name}] Error: {e}")

# Create and start threads
threads = []

start_time = time.time()

for i in range(NUM_THREADS):
    t = threading.Thread(target=fuzz, name=f"Fuzzer-{i+1}")
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"\nFuzzing completed in {time.time() - start_time:.2f} seconds.")
