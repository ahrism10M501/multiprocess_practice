'''
    Section 3
    Concurrency, CPU Bound, I/O Bound - MultiProcessing vs Threading vs Async IO
    Keyword = CPU bound, IO bound, AsyncIO

'''
'''

    CPU bound vs IO bound
        CPU Bound
            - 주로 프로세스 진행 -> CPU 성능에 의존
            - 행렬곱, 고속연산, 파일압축, 집합연산 등에 적합
            - CPU연산 위주 작업
    
        I/O bound
            - 파일쓰기, 디스크 작업, 네트워크 통신, 시리얼 포트 송수신
            - 작업에 따라(병목) 수행시간 결정됨
            - CPU 성능 지표가 수행시간 단축에 큰 영향을 끼치지 않음
        
    메모리 바인딩, 캐시바운딩
        - 작업 목적에 따라서 적절한 동시성 라이브러리 선택이 중요하다
        
    최종 비교!
    MultiProcessing
        - Multiple Processes, 고가용성(CPU) Utilization -> CPU Bound
        - 10개의 부엌, 10명의 요리사, 10개의 요리
        
    Threading
        - Single(Multi) Process, Multiple Threads, OS decides task switching(코스트 발생)
        - Fast I/O Bound
        - 1개의 부엌, 10명의 요리사, 10개의 요리
        
    AsyncIO
        - Single Process, Single Threads, Coperative Multitasking
        - Tasks cooperatively decide switching
        - Slow I/O Bound
        - 1개의 부엌, 1명의 요리사, 10개의 요리
        
'''