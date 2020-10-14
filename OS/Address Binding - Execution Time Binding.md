# Address Binding - Execution Time Binding

- 실행할 때 메모리 바인딩
- MMU(Memory Management Unit) : 실행할 때 마다 주소를 새로 계산하는데 이용하는 하드웨어

- Load Time Binding과의 차이점 - 바인딩 시점
  - Load Time Binding : 메모리에 로딩할 때 작업을 미리 다 해놓음
  - Execution Time Binding : 코드가 실행될 때마다 변환 작업을 그때 그때 해 줌
- 하드웨어의 성능이 좋아져 MMU를 이용하면 Load Time Binding보다 오버헤드가 작음
- 현재 시스템 환경에서 사용되는 방식