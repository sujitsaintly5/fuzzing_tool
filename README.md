# 🔍 Multithreaded Web Fuzzer (Python)

A simple yet effective multithreaded web fuzzer written in Python.  
This tool takes a base URL and a wordlist of paths/files, and tests each endpoint concurrently.

---

## 🚀 Features

- Multithreaded for fast scanning using `ThreadPoolExecutor`
- Takes user input for:
  - Base URL (e.g., `https://example.com`)
  - Wordlist file (e.g., `wordlist.txt`)
- Skips 404 errors and shows valid responses (e.g., 200, 403, etc.)
- Simple to extend for advanced fuzzing

---

## 🛠 Requirements

- Python 3.6+
- `requests` library

Install with:

```bash
pip install requests

```
