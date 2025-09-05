'''
    Section 2
    Parallelism with Multiprocessing - join, is_alive
    Keyword = multiprocessing, processing state
    
'''

from multiprocessing import Process
import time
import logging

def proc_fn(name):
    logging.info("SUB: START %s", name)
    time.sleep(3)
    logging.info("SUB: END %s", name)
    

def main():
    # 함수 인자 확인
    p = Process(target=proc_fn, args=("First",))
    
    logging.info("MAIN: before creating process")
    
    p.start()
    
    logging.info("MAIN: Starting process")
    
    # logging.info("MAIN: Terminated Process")
    # p.terminate() # 프로세스를 바로 죽이므로 3초간 기다리지 않는다.
    
    logging.info("MAIN: Joined process")
    p.join()
    
    # 프로세스 상태 확인
    print(f"process p is alive : {p.is_alive()}")
    
    
if __name__ == "__main__":
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    main()