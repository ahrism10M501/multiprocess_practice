'''
    Section 3
    Concurrency, CPU Bound, I/O Bound - what is Concurrency
    Keyword = Concurrency

'''
'''

    Concurrency (동시성)
        - CPU 가용성을 극대화 하기 위해 Parralleism의 단점 및 어려움을 소프트웨어 레벨에서 해결하기 위한 방법이다.
        - 싱글코어에서 멀티스레드 패턴으로 작업을 처리
        - 동시 작업에 있어 일정량 처리 후 다음 작업으로 넘기는 방식
        - 제어권을 주고 받으며 작업을 처리하는 패턴. 병렬적이진 않으나 유사함
        
    Concurrency vs Parralleism
        동시성:
            논리적, 동시 실행 패턴, 싱글코어, 멀티 코어에서도 가능 , 한 개를 공유 처리
            단점: 디버깅 매우매우 매ㅐ애애애우 어려움
            Mutex, DeadLock
        
        병렬성:
            물리적, 물리적인 동시 실행, 멀티코어에서만 가능, 별개의 작업
            단점: 디버깅 어려움
            OpenMP, MPI, CUDA

'''