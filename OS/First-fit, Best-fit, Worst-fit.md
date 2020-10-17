# First-fit, Best-fit, Worst-fit

- Trace Data(추적데이터)
  - 하루동안 프로그램이 실행, 종료되는 것들을 모아둔 데이터
  - 시뮬레이션 프로그램으로 성능 측정 (first-fit, best-fit, worst-fit)

### First-fit

- 가장 최초로 발견되는 hole에 할당
- 남은 메모리를 순차적으로 앞에서부터 탐색

### Best-fit

- hole의 공간을 최대한 줄일 수 있는 곳에 할당
- 단편화가 가장 작게 생김

### Worst-fit

- 메모리의 가장 큰 공간에 할당
- 딱 맞는 공간이 있더라도 가장 큰 공간에 할당하는 방식

### 성능비교

- fisrt-fit, best-fit은 속도나 메모리 사용률에서 wort-fit 보다 좋음
- first-fit, best-fit은 성능적으로는 별로 차이가 없으며, 알고리즘에 따라 성능 차이가 생김
  - 일반적으로 first-fit의 알고리즘 성능이 우수하다고 함
- 단편화는 어떻게든 생기게 됨(50% 규칙) - paging으로 해결
  - 고정분할방법 - paging