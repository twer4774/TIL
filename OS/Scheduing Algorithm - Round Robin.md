# Scheduing Algorithm - Round Robin

- 시분할 시스템이 나온 이후에 쓰이는 알고리즘
- 목적
  - Waiting time을 줄이기 위함
  - 공평하게 들어온 순서대로(FCFS, FIFO) 처리한다면 CPU Burst가 커질수록 Wating time이 길어짐
- 현재 시스템에서는 Priroriy Scheduling과 Round Robin을 혼합하여 사용하고 있음
- 타임퀀텀(Time Quantum) : 한 라운드마다 각 프로세스에 할당되는 작업시간
- 콘텍스트 스위칭(Context Switching) : 타임퀀텀 시간이 지난 후 프로세스를 변경하는 것

### 단점

- 타임퀀텀시간을 어떻게 정하느냐에 따라 단점이 될 수 있다
- 타임퀀텀을 정하는 방법
  - CPU Burst의 80% 정도를 포함할 수 있도록 설정해야 함
- 콘테스트 스위칭의 횟수를 줄이는게 성능의 핵심 - 줄일려면 타임퀀텀을 잘 정해야 함

### 활용

p1 : arrival time 0 / busrt time 3 

p2 : arrival time 0 / busrt time 4

p3 : arrival time 0 / busrt time 3

time quantum: 1 이라면, wating time, turnaruound time, response time, completion time을 구해라

| 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| p1   | p2   | p3   | p1   | p2   | p3   | p1   | p2   | p3   | p2   |

- completion time => p1: 7 / p2: 10 / p3: 9 (ready queue이므로 인덱스는 0부터 시작, 초로변환하면 1씩 더해야함)

- turnaround time => completion time - arrvial time
  - p1 : 7-0 = 7 / p2 : 10-0=10 /p3 : 9-0 = 9 => 평균 turnaround time = (7+10+9)/3 = 8.67

- wating time => 다른 프로세스가 수행되어 기다려야 하는 시간. 총 걸리는 작업 수행에서 자신의 작업시간을 뺌
  - turnaround time - burst time
  - wating p1 : 7-3 = 4 / p2 : 10-4 = 6 / p3 : 9-3=6
  - 평균 wating time = (4+6+6)/3 = 5.33
- response time => 프로세스가 처음으로 응답하기까지의 시간
  - 처음으로 응답하는 시간 - 도착하는 시간 (여기서는 모두 0이므로 처음으로 응답하는 시간만 생각하면됨)
  - p1: 0/ p2: 1 / p3: 2

​	