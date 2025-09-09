'''
    Section 3
    Concurrency, CPU Bound, I/O Bound - I/O bound Parrallel
    Keyword = I/O Bound, requests, concurrency, parrallelism
    
'''

import multiprocessing
import requests
import time

# 각 프로세스 메모리 영역에 생성되는 객체(독립적)
# 함수 실행 마다 객체 생성은 좋지 않음 -> 각 프로세스마다 할당

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()
    
def requests_all(url):
    # 세션 획득
    assert session, f"Session is {session}"
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"[{name} READ] {len(response.content)}, Status_code: {response.status_code} from {url}")

def request_all_sites(urls:list):
   # 멀티 프로세싱 실행
   # 반드시 processes 개수 조정 session 객체 확인
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(requests_all, urls)

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