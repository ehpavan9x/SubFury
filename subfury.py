#!/bin/python3

# A Tool Developed By Pavan

import requests
import argparse
import pyfiglet
from concurrent.futures import ThreadPoolExecutor

banner = pyfiglet.figlet_format("Subdomain Finder")
print(banner)

parser = argparse.ArgumentParser(description="Subdomain finder by Pavan")
parser.add_argument('domain', help="Enter the domain e.g. (example.com)")
parser.add_argument('-w', '--wordlist', help="Enter the wordlist containing subdomains (default: wordlist.lst in current folder)", default="wordlist.lst")
parser.add_argument('-o', '--output', help="Enter the file name to save subdomains.")
parser.add_argument('--include-crtsh', action='store_true', help="Include subdomains from crt.sh (Certificate Transparency logs)")

args = parser.parse_args()

def fetch_from_crtsh(domain):
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    subdomains = set()
    try:
        response = requests.get(url, timeout=15)
        data = response.json()
        for entry in data:
            name = entry['name_value']
            for sub in name.split('\n'):
                subdomains.add(sub.replace("*.", "").strip())
    except Exception as e:
        print(f"[!] Error fetching from crt.sh: {e}")
    return subdomains

words = []
try:
    with open(args.wordlist, 'r') as w:
        words = w.read().splitlines()
except FileNotFoundError:
    print(f"[!] File Not Found: {args.wordlist}")
    exit(1)

crtsh_subs = set()
if args.include_crtsh:
    print("[*] Fetching subdomains from crt.sh...")
    crtsh_subs = fetch_from_crtsh(args.domain)
    if crtsh_subs:
        print(f"[+] Found {len(crtsh_subs)} subdomains from crt.sh:")
        for sub in crtsh_subs:
            print(f"    - {sub}")
    else:
        print("[!] No subdomains found from crt.sh.")

wordlist_subs = [f"{word}.{args.domain}" for word in words]
all_subs = list(set(wordlist_subs + list(crtsh_subs)))


def check_subdomain(sub):
    url = f"https://{sub}"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code in [200, 302]:
            print(f"[+] Subdomain Found: {url} (Status: {response.status_code})")
            if args.output:
                with open(args.output, "a") as out:
                    out.write(url + "\n")
    except (requests.ConnectionError, requests.Timeout):
        pass

try:
    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(check_subdomain, all_subs)
except KeyboardInterrupt:
    print("\n[!] The script was stopped by user.")
    exit(0)
