'''
    Section 2
    Parallelism with Multiprocessing - Sharing State
    Keyword = memory sharing, array, value

'''

from multiprocessing import Process, current_process
import os

# 프로세스 메모리 공유 예제(공유 X)
def gen_update_number(v: int):
    for _ in range(50):
        v += 1
    print(current_process().name, ", data: ", v)

def main():
    # 부모 프로세스 아이디
    parent_pid = os.getpid()
    print(f"Parent pid: {parent_pid}")
    
    processes = list()
    # 프로세스 메모리 공유 변수
    shared_value = 0
    
    for _ in range(1, 10):
        p = Process(target=gen_update_number, args=(shared_value, ))
        processes.append(p)
        p.start()
        
    for proc in processes:
        proc.join()
    
    print(f"Final data in parent process: {shared_value}")
    
if __name__ == "__main__":
    main()