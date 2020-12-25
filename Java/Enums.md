# Enums

- 서로 관련된 상수를 편리하게 선언하기 위한 것 -> 여러 상수를 정의할 때 사용하면 유용
- 열거형이 갖는 값 뿐만 아니라 타입도 관리하기 때문에 논리적인 오류를 줄일 수 있음

```java
class Card {
  static final int CLOVER = 0;
  static final int HEART = 1;
  static final int DIAMOND = 2;
  static final int SPADE = 3;
  
  static final int TWO = 0;
  static final int THREE = 1;
  static final int FOUR = 2;
  
  final int kind;
  final int num;
}

// => 열거형으로 변환
class Card {
  enum Kind { CLOVER, HEART, DIAMOND, SPADE } //열거형 Kind 정의
  enum Value { TWO, THREE, FOUR } //열거형 Value 정의
  
  final Kind kind; //타입이 int가 아닌 Kind임을 유의
  final Value value;
}
```

- 타입까지 체크
  - if(Card.CLOVER == Card.TWO) //ture가 나옴
  - if(Card.Kind.CLOVER == Card.Value.TWO) //컴파일 에러. 타입까지 체크함

## 열거형의 정의와 사용

```java
enum 열거형 이름 { 상수명1, 상수명2, ... }

enum Direction { EAST, WEST, SOUTH, NOTH}

class Unit {
  int x, y; 
  Dircetion dir; //열거형을 인스턴스 변수로 선언
  
  void int(){
    dir = Direction.EAST; //유닛의 방향을 EAST로 초기화
  }
}
```

- Switch문에서 열거형 사용
  - 주의: case에 Direction.EAST가 아닌 EAST만 씀 => 자바에서 그렇게 만듦

```java
void move() {
  switch(dir){
    case EAST: x++;
      break;
    case WEST: x--;
      break;
  }
}
```

### 모든 열거형의 조상 - java.lang.Enum

- 열거형 Direction에 정의된 모든 상수를 출력하려면,

  - values()메서드 사용

  ```java
  Direction[] dArr = Direction.values();
  
  for(Direction d : dArr){
    System.out.printf("%s = %d%n", d.name(), d.ordinal());
  }
  ```

| 메서드                                    | 설명                                                 |
| ----------------------------------------- | ---------------------------------------------------- |
| Class<E> getDeclaringClass                | 열거형의 Class객체반환                               |
| String name()                             | 열거형 상수의 이름을 문자열로 반환                   |
| int ordinal()                             | 열거형 상수가 정의된 순서를 반환(0부터 시작)         |
| T valueOf(Class<T> enumType, String name) | 지정된 열거형에서 name과 일치하는 열거형 상수를 반환 |

## 열거형에 멤버 추가

- Enum클래스에 정의된 ordinal()은 내부적인 용도로만 사용할 것(이 값을 열거형 상수의 값으로 사용하지 말 것)
- 열거형 상수의 값이 불연속적인 경우
  - 열거형 상수의 이름 옆에 원하는 값을 괄호에 넣어 줌

```java
enum Direction { EAST(1), SOUTH(5), NOTH(10), WEST(-1) }
```

### 멤버 추가

```java
enum Direction {
	EAST(1), SOUTH(5), NOTH(10), WEST(-1); //끝에 ; 추가
  
  private final int value; //정수를 저장할 필드 (인스턴스변수) 추가
  Direction(int value) { this.value = value; } //생성자 추가
  
  public int getValue() { return value; }
}
```

```java
package JavaStandard;


enum Direction{
    EAST(1, ">"), SOUTH(2, "v"), WEST(3, "<"), NORTH(4,"^");

    private static final Direction[] DIR_ARR = Direction.values();
    private final int value;
    private final String symbol;

    Direction(int value, String symbol){ //접근 제어자 private가 생략됨
        this.value = value;
        this.symbol = symbol;
    }

    public int getValue() { return value; }
    public String getSymbol() { return symbol; }

    public static Direction of(int dir){
        if(dir < 1 || dir > 4){
            throw new IllegalArgumentException("Invalid value : " + dir);
        }

        return DIR_ARR[dir - 1];
    }

    //방향을 회전시키는 메서드. num의 값 만큼 90도씩 시계방향으로 회전
    public Direction rotate(int num) {
        num = num % 4;

        if(num < 0) num += 4; //num이 음수일 때 시계반대방향으로 회전

        return DIR_ARR[(value-1+num) % 4];
    }

    public String toString(){
        return name() + getSymbol();
    }
} // enum Direction

public class EnumDirection {
    public static void main(String[] args) {
        for(Direction d: Direction.values()){
            System.out.printf("%s=%d%n", d.name(), d.getValue());
        }

        Direction d1 = Direction.EAST;
        Direction d2 = Direction.of(1);

        System.out.printf("d1=%s, %d%n", d1.name(), d1.getValue());
        System.out.printf("d2=%s, %d%n", d2.name(), d2.getValue());

         //방향을 회전시키는 메서드. num의 값 만큼 90도씩 시계방향으로 회전
        System.out.println(Direction.EAST.rotate(1)); //EAST의 90도 회전 => SOUTH
        System.out.println(Direction.EAST.rotate(2)); //180 => WEST
        System.out.println(Direction.EAST.rotate(-1)); //-90 => NORTH
        System.out.println(Direction.EAST.rotate(-2)); //-180 => WEST
    }
}
/*
EAST=1
SOUTH=2
WEST=3
NORTH=4
d1=EAST, 1
d2=EAST, 1
SOUTHv
WEST<
NORTH^
WEST<
*/
```

### 열거형에 추상 메서드 추가 - 잘 사용하지 않으므로 참고만 하자

- 운송수단별로 거리에 따른 요금을 설정하는 예

```java
/**
 * 운송수단 별로 거리에 따라 요금이 다르므로, 추상메서드를 추가하여 해결
 */


enum Transportation{
    BUS(100) { int fare(int distance) { return distance*BASIC_FARE;}},
    TRAIN(150) { int fare(int distance) { return distance*BASIC_FARE;}},
    SHIP(100) { int fare(int distance) { return distance*BASIC_FARE;}},
    AIRPLANE(300) { int fare(int distance) { return distance*BASIC_FARE;}};

    protected final int BASIC_FARE; //protected로 선언해야 각 상수에서 접근 가능

    private Transportation(int basicFare){
        BASIC_FARE = basicFare;
    }

    public int getBasicFare() { return BASIC_FARE; }

    abstract  int fare(int distance); //거리에 따른 요금 계산 추상메서드
}

public class EnumTransportFare {
    public static void main(String[] args) {
        System.out.println("bus fare = " + Transportation.BUS.fare(100));
        System.out.println("train fare = " + Transportation.TRAIN.fare(100));
        System.out.println("ship fare = " + Transportation.SHIP.fare(100));
        System.out.println("airplane fare = " + Transportation.AIRPLANE.fare(100));
    }
}

/*
bus fare = 10000
train fare = 15000
ship fare = 10000
airplane fare = 30000
*/
```

