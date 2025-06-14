#!/bin/python3

# A Tool Developed By Pavan


import requests
import argparse
import pyfiglet

banner = pyfiglet.figlet_format("Subdomain Finder")
print(banner)

parser = argparse.ArgumentParser(description="Subdomain finder by Pavan")

parser.add_argument('domain', help="Enter the domain e.g. (example.com)")
parser.add_argument('-w', '--wordlist', help="Enter the wordlist containing subdomains (default: wordlist.lst in current folder)", default="wordlist.lst")
parser.add_argument('-o', '--output', help="Enter the file name to save subdomains.")

args = parser.parse_args()  

try:
    with open(args.wordlist, 'r') as w:  
        words = w.read().splitlines()
except FileNotFoundError:
    print(f"File Not Found: {args.wordlist}")  
    exit(1)

try:
    for word in words:
        protocols = ['https']

        for protocol in protocols:
            url = f"{protocol}://{word}.{args.domain}"  
            try:
                response = requests.get(url, timeout=2)
                if response.status_code in [200, 302]:
                    print(f"[+] Subdomain Found: {url} (Status: {response.status_code})")

                    if args.output:
                        with open(args.output, "a") as out:
                            out.write(url + "\n")
                    break
            except (requests.ConnectionError, requests.Timeout):
                continue
except KeyboardInterrupt:
    print("\n[!] The script was stopped by user.")
    exit(0)
