# Scheduling Technique - Multilevel Queue 

- Mutlilevel - 프로세스의 중요도에 따라 레벨을 나눔
- 중요도에 따라 나눈 프로세스를 레벨별로 나누고, 여러 개의 큐에 다양한 알고리즘을 적용하는 스케줄링 기법
- OS가 할당한 프로세스의 레벨이 가장 높으며, 사용자가 할당한 프로세스의 레벨이 가장 낮음
  - 레벨이 높은 순서대로 먼저실행
- RR 방식을 도입한 time-slice 방식도 존재함
  - Queue 사이에 time-slice를 적용하여 각 큐에 다른 time quantum 설정
  - 결국 priority + RR 방식이 됨