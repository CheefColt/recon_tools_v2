import requests
from bs4 import BeautifulSoup

with open("domains.txt", "r") as f:
    domains = [line.strip() for line in f]

for domain in domains:
    url = f"http://{domain}"
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        print(f"\n[+] Links for {domain}")
        for link in soup.find_all("a", href=True):
            print(link["href"])
    except Exception as e:
        print(f"[-] Error fetching {domain} → {e}")
