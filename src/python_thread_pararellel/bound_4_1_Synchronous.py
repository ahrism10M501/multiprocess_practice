'''
    Section 3
    Concurrency, CPU Bound, I/O Bound - I/O bound Synchronous
    Keyword = I/O Bound, requests, Synchronous
    
'''

import requests
import time

def requests_all(url, session:requests.Session):
    # print(session)
    # print(session.headers)
    # {'User-Agent': 'python-requests/2.32.5', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

    with session.get(url) as response:
        print(f'[READ] : {len(response.content)}, status_code : {response.status_code} from {url}')

def request_all_sites(urls:list):
    with requests.Session() as session:
        for url in urls:
            requests_all(url, session)

def main():
    # 테스트 URLS
    URLS = ["https://www.jython.org",
            "http://olympus.realpython.org/dice",
            "https://realpython.com"
            ] *3
    
    start_time = time.time()
    
    # 실행
    request_all_sites(URLS)
    
    duration = time.time() - start_time
    print()
    print(f"Downloaded {len(URLS)} sites in {duration}s")
    
if __name__ == "__main__":
    main()