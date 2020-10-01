# Synchroniztion - 동기화

- Mutil-Thread Program 또는 Multi-Process Program에서 공유 데이터에 대해 접근할 때, 그 순서를 조절하는 것을 Synchroniztion이라고 한다.

### Race Condition

- 두 개 이상의 동시발생가능한 스레드들이 공유된 자원을 접근할 경우, 동기화 메커니즘이 없는 상태
- 두 개의 스레드가 자원을 놓고 레이싱하는 상황
- 문제
  - 실행순서를 조절해주지 않으면 비정상적인 상태가 나옴