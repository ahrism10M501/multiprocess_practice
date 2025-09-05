'''
    Section 1
    Multithreading - prod vs cons using Queue
    Keyword = Queue, Producer, Consumer, 생산자 소비자 패턴
    
'''
'''

    Producer-Consumer Pattern
    (1) 멀티 스레드 디자인 패턴의 정석
    (2) 서버측 프로그래밍의 핵심
    (3) 주로 허리 역할. 그만큼 중요
    
    Python Event 객체(랫치?)
    (1) Flag 초기값(0)
    (2) set() -> 1, clear() -> 0, wait() -> (1->리턴, 0->대기), is_set() -> Flag 상태 반환

'''

import threading
import concurrent.futures
import queue
import time
import logging
import random

def producer(q:queue.Queue, event: threading.Event):
    """네트워크 대기 상태라 가정(서버)

    Args:
        q (queue.Queue): _description_
        event (threading.Event): _description_
    """
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info("Producer make message: %s", message)
        q.put(message)
        
    logging.info("Producer received event Exiting")

def consumer(q:queue.Queue, event: threading.Event):
    """ 응답 받고 소비하는 것으로 가정 혹은 DB 저장

    Args:
        q (queue): _description_
        event (threading.Event): _description_
    """
    while not event.is_set() or not q.empty():
        message = q.get()
        logging.info("Consumer storing message: %s (size=%d)", message, q.qsize())
        
    logging.info("Consumer send event Exiting")
     
def main():
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # max size가 굉장히 중요하다!
    # 만약 Queue가 너무 크면 병목이 일어나거나 성능 하락을 경험하게 된다.
    pipeline = queue.Queue(maxsize=10)

    # event flag 초기값 0
    event = threading.Event()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
    
        # 실행 시간 조정
        time.sleep(0.1)
    
        logging.info("MAIN: about to set event")
    
        event.set()
    
if __name__ == "__main__":
    main()
        
