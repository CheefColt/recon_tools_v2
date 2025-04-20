#!/bin/bash

INPUT="domains.txt"
OUTPUT="results/subdomains.txt"

mkdir -p results

echo "[+] Starting passive subdomain search..."
while read domain; do
    echo "[*] Searching: $domain"
    curl -s "https://crt.sh/?q=%25.$domain&output=json" | jq -r '.[].name_value' | sort -u >> $OUTPUT
done < $INPUT

echo "[+] Done. Results in $OUTPUT"
