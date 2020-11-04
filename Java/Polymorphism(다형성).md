# Polymorphism(다형성)

- 여러 가지 형태를 가질 수 있는 능력
- 자바에서는 한 타입의 참조변수로 여러 타입의 객체를 참조할 수 있도록 함으로써 다형성을 프로그램적으로 구현함
  - 조상 클래스 타입의 참조변수로 자손클래스의 인스턴스를 참조할 수 있도록 함

```java
class Tv{
  boolean power; //전원 상태(on/off)
  int channel;
  
  void power(){ power = !power; }
  void channelUp() { ++channel; }
  void channelDown() { --channel; }
}

class CaptionTv extends Tv{
  String text; //캡션을 보여주기 위한 문자열
  void caption() { /* 내용 생략 */}
}

Tv t = new Tv();
CaptionTv c = new CatpionTv();
```

- 인스턴스 변수의 생성을 인스턴스 타입과 참조타입과 일치하는 것이 보통이지만, 상속 관계에 있는 경우 조상 타입의 참조변수로 자손 인스턴스를 참조할 수 있음

  ```java
  Tv t = new CaptionTv(); //조상 타입의 참조변수(Tv)로 자손 인스턴스(CaptionTv) 참조
  ```

  - 위와 같이 선언한 경우 t는 CaptinTV에 정의된 text 변수와 caption 메서드를 사용할 수 없음
  - 반대로 자손 타입의 참조변수로 조상타입의 인스턴스를 참조할 수 없음

### 참조변수의 형변환

- 기본형 변수와 같이 참조변수도 형변환이 가능
  - 단, 서로 상속관계에 있는 클래스 사이에서만 가능하기 때문에 자손타입의 참조변수를 조상타입의 참조변수로, 조상타입의 참조변수를 자손타입의 참조변수로의 형변환만 가능
- 형변환
  - Up-Casting : 자손타입 -> 조상타입 (형변환 생략 가능)
  - Down-Casting : 조상타입 -> 자손타입 (형변환 생략 불가)

```java
class Car {
  String color;
  int door;
  void drive(){
    System.out.println("dirve, Brrr~");
  }
  void stop(){
    System.out.println("stop!");
  }
}

class FireEngine extends Car { //소방차
  void water() {
  	System.out.println("water");
  }
}

class Ambulance extends Car { //앰뷸런스
  void siren() {
    System.out.println("siren~~~");
  }
}

Car car = null;
FireEngine fe = new FireEngine();
FireEngine fe2 = null;

car = fe; //car (Car) fe;에서 형변환이 생략 (업 캐스팅)
fe2 = (FireEngine) car; //형변환 생략 불가 (다운 캐스팅)
```