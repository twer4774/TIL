# Scheduling, Dispatcher

- 넓은 의미 스케줄링 : Scheduling + Dispatcher
  - Scheduling : Ready Queue(대기 큐)에서 선택한 프로세스를 실행하는 것
    - FCFS, SJF, RR 등의 스케줄링 알고리즘이 존재

### 스케줄링 평가기준

- CPU의 가용성 : CPU를 얼마나 사용하는가
- 처리량(Throughput)
  - 초당 몇 million의 명령을 수행했는가
- 시간
  - turn around time : 실행되는데 걸리는 시간(시작시간~종료시간)
  - waiting time : 대기 시간. ready queue에서 실행되기까지 기다리는 시간
  - response time : 응답하는데 걸리는 시간
    - 자료를 처리하고 있음에 대한 응답(압축시 압축하고 있다는 것을 사용자에게 노출)

### 디스패처

- 스케줄러와의 차이
  - 스케줄러 : 해야할 일들을 ready queue에 저장하는 것 까지만
  - 디스패처 : 실제로 cpu에 프로세스를 할당