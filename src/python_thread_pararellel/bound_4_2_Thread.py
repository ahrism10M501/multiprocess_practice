'''
    Section 3
    Concurrency, CPU Bound, I/O Bound - I/O bound Parrallel
    Keyword = I/O Bound, requests, concurrency, parrallelism
    
'''

import concurrent.futures
import threading
import requests
import time

# 각 스레드에 생성되는 객체. 이름은 같지만, 각 스레드 마다 별도로 생성되는 세션
# 독립된 네임스페이스
local_thread = threading.local()
    
def get_session():
    if not hasattr(local_thread, "session"):
        local_thread.session = requests.Session()
    return local_thread.session
    
def requests_all(url):
    # 세션 획득
    session = get_session()
    with session.get(url) as response:
        print(f"[READ] {len(response.content)}, Status_code: {response.status_code} from {url}")

def request_all_sites(urls:list):
   # 멀티스레드 실행
   # 반드시 max_workers 개수 조정 session 객체 확인
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(requests_all, urls)

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