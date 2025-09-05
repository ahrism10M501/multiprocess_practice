'''
    Section 1
    Multithreading - Lock, DeadLock
    Keyword = Lock, DeadLock, Race Condition, Thread sychronization
    
'''
'''

    (1) 세마포어(Semaphore) : 프로세스 간 공유 된 자원에 접근 시 문제 발생 가능성 -> 한 개의 프로세스만 접근 처리 고안(경쟁 상태 예방)
    
    (2) 뮤텍스(Mutex) : 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것.
    
    (3) Lock : 상호 배제를 위한 잠금 처리
        - 데이터 경쟁을 없애기 위한 잠금 처리
        
    (4) 데드락(DeadLock) : 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착 상태) - Systematically Fatal
    
    (5) Thread Sycronization : (4)의 문제를 스레드 동기화를 통해 안정적으로 동작하도록 처리한다. (동기화 메서드, 동기화 블럭)
    
    (6) Semaphore와 Mutex의 차이 
        - Semaphore는 프로세스 관점, Mutex는 데이터 관점
            -> 여러 프로세스가 공유된 자원에 접근하는 걸 막는 Semaphore
            -> 공유된 데이터에 여러 스레드가 접근하는 걸 막는것
            --> Semaphore는 Mutex가 될 수 있으나, 반대는 불가능
            
        - 뮤텍스 개체 = 딘일 스레드가 리소스 또는 중요 섹션을 소비 허용
        - 세마포어 = 리소스에 대한 제한된 수의 동시 엑세스 허용

'''

# 문제 상황 만들기

import time
import logging
from concurrent.futures import ThreadPoolExecutor

class FakeDataStore:
    # 공유 변수
    def __init__(self):
        # code, data, heap 영역에서 공유
        self.value = 0

    # 변수 업데이트 함수 ( 스택 영역 )
    def update(self, n):
        logging.info("Thread %s: Starting Update", n)
        
        # Mutext&락 동기화 -> 2번 파일에서 해결해본다.add()
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        
        logging.info("Thread %s: Finishin Update", n)

def main():
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # 클래스 인스턴스 화
    store = FakeDataStore()
    logging.info("Testing Update: Starting value is %d", store.value)
    
    # with Context
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)
            
    logging.info("Testing Update: Ending value is %d", store.value)
    # 3이 나와야 하는데 2가 나온다!
    # 동기화가 되지 않았기 떄문이다..!
    
if __name__ == "__main__":
    main()