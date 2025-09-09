'''
    Section 3
    Concurrency, CPU Bound, I/O Bound - I/O bound Parrallel
    Keyword = I/O Bound, requests, concurrency, parrallelism
    
'''

import asyncio
import aiohttp
import time

# asyncio는 threading 보다 높은 코드 복잡도를 가짐. 특히 실수하면 동기로 실행됨
# requests 는 async로 쓰여지지 않았으므로 사용불가하다
# aiohttp로 해본다!
async def requests_all(session, url):
    async with session.get(url) as response:
        print("[READ] {0}, from {1}".format(response.content_length, url))

async def request_all_sites(urls:list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(urls):
           # 태스크 목록 생성
            task = asyncio.ensure_future(requests_all(session, url))
            tasks.append(task)
            print(i, end=' ')
        await asyncio.gather(*tasks, return_exceptions=True)
    
def main():
    # 테스트 URLS
    URLS = ["https://www.jython.org",
            "http://olympus.realpython.org/dice",
            "https://realpython.com"
            ] *3
    
    start_time = time.time()
    
    # 실행
    asyncio.run(request_all_sites(URLS))
    # asyncio.get_event_loop().run_until_complete(request_all_sites(URLS))
    
    duration = time.time() - start_time
    print()
    print(f"Downloaded {len(URLS)} sites in {duration}s")
    
if __name__ == "__main__":
    main()