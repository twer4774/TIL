# Inner Class(내부 클래스)

- 내부클래스는 AWT, Swing같은 GUI어플리케이션의 이벤트 처리 이외에는 잘 사용하지 않음
- 내부클래스를 이용하는 이유
  - 내부 클래스에서 외부 클래스의 멤버들을 쉽게 접근할 수 있음
    - 한 클래스를 다른 클래스의 내부 클래스로 선언하면 두 클래스의 멤버들 간에 서로 쉽게 접근 가능
  - 캡슐화 - 코드의 복잡성을 줄일 수 있음

```java
class A { //외부 클래스
  ...
    class B { //내부 클래스
      ...
    }
}

class Outer{
  class InstantceInner {}
  static class StaticInner {}
  
  void myMethod() {
    class LocalInner {}
  }
}
```

- 내부 클래스는 외부 클래스 이외에 다른 클래스에서는 잘 사용되지 않음
- 내부 클래스의 종류와 특징
  - Instatnce Class : 외부 클래스의 멤버변수 선언위치에 선언. 외부 클래스의 인스턴스 멤버들과 관련된 작업에 사용
  - Static Class : 외부 클래스의 멤버변수 선언위치에 선언. 외부 클래스의 static 멤버, static 메서드 관련 작업에 사용
  - Local Class : 외부 클래스의 메서드나 초기화 블럭 안에 선언. 선언된 영역 내부에서만 사용
  - Anonymous Class : 클래스의 선언과 객체의 생성을 동시에 하는 이름 없는 클래스(일회용)