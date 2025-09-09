'''
    Section 3
    Concurrency, CPU Bound, I/O Bound - CPU bound multiprocessing
    Keyword = CPU Bound, multiprocessing
    
'''
import os
import time
from multiprocessing import current_process, Array, Value, Manager, Process, freeze_support

def cpu_bound(n, total_list):
    pid = os.getpid()
    pname = current_process().name
    
    # Process 정보 출력
    print(f"Process ID: {pid}, Process Name :{pname}")
    
    total_list.append(sum(i*i for i in range(n)))

def main():
    numbers = [3_000_000 + x for x in range(30)]
    
    # 프로세스 리스트 삽입
    processes = list()
    manager = Manager()
    
    # 리스트 획득( 프로세스 공유 리스트 )
    total_list = manager.list()
    
    st_ = time.time()
    
    # 프로세스 생성 및 실행
    for i in numbers:
        # 프로세스 생성
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list))
        processes.append(t)
        t.start()
        
    for proc in processes:
        proc.join()
    
    ed_ = time.time()
    print()
    print(f"Total : {total_list}")
    print(f'sum : {sum(total_list)}')
    duration = ed_ - st_
    print(f"Dutarion : {duration}s")

if __name__ == "__main__":
    # freeze_support() # 윈도우에서 오류 발생 시 해결사
    main()