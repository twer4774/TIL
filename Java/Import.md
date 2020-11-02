# import

- 컴파일러에게 소스파일에 사용된 클래스의 패키지에 대한 정보를 제공
- import packageName.*; 과 같은 형태로 선언
  - *을 사용해도 개별적으로 불러오는 것과 성능차이는 없음
- import java.lang.*;은 묵시적으로 선언되어 있기 때문에 System, String과 같은 클래스들을 import 하지 않아도 사용할 수 있음

### static import

- static 멤버를 호출할 때 클래스 이름을 생략할 수 있음
- 특정 클래스의 static 멤버를 자주 사용할 때 편리