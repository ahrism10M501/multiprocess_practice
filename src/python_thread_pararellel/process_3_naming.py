'''
    Section 2
    Parallelism with Multiprocessing - naming
    Keyword = Naming, id, parallel processing

'''

from multiprocessing import Process, current_process
import os
import random
import time
import logging

def square(n):
    time.sleep(random.randint(1, 3))
    process_id = os.getpid()
    process_name = current_process().name
    
    print("id: {}, name: {}".format(process_id, process_name))
    print("Result of {} squre {}".format(n, n*n))

def main():
    # 부모 프로세스 아이디
    parent_pid = os.getpid()
    logging.info(f"ppid {parent_pid}")
    
    processes = list()
    
    # 프로세스 생성 및 실행
    for i in range(1, 100):
        # 생성
        t = Process(name=str(i), target=square, args=(i,)) # 지정하지 않으면, 임의의 4자리 숫자로 지정됨(os따라 다름)
        
        processes.append(t)
        
        # 시작
        t.start()
        
    for proc in processes:
        proc.join()

    logging.info("MAIN: END")

if __name__ == "__main__":
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    main()