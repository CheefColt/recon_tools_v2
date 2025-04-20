import requests
from bs4 import BeautifulSoup
import random

user_agents = [
    "Mozilla/5.0 (ReconBot)",
    "Mozilla/5.0 (Linux; Android 11)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
]

with open("domains.txt", "r") as f:
    domains = [line.strip() for line in f]

for domain in domains:
    url = f"http://{domain}"
    try:
        headers = {"User-Agent": random.choice(user_agents)}
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        print(f"\n[+] Links for {domain}")
        for link in soup.find_all("a", href=True):
            print(link["href"])
    except Exception as e:
        print(f"[-] Error fetching {domain} → {e}")
