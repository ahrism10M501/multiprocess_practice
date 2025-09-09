'''
    Section 3
    Concurrency, CPU Bound, I/O Bound - AsyncIO
    Keyword = IO Bound, asyncio

'''
'''

    동시 프로그래밍 패러다임 변화
        - 싱글 코어 -> 처리향상 미미, 저하 -> 비동기 프로그래밍 대두!
        - Nginx와 apache 차이
        - CPU 연산, DB연동, API 호출 대기 시간이 늘어남 -> 다른 일을 하자..! -> Async Non-blocking
    
    > python 3.4: 비동기(asyncio) 표준 라이브러리 등장

'''

import time
import asyncio

def exe_calc_sync(name, n):
    for i in range(1, n+1):
        print(f"{name} -> {i} of {n}")
        time.sleep(1)
    print(f"{name} - {n} is done!")

def process_sync():
    start = time.time()
    exe_calc_sync("one", 3)
    exe_calc_sync("two", 2)
    exe_calc_sync("thr", 1)
    end = time.time()
    print(f">> Total: {end - start}")

# 비동기 함수 안에서 비동기 함수를 실행 할 때는 await를 붙여야 한다!
# 안 붙이면 동기처리 혹은 예외처리 됨
# Async가 붙으면 coroutine object가 반환됨
async def exe_calc_async(name, n):
    for i in range(1, n+1):
        print(f"{name} -> {i} of {n}")
        await asyncio.sleep(1)
    print(f"{name} - {n} is done!")

async def process_async():
    start = time.time()
    
    # 3.11 이상에서는 불가함
    # await asyncio.wait([
    #     exe_calc_async("one", 3),
    #     exe_calc_async("two", 2),
    #     exe_calc_async("thr", 1)])

    # 3.11 이상에서는 다음 두 방법 사용
    # task_one = asyncio.create_task(exe_calc_async("one", 3))
    # task_two = asyncio.create_task(exe_calc_async("two", 2))
    # task_thr = asyncio.create_task(exe_calc_async("thr", 1))
    # await asyncio.wait([task_one, task_two, task_thr])
    
    # 코루틴을 태스크로 변환해 동시에 실행
    await asyncio.gather(
        exe_calc_async("one", 3),
        exe_calc_async("two", 2),
        exe_calc_async("thr", 1)
    )
    
    end = time.time()
    print(f">> Total: {end - start}")

if __name__ == "__main__":
    # process_sync()
    
    # 파이썬 3.7 이상
    asyncio.run(process_async())
    
    # 파이썬 3.7 이하
    #asyncio.get_event_loop().run_until_complete(process_async())




