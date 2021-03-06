# Address Binding - Load Time Binding

### Load Time Binding

실제로는 안쓰이는 방법 - > 치명적인 단점: 메모리 로딩 시 속도가 매우 오래 걸림

- 로딩할때 바인딩하는 방법
- 프로그램 내부에서 사용하는 주소와 Physical 주소는 다름
  - Compile Time Binding에서는 프로그램 내부의 주소와 physical 주소가 같음
- 상대주소를 이용하여 주소 바인딩 실행
  - 상대주소 : 현재 위치한 곳을 기준으로하여 다음 주소를 계산하는 방법(기준 주소에서 얼마나 떨어져있는지)
  - 컴파일 타임 바인딩에서는 absolute code, 로드 타임 바인딩에서는 relocatable code
- 장점
  - physical 메모리의 주소와 분리하여 로딩이 되므로 멀티프로그래밍이 가능
- 단점
  - 메모리 로딩 시 속도가 매우 오래 걸림
    - 장점에서 쓰이는 방법처럼 physical 메모리의 주소와 분리하였으므로 코드 세그먼트의 명령어들이 많음
      - 코드 세그먼트 중에서 메모리를 참조하는 명령어도 존재하므로 결과적으로 메모리 로딩 시간이 지연됨
  - 로딩할때 마다 모든 메모리 주소가 한번씩 바뀜
    - 논리적 주소와 물리적 주소를 잘 분리하여 멀티 프로그래밍이 가능하지만, 잦은 주소 변경이 생김
    - 해결방안으로 Execution Time Binding(런타임 바인딩)이 나옴