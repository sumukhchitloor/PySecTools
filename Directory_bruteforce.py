import requests
import threading
import time

url = input("Enter the url: ")
wordlist = input("Enter the directory list path: ") 
extensions = ["", ".html", ".php", "/"] 
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
max_threads = 10 
request_timeout = 10
rate_limit = 0.5 

def read_wordlist():
    with open(wordlist, "r") as f:
        return [line.strip() for line in f.readlines()]

def send_request(url):
    try:
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers, timeout=request_timeout)
        if response.status_code == 200:
            print(f"[+] Found: {url}")
        elif response.status_code == 404:
            print(f"[-] Not found: {url}")
        else:
            print(f"[!] Error {response.status_code}: {url}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")

def process_wordlist():
    paths = read_wordlist()
    total_paths = len(paths) * len(extensions)
    progress = 0
    threads = []
    for path in paths:
        for ext in extensions:
            full_path = url + path + ext
            t = threading.Thread(target=send_request, args=(full_path,))
            threads.append(t)
            t.start()
           
            time.sleep(rate_limit)
            progress += 1
            print(f"[+] Progress: {progress}/{total_paths} ({round(progress/total_paths*100, 2)}%)")
   
    for t in threads:
        t.join()

if __name__ == "__main__":
    process_wordlist()
