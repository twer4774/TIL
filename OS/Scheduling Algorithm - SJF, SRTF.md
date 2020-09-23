# Scheduling Algorithm - SJF

- SJF(Shortest Job First)
- 최단 작업 우선 스케줄링
- FCFS(First Come First Served , FIFO)
  - Wating time이 길어 SJF알고리즘이 나오게 됨
- 특징
  - 가장 CPU Burst가 적은 것을 먼저 수행
  - 평균 Wating Time이 가장 적은 알고리즘
  - Non-preemptive
    - 우선순위가 정해진 방법
    - 중간에 끼어들지 못함
  - Preemptive
    - 중간에 끼어들기 가능
      - 수행중인 작업(Job)을 도중에 다른 작업으로 대체(Sortest Remaining Time First, SRTF)

- 한계
  - SJF, SRTF 모두 컴퓨터 방식에 적용하기는 힘듦
    - I/O 요청의 명령으로 CPU가 CPU Burst를 인지할 수 있기 때문에 다음 CPU요청의 길이를 알 수 없음
  - Priority Scheduling(우선순위 스케줄링)알고리즘으로 한계 대체

