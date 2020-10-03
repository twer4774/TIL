# Peterson's Solution - 피터슨 알고리즘

- 동기화 문제를 해결하기 위한 상호배제 알고리즘
- flag, turn 변수를 이용
  - flag : 공유자원을 쓰고자 할때 표시
  - turn : 차례를 의미. 누구의 차례인지 명시

### 임계영역 해결 조건

- 상호배제가 보존되어야 한다 (Mutual exclusion is preserved)
  - 동시에 접근하지 않으려면 서로 배타적으로 동작해야 함
- 진행 (The progress requirement is statisfied)
  - 임계영역에 어떤 스레드의 접근도 없을 때 항상 접근이 가능해야 함
- 무한정 대기가 없어야 함 (Bounded-waiting requirement is met)
  - 모든 프로세스가 임계영역에 들어가기 위한 공정한 기회를 가져야 함
  - starvation을 방지
  - aging 기법이용이 대표적인 방법