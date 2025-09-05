'''
    Section 2
    Parallelism with Multiprocessing - Sharing State
    Keyword = memory sharing, array, value

'''

from multiprocessing import Process, current_process, Value, Array
import os

# 프로세스 메모리 공유 예제(공유 O)
def gen_update_number(v):
    for _ in range(50):
        v.value += 1
    print(current_process().name, ", data: ", v.value)

def main():
    # 부모 프로세스 아이디
    parent_pid = os.getpid()
    print(f"Parent pid: {parent_pid}")
    
    processes = list()
    # 프로세스 메모리 공유 변수
    # from multiprocess import shared_memory 사용 가능(파이썬 >3.8)
    # from multiprocess import Manager
    shared_value = Value('i', 0)
    """
    typecode_to_type = {
    'c': ctypes.c_char,     'u': ctypes.c_wchar,
    'b': ctypes.c_byte,     'B': ctypes.c_ubyte,
    'h': ctypes.c_short,    'H': ctypes.c_ushort,
    'i': ctypes.c_int,      'I': ctypes.c_uint,
    'l': ctypes.c_long,     'L': ctypes.c_ulong,
    'q': ctypes.c_longlong, 'Q': ctypes.c_ulonglong,
    'f': ctypes.c_float,    'd': ctypes.c_double
    }
    """
    
    for _ in range(1, 10):
        p = Process(target=gen_update_number, args=(shared_value, ))
        processes.append(p)
        p.start()
        
    for proc in processes:
        proc.join()
    
    print(f"Final data in parent process: {shared_value.value}")
    
if __name__ == "__main__":
    main()