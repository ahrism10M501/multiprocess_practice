'''
    Section 1
    Multithreading - ThreadPoolExecutor
    Keyword = Many Threads, concurrent futures, (xxx)PoolExecutor
'''
'''
    프로세서 생성 관리가 힘들다!
        -> 관련 모듈 사용
    
    그룹 스레드
    (1) python 3.2 이상 표준 라이브러리
    (2) concurrent.futures
    (3) with 사용으로 생성, 소멸 라이프사이클 관리 용이
    (4) 단점으로, 디버깅이 어렵다.(난해하다)
    (5) 대기중인 작업 -> Queue -> 완료 상태 조사 -> 결과 또는 예외 발생 -> 단일화(캡슐화)
    
'''

import time
import logging
from concurrent.futures import ThreadPoolExecutor

def task(name):
    logging.info("Sub-Thread: %s - START", name)
    result = 0
    for i in range(10001):
        result += i
    logging.info("Result: %d", result)
    logging.info("Sub-Thread: %s - END", name)

    return result
    
def main():
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating and running thread")

    # 실행 방법 1
    # max_workers : 작업의 개수가 넘어가면 직접 설정이 유리함.
    excutor = ThreadPoolExecutor(max_workers=3)

    # task1 = excutor.submit(task, ('First'))
    # task2 = excutor.submit(task, ('Second'))
    
    # with를 이용해 라이프 사이클 관리
    
    # 실행 방법 2
    with ThreadPoolExecutor(max_workers=3) as excutor:
        tasks = excutor.map(task, ('First', 'Second', 'Third'))
        
        print(list(tasks))
    
    # 결과 값이 있을 경우
    # print("task1 result ",task1.result())
    # print("task2 result ",task2.result())
    
if __name__ == "__main__":
    main()

