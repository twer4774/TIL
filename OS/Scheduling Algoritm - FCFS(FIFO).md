# Scheduling Algorithm - FIFO(FCFS)

- First In First Out = FCFS(First Come First Served)
- 들어온 순서대로 CPU에 할당 하여 처리하므로 가장 공평한 알고리즘
- 일단 프로세스가 CPU를 차지하면 완료될 때까지 수행
- 단점
  - 처리시간(Burst TIme)이 긴 프로세스가 들어오면 평균 대기시간이 길어짐 => Convoy Effect
  - 중요하지 않은 작업을 기다리게 할 수 있음
- FCFS의 보완 - SJF 알고리즘