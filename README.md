<h1 align="center">🔥 SubFury - Subdomain Finder</h1>

<p align="center">
  <b>Find subdomains quickly using Python. Supports HTTP/HTTPS, wordlists, and output saving.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Author-Pavan-blue.svg">
  <img src="https://img.shields.io/badge/Tool-Subdomain--Finder-green.svg">
  <img src="https://img.shields.io/badge/Made%20With-Python3-yellow.svg">
</p>

---

## 🚀 Features


- 🔎 Scans for subdomains using your own or default wordlist  
- 🌐 Supports `https` protocol only (no noise from `http`)  
- 🔗 Fetches subdomains directly from [crt.sh](https://crt.sh) using `--include-crtsh`  
- 🧵 Fast multithreaded scanning using Python's `ThreadPoolExecutor`  
- 💾 Save found subdomains to an output file using `-o`  
- ⚡ Beginner-friendly and easy to use  
- 💥 Graceful exit with `Ctrl + C`  
- 🧠 Merges wordlist + crt.sh results without duplicates  

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/subfury.git

2. Navigate into the folder
cd SubFury

3. Install requirements
pip install -r requirements.txt
```

**Usage**

🚀 Basic Usage
```
python3 subfury.py example.com
```
🔍 With Wordlist
```
python3 subfury.py example.com -w wordlist.txt
```

🌐 Include crt.sh Subdomains
```
python3 subfury.py example.com --include-crtsh
```

💾 Save Output to File
```
python3 subfury.py example.com -o output.txt
```

🧩 Combine All Options
```
python3 subfury.py example.com -w wordlist.txt --include-crtsh -o output.txt
```

**Sample Output**
```
[+] Subdomain Found: http://admin.example.com (Status: 200)
[+] Subdomain Found: https://mail.example.com (Status: 302)
```

**🧾 Requirements**
```Use the below commmand:
pip3 install -r requirements.txt
```

**👨‍💻 Author**
```
Pavan
🔗 https://pavansec.pro
💬 Young cybersecurity enthusiast from India 🇮🇳
```

**⚠️ Disclaimer**
```
This tool is for educational and authorized security testing only. Do not use on systems you don’t own or have permission to test.
```

⭐ If you like this tool, give it a star on GitHub to support the project!



