'''
    Section 3
    Concurrency, CPU Bound, I/O Bound - Blocking vs Non-blocking
    Keyword = Blocking IO, Non-blocking IO, Sync, Async

'''
'''

    Blocking IO vs Non-Blocking IO
        Blocking IO
            - 시스템 콜 요청시 -> 커널 IO 작업 완료까지 응답 대기
            - 카톡 보내놓고 답장 올때까지 계속 카톡만 보고 있기
            - 제어권: IO -> 커널 소유 -> 응답(Respoense) 전 까지 대기(Block) = 다른 작업 수행 불가
        
        Non-blocking IO
            - 시스템 콜 요청시 -> 커널 IO 작업 완료 여부 상관없이 즉시 응답
            - 카톡 보내놓고 딴거 하다가 응답 오면 확인하기(call bcak)
            - 제어권: IO -> 유저 프로세스 -> 다른 작업 수행 가능 -> 주기적으로 시스템 콜을 통해 IO 작업 완료 여부 확인 (이건 디자인 패턴으로 해결 가능하다!)
            
    Async vs Sync
        Async
            - IO 작업 완료 여부에 대한 Noty는 커널(호출되는 함수) -> 유저프로세스(호출하는 함수)
        Sync
            - IO 작업 완료 여부에 대한 NOty는 유저프로세스(호출하는 함수) -> 커널(호출되는 함수)
            
    Sync Blocking IO
    Async Blocking IO
    Sync Non-blocking IO
    Async Non-blocking IO
    
'''