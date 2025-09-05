'''
    Section 2
    Parallelism with Multiprocessing - Queue, Pipe
    Keyword = Queue, Pipe, Communications between Processes

'''

# 프로세스 통신 구현 Queue
from multiprocessing import Process, Queue, current_process
import time
import os

def worker(id, base_num, q):
    process_id = os.getpid()
    process_name = current_process().name
    # 누적
    sub_total = 0
    for i in range(base_num):
        sub_total += 1
        
    # producer
    q.put(sub_total)
    print(f'pid: {process_id}, pname: {process_name}, id" {id}')
    print(f'sub_total = {sub_total}')

def main():
    # 부모 프로세스 아이디
    parent_pid = os.getpid()
    print("Parent pid:", parent_pid)
    
    # 프로세스 리스트 선언
    processes = list()
    # 시작 시간
    start_time = time.time()
    total = 0
    
    # Queue 선언
    q = Queue()
    
    for i in range(20):
        # 새성
        p = Process(name=str(i), target=worker, args=(i, 100000000, q))
        processes.append(p)
        p.start()
        
    for proc in processes:
        proc.join()
    
    # 순수 계산 시간
    print(f"Execute time: {time.time()-start_time}s")
    
    # 종료 플래그
    q.put('exit')
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp
            
    print()
    print('MAIN: Total count= {}'.format(total))
    print('MAIN: END')

if __name__ == "__main__":
    main()