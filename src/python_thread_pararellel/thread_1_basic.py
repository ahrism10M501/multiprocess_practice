"""
    Section 1
    Multithreading - Difference between Process and Thread
    Keyword = Process, Thread
    
    운영체제에 관련한 내용을 깊이 알고 있는 것은 굉장히 중요하다.
    이런 쓰레드에 대한 내용을 잘 알면 취직에 유리할 뿐더러 훨씬 깊고 좋은 코드를 작성 할 수 있다.
    
    ++ (1) 프로세스 Process ++
        - 운영체제에게서 할당 받는 자원의 단위(실행 중인 프로그램)
        - CPU 동작 시간, 주소 공간(독립적)
        - Code, Data, Stack, Heap -> 독립적
        - 최소 1개의 메인 스레드 보유 (5개의 프로세스 -> 50개의 스레드 마냥)
        - 파이프, 파일, 소켓 등을 사용해서 프로세스 간 통신(Cost 높음) -> Context Switching
    
    ++ (2) 스레드 thread ++
        - 프로세스 내에 실행 흐름 단위
        - 프로세스 자원 사용
        - Stack 만 별도로 할당하고 나머지는 공유한다 (Code, Data, Heap)
        - 메모리 공유(변수 공유)
        - 한 스레드의 결과가 다른 스레드에 영향을 끼침
        
    ++ (3) 멀티 스레드 Multi Thread ++
        - 한 개의 단일 어플리케이션(응용프로그램) -> 여러 스레드로 구성 후 작업 처리
        - 시스템 자원 소모 감소(효율성, 처리량 증가)
        - 통신 부감 감소, 디버깅 어려움, 단일 프로세스에는 효과가 미약함
        - 자원 공유 문제(교착 상태), 프로세스에 영향을 준다.
        
    ++ (4) 멀티 프로세스 Multi Process ++
        - 한 개의 단일 어플리케이션(응용프로그램) -> 여러 프로세스로 구성 후 작업 처리
        - 한 개의 프로세스 문제 발생은 확산하지 않음(프로세스 Kill)
        - 캐시 체인지, Cost 비용 매우 높음(오버레드) -> 복잡한 통신 방식으로 인해
        
    --- --- --- --- --- --- ---
    
    Section 1
    Multithreading - Python's GIL
    Keyword = CPython, 메모리 관리, GIL 사용 이유
    
    Python GIL?
        - Global Interpreter Lock
        - Python 실행 -> Cpython -> Python(bytecode) 실행 시 여러 Thread를 사용할 경우
        - 멀티 스레드로 코드를 작성해도 I/O Bound를 만나면 한 타임에 하나만 접속하도록 제한함
             -> 싱글 스레드에서 파이썬이 제일 성능이 잘 나와서, 파이썬 개발자가 내부적으로 막아 놓았다.
        - 단일 스레드만이 Python.object에 접근하게 제한하는 mutex
            -> CPython 메모리 관리가 취약하기 떄문(즉, Thread-safe)
        - 프로세스 사용 가능(numpy, torch, scipy) GIL 외부에서 효율적인 코딩
        ---- GIL이 Python을 안 좋은 언어로 만들지 않는다.
        - 병렬 처리는 MultiProcessing, asyncio 등 선택지가 다양하다
        -(파이썬에서) Thread 동시성 완벽 처리를 위해, Jython(자바에서 파이썬), IronPython, Stackless Python 등의 다른 언어도 있다.
        
    --- --- --- --- --- --- ---
    Section 3
    Multithreading - THread Basic 1
    Keyword = Threading basic
    
"""

import logging
import threading
import time

def thread_func(name):
    logging.info(f"Sub-Thread !{name}! : START")
    time.sleep(3)
    logging.info(f"Sub-Thread !{name}! : END")

if __name__ == "__main__":
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before Creating Thread")
    
    # Thread 생성
    # 스레드는 디버깅이 어려우므로 로그를 잘 찍어주는 것이 현직에서 중요하다.
    x = threading.Thread(target=thread_func, args=('First', ))
    
    logging.info("Main-Thread: Before Running")
    x.start()
    logging.info("Main-Thread: Wait for the thread to finish")
    
    # 스레드는 한 번 실행되면 메인 스레드의 종료와 상관 없이 끝까지 실행한다.
    x.join()
    # join을 만나면 자식 스레드가 끝날때까지 메인 스레드는 대기한다.
    
    logging.info("Main-Thread: All done")