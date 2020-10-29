# Inheritance(상속)

- 기존의 클래스를 재사용하여 새로운 클래스를 작성. extends 키워드 이용
- 적은 양의 코드로 새로운 클래스를 작성할 수 있음
  - 부모 클래스에서 정의된 멤버변수는 자식 클래스에서 사용 가능
  - 코드의 중복이 줄어들어 유지 보수에 좋음

### 클래스 간의 관계 - 포함관계

- 클래스를 재사용하는 방법으로 상속 이외의 방법

```java
class Circle{
  int x;
  int y;
  int r;
}

class Point{
  int x;
  int y;
}

//Point 클래스를 포함관계로 사용하여 클래스 재사용하기
class Circle {
  Point c = new Point();
  int r;
}
```

- 상속 관계를 맺을지 포함관계를 맺을지 결정하는 방법
  - '~은 ~이다(is-a, 상속)' 와 '~은 ~을 가지고 있다(has-a, 포함)'를 이용하여 결정
    - Circle is a Point => 원은 점이다
    - Circle has a Point => 원은 점을 가지고 있다
    - => 두번째 has a 가 더 알맞은 문장이므로 포함관계를 맺어줌

### 단일상속(Single Inheritance)

- 자바에서는 단일 상속만을 허용
  - 클래스간의 관계복잡도를 방지하기 위함
- 단일 상속을 하는 대신 포함관계(IS - A)를 이용하여 클래스의 재사용 가능

### Object 클래스 - 모든 클래스의 조상

- 모든 클래스들은 자동으로 Object 클래스를 상속 받고 있음
- 따라서 Object 클래스에 정의된 멤버 변수들을 사용 할 수 있음
  - toString(), equals(Object o) 등 11가지

