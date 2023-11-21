import requests
import sys

def sqli_check(url, headers):
    sql = "'.','1'),('".encode('utf-8')
    if url.find('?') != -1:
        split_url = url.split('?')
        base_url = split_url[0]
        query = split_url[1]
        queries = query.split('&')
        for query in queries:
            if query.find('=') != -1:
                key, value = query.split('=')
                check_url = f"{base_url}?{key}={value[:10]}{sql}"
                response = requests.get(check_url, headers=headers)
                if 'Unclosed' in response.text:
                    return True
                elif 'Unknown' in response.text:
                    return True
    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py [url]")
        sys.exit(1)
    url = sys.argv[1]
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    }
    if sqli_check(url, headers):
        print(f"[+] SQL Injection Vulnerability Found at {url}")
    else:
        print(f"[-] No SQL Injection Vulnerability Found at {url}")

