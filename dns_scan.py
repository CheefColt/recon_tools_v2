import dns.resolver
import sys

resolver = dns.resolver.Resolver()
resolver.timeout = 2

with open("domains.txt", "r") as f:
    for domain in f:
        domain = domain.strip()
        try:
            answers = resolver.resolve(domain, "A")
            for rdata in answers:
                print(f"[+] {domain} → {rdata}")
        except Exception as e:
            print(f"[!] Skipped{domain} → ({e})")
