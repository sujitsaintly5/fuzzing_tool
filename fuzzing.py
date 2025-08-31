import requests
import concurrent.futures
import sys
from urllib.parse import urljoin

# Disable warnings for unverified HTTPS requests (optional)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def fuzz_url(base_url, path):
    full_url = urljoin(base_url, path.strip())
    try:
        response = requests.get(full_url, timeout=5, verify=False)
        if response.status_code != 404:
            print(f"[{response.status_code}] {full_url}")
    except requests.RequestException as e:
        print(f"[ERROR] {full_url} - {e}")

def main():
    base_url = input("Enter the base URL (e.g., https://example.com/): ").strip()
    wordlist_path = input("Enter the path to the wordlist file: ").strip()

    try:
        with open(wordlist_path, 'r') as f:
            paths = f.readlines()
    except FileNotFoundError:
        print("Error: Wordlist file not found.")
        sys.exit(1)

    print(f"\n[*] Starting fuzzing on {base_url} with {len(paths)} paths...\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(lambda path: fuzz_url(base_url, path), paths)

    print("\n[*] Fuzzing complete.")

if __name__ == "__main__":
    main()
