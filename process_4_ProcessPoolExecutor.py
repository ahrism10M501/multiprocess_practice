'''
    Section 2
    Parallelism with Multiprocessing - ProcessPollExecutor
    Keyword = ProcessPoolExecutor, as_compeleted, futures, timeout, dict

'''

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request
import logging

# 조회 url
URLS = [
    'http://www.daum.net',
    'http://www.cnn.com',
    'http://naver.com',
    'http://velog.io/@ahrism7/posts',
    'http://github.com/'
]

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def main():
    # 프로세스 풀 Context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        # Future 로드
        future_to_url = {executor.submit(load_url, url, 5): url for url in URLS} # DICT Comprehension
        
        # 중간 확인
        # print(future_to_url) {<Future at 0x1a3be462f60 state=running>: 'https://www.daum.net', <Future at 0x1a3be463020 state=running>: 'https://www.cnn.com', <Future at 0x1a3be494710 state=running>: 'https://naver.com', <Future at 0x1a3be494920 state=running>: 'https://velog.io/@ahrism7/posts', <Future at 0x1a3be494800 state=running>: 'https://github.com/'}
        
        for future in as_completed(future_to_url):
            # key 값이 future 객체
            url = future_to_url[future]
            
            try:
                data = future.result()
                print("%r page is %d bytes" % (url, len(data)))
            except Exception as exc:
                print("%r generated an exception: %s" % (url, exc))

if __name__ == "__main__":
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    main()
    