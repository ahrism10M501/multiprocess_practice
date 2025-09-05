
import time
import logging
import threading
from concurrent.futures import ThreadPoolExecutor

class FakeDataStore:
    # 공유 변수
    def __init__(self):
        # code, data, heap 영역에서 공유
        self.value = 0
        self._lock = threading.Lock()
        
    # 변수 업데이트 함수 ( 스택 영역 )
    def update(self, n):
        logging.info("Thread %s: Starting Update", n)
        
        # Mutext&락 동기화 -> 2번 파일에서 해결해본다.
        
        # # Lock 획득 방법 1
        # self._lock.acquire()
        # logging.info("thread %s has lock", n)
        
        # local_copy = self.value
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy
        
        # logging.info("thread %s release lock", n)
        
        # # Lock 반환 ( 방법 1 ) 
        # self._lock.release()
        
        
        # Lock 획득 방법 2
        with self._lock:
            logging.info("thread %s has lock", n)
        
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
        logging.info("thread %s release lock", n)
        
        logging.info("Thread %s: Finishing Update", n)

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