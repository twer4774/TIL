# Static Linking VS Dynamic Linking 

### Static Linking

- 실행 파일을 만들때 라이브러리를 같이 포함시킴
- 장점
  - 컴파일 시간 단축
  - 직접 구현한 코드를 라이브러리화 시키므로 기술 유출 방지
- 단점
  - 라이브러리 코드가 저장되기 때문에 메모리가 많이 필요

### Dynamic Linking

- 실행할때까지 링킹하는 것을 미룸
- 스텁 - 라이브러리가 메모리에 존재하지 않을 때, 라이브러리가 메모리에 상주할 수 있도록 라이브러리 루틴을 적절히 적재하는 방법을 알려주는 작은 코드
- 스텁은 모든 라이브러리 루틴에 들어있으며, 처음에는 dynamic linking으로 연결하지만 그 후에는 바로 주소를 참조하여 실행 할 수 있게 됨 => 메모리 절감효과
- 메모리에 똑같은것이 많이 올라가는 경우 static linking을 사용하면 메모리 사용량이 늘어나므로 dynamic linking을 사용
- 현재 Linux, Unix, Window에서 기본값으로 설정 됨
- DLL(Dynamic-link Library) : 윈도에서 동적링키을 사용할 때 사용되는 라이브러리 파일. 시스템 디렉토리에 저장되어 있음
- Shared Library(.so) : 윈도우에서는 DLL, Linux와 Unix에서는 Shared Library라고 부름

- 장점
  - 메모리의 요구사항이 적음 - 라이브러리 정보를 하나씩만 메모리에 올려서 실행
- 단점
  - 라이브러리가 저장되어있는 곳으로 이동해야 하므로
    - 성능상에서 약간의 오버헤드 발생
    - 불필요할 수도 있는 코드가 삽입(주소로 이동해야하는 코드)
- 활용
  - 게임의 업데이트
    - 게임의 새로운 버전이 나오면 새로 구매하는것이 아니라 기존의 것을 업데이트하여 이용(라이브러리의 업데이트)