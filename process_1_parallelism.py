'''
    Section 2
    Parallelism with Multiprocessing - Process vs Thread, Parallelism
    Keyword = Process, Thread, 병렬성
    
'''
'''

    (1) Parrallelism 병렬성
        - 완전히 동일한 타이밍(시점)에 태스크 슬행
        - 다양한 파트로 나눠서 실행
        - 멀티 프로세싱에서 CPU가 1CORE인 경우 불가함
        - 딥러닝, 비트코인 채굴 등에 사용
        
    (2) Process vs Thread(차이 비교)
        - 독립된 메모리 vs 공유 메모리
        - 많은 메모리 필요 vs 적은 메모리 필요
        - 좀비(데드) 프로세스 생성 가능성 vs 좀비(데드) 스레드 생성 가능성 적음
        - 오버헤드 큼 vs 오버헤드 작음
        - 생성 및 소멸 속도 느림 vs 생성 및 소멸 속도 빠름 (코스트 관점에서)
        - 코드 작성 쉬움/ 디버깅 어려움 vs 작성 어렵고 디버깅도 난해함
    
'''
