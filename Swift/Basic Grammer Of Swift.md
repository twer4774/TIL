# 과거의 틀

Vi, Vim => GCC컴파일(컴파일 오류) => 실행(런타임 오류)

런타임 오류 잡는 방법(디버깅) - 런타임 오류가 잡기 힘들지...

- 브레이크 포인트 이용
  브레이크 포인트를 하나씩 넘겨가면서 오류 잡기
- 메모리 덤프로 메모리의 데이터 분석
  메모리 덤프 - 메모리의 상태 로그를 통째로 가져오는 것

플레이 그라운드의 역할

1. 스위프트의 코드 문법 및 코드의 실행과정 확인을 위한 프로토타입 역할
2. 스위프트 코드를 위한 각종 문서 및 가이드 작성 역할 - 리치 도큐먼트 형식의 문서작성
   플레이 그라운드로 마크다운 문법을 적용할 수 있다. 내 생각에는 typora같은 에디터로 작성하는게 더 쉽고 깔끔하지 않을까 한다. 플레이 그라운드로 굳이 만들 필요가 있을지??

 

# 스위프트 기본문법

- 헤더파일 작성하지 않음

- 대소문자 구분

- - 함수와 메소드, 인스턴스명의 첫 글자는 소문자
  - 클래스, 구조체, 프로토콜 등 객체의 첫 글자는 대문자

- 세미콜론 생략가능

- 엔트리포인트(시작점)으로 사용되는 main 함수가 없음

- - @UIApplicationMain어노테이션을 사용하여 앱을 시작하는 객체 지정 => 앱 당 하나만 지정 가능
  - 보통 AppDelegate파일에 있음

- 문자열 뿐만 아니라 문자(Character)      또한 큰따옴표 사용

- import키워드 사용 => 라이브러리, 프레임워크 참조용

 

# 변수와 상수

### 이름 정하기

1. 알파벳, 한글 자음, 모음, 아라비아 숫자, 특수기호, 한자, 바이너리 코드 등 이용가능
   But 영어, 숫자, 밑줄만 이용할 것!
2. 첫번째 글자는 숫자 이용 불가!



# 자료형

기본자료형

- | Int           | -128 ~ 127        |
  | ------------- | ----------------- |
  | UInt          | 양의 정수 0 ~ 255 |
  | Double, Float |                   |
  | Bool          |                   |
  | String        |                   |
  | Character     | 한개의 문자       |