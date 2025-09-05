'''
    Section 2
    Parallelism with Multiprocessing - Queue, Pipe
    Keyword = Queue, Pipe, Communications between Processes

'''

# 프로세스 통신 구현 Queue
from multiprocessing import Process, Pipe, current_process
import time
import os

def worker(id, base_num, conn):
    process_id = os.getpid()
    process_name = current_process().name
    # 누적
    sub_total = 0
    for i in range(base_num):
        sub_total += 1
        
    # producer
    conn.send(sub_total)
    conn.close()
    
    print(f'pid: {process_id}, pname: {process_name}, id" {id}')
    print(f'sub_total = {sub_total}')

def main():
    # 부모 프로세스 아이디
    parent_pid = os.getpid()
    print("Parent pid:", parent_pid)
    
    # 시작 시간
    start_time = time.time()
    total = 0
    
    # Pipe 선언
    parent_conn, child_conn = Pipe()
    
    p = Process(name=str(1), target=worker, args=(1, 100000000, child_conn))
    p.start()
    p.join()
    
    # 순수 계산 시간
    print(f"Execute time: {time.time()-start_time}s")
    print()
    print('MAIN: Total count= {}'.format(parent_conn.recv()))
    print('MAIN: END')

if __name__ == "__main__":
    main()