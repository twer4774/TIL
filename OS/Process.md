# Process(프로세스)

- CPU에 의해 처리되는 사용자 프로그램. 즉, 실행중인 프로그램
- Job, task라고도 함

### 프로세스의 형태

1. PCB(프로세스제어블록)를 가진 프로그램
2. 실기억장치에 저장된 프로그램
3. 프로세서가 할당되는 실체로서, 디스패치가 가능한 단위
4. 프로시저가 활동중인 것
   - 프로시저 : 프로그램을 분할한 작은 단위의 프로그램. 부 프로그램
5. 비동기적 행위를 일으키는 주체
6. 지정된 결과를 얻기 위한 일련의 계통적 동작
7. 목적 또는 결과에 따라 발생되는 사건들의 과정
8. 운영체제가 관리하는 실행단위

### 프로세스 상태 전이

- 제출
  - 작업을 처리하기 위해 사용자가 시스템에 제출한 상태
- 접수
  - 제출된 작업이 스풀 공간인 디스크의 할당 위치에 저장된 상태
- 준비
  - 프로세스가 프로세서를 할당받기 위해 기다리고 있는 상태
  - 프로세스는 준비상태 큐(스케줄링 큐)에서 실행을 준비하고 있음
  - 접수상태에서 준비 상태로의 전이는 Job스케줄러에 의해 수행됨
- 실행
  - 준비상태 큐에 있는 프로세스가 프로세서를 할당받아 실행되는 상태
  - 프로세스 수행이 완료되기 전에 프로세스에게 주어지너 프로세서 할당 시간이 종료되면 프로세스는 준비상태로 전환됨
  - 실행중인 프로세스에 입출력 처리가 필요하면 실행중인 프로세스는 대기 상태로 전이되며, 실행상태로의 전이는 CPU 스케줄러에 의해 수행
- 대기
  - 프로세스에 입출력 처리가 필요하면 현재 실행중인 프로세스가 중단되고, 입출력 처리가 완료될때까지 대기
- 종료
  - 프로세스의 실행이 끝나고 프로세스 할당이 해제된 상태

### 프로세스 상태전이 관련용어

- 디스패치(Dispatch) 
  - 준비 상태에서 대기하고 있는 프로세스 중 하나의 프로세서가 할당받아 실행 상태로 전이되는 과정
- 웨이크업(Wake Up)
  - 입,출력 작업이 완료되어 프로세스가 대기 상태에서 준비 상태로 전이되는 과정
- 스풀링(Spooling)
  - 입,출력 장치의 공유 및 상대적으로 느린 입출력 장치의 처리속도를 보완하고 다중 프로그래밍 시스템의 성능을 향상 시키기 위해 입,출력할 데이터를 직접 입출력장치에 보내지 않고 디스크에 저장
- 교통량 제어기
  - 프로세스의 상태에 대한 조사와 통보 담당