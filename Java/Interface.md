# Interface

- 일종의 추상클래스
- 추상클래스처럼 추상메서드를 갖지만 추상클래스보다 추상화가 높아서 일반 메서드와 멤버변수를 구성원으로 가질 수 없음
  - 추상클래스 : 미완성 설계도
  - 인터페이스 : 기본 설계도

```java
interface 인터페이스이름{
  public static final 타입 상수이름 = 값;
  public abstract 메서드이름 (매개변수목록);
}
```

- 인터페이스 멤버들의 제약사항
  - 모든 멤버변수는 public static final이어야 하며 이를 생략할 수 있음
  - 모든 메서드는 public abstract이어야 하며 이를 생략할 수 있음
  - => interface로 정의된다면 public static fianl, public abstract 가 생략된 것으로 생각해야 함
- JDK1.8부터 인터페이스에 static 메서드와 default메서드의 추가가 허용됨

### 인터페이스의 상속

- 인터페이스의 상속은 인터페이스 다중 상속 가능

```java
interface Movable {
  //지정된 위치로 이동하는 기능 메서드
  void move(int x, int y);
}

interface Attackable{
  //저정된 대상을 공격하는 기능 메서드
  void attack(Unit u);
}

interface Fightable extends Movable, Attackable { }
```

### 인터페이스 구현

- 인터페이스만으로는 인스턴스를 생성할 수 없으며, 클래스의 implements를 통해 인터페이스를 구현한 후 인터페이스를 구현한 클래스의 인스턴스를 사용해야 함

```java
//구현하는 인터페이스의 메서드 중 일부만 구현한다면, abstract를 붙여 추상클래스로 선언해야 함
abstract class Fighter implements Fightable {
  public void move(int x, int y) { ... }
}

//상속과 구현을 동시에 가능
class Fighter extends Unit implements Fightable {
  public void move(int x, int y) { ... }
  public void attack(Unit u) { ... }
}
```

### 인터페이스의 장점

- 개발시간 간축
- 표준화 가능
- 서로 관계없는 클래스들에게 관계를 맺어줌
- 독립적인 프로그래밍 가능

