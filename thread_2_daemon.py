#  Daemon, Join, DaemonThreads
"""
    데몬 스레드 Daemon Thread
        - 백그라운드 영역에서 실행됨.
        - 메인 스레드 종료시 해당 데몬 스레드 즉시 종료(일반 스레드)
        - 자신을 생성한 스레드 종료 시 자식 데몬 스레드 즉시 종료
        - 주로 백그라운드 무한 대기 이벤트 발생을 실행하는 부분을 담는다.
            - JVM 가비지 콜렉터, word 프로세서 자동저장... 등
            - 메인이 실행 중일 때, 무한 루프 데몬 스레드를 돌려놓을 수 있다!
        - 일반 스레드는 작업 종료 시 까지 계속 실행된다.
"""

import logging
import threading

def thread_func(name, num):
    logging.info(f"Sub-Thread !{name}! : START")
    for i in num:
        if i % 1000 == 0:
            print(i)
    logging.info(f"Sub-Thread !{name}! : END")

if __name__ == "__main__":
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before Creating Thread")
    
    # Thread 생성
    # 스레드는 디버깅이 어려우므로 로그를 잘 찍어주는 것이 현직에서 중요하다.
    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Second', range(10000)), daemon=True)
    
    logging.info("Main-Thread: Before Running")
    x.start()
    y.start()
    logging.info("Main-Thread: Wait for the thread to finish")
    
    # DaemonThread 확인
    # print(x.daemon) # python 3.10+ 부터 isDaemon과 setDaemon deprecated
    # x.daemon = True
    
    # 스레드는 한 번 실행되면 메인 스레드의 종료와 상관 없이 끝까지 실행한다.
    # x.join()
    # y.join()
    # join을 만나면 자식 스레드가 끝날때까지 메인 스레드는 대기한다.
    
    logging.info("Main-Thread: All done")