# 생성자(Constructor)

- 인스턴스가 생성될 때 호출되는 '인스턴스 초기화 메서드'
- 인스턴스 변수의 초기화 작업에 주로 사용
  - 인스턴스 생성시 실행 되어야 할 작업을 위해 사용
- 생성자의 조건
  - 생성자의 이름은 클래스의 이름과 같아야 함
  - 생성자는 리턴 값이 없음 - 메서드와의 차이점
  - 생성자도 오버로딩이 가능 함

```java
class Card {
  Card(){ //매개변수가 없는 생성자
    ...
  }
  
  Card(String k, int num){ //매개변수가 있는 생성자
    ...
  }
}
```

- Card c = new Card(); 의 수행과정
  1. 연산자 new에 의해 메모리(heap)에 Card클래스의 인스턴스 생성
  2. 생성자 Card()가 호출되어 수행
  3. 연산자 new의 결과로 생성된 Card인스턴스의 주소가 반환되어 참조변수 c에 저장

### 기본 생성자(default constructor)

- 생성자가 하나도 정의되지 않을 경우 컴파일러는 자동적으로 매개변수가 없는 생성자를 추가하여 컴파일 함

### 매개변수가 있는 생성자

- 인스턴스를 생성하여 변수의 값을 변경하는 것 보다 매개변수가 있는 생성자를 이용해 값 변경이 코드를 간결하고 직관적이게 만듦

```java
class Car{
 	String color;
  String gearType; //auto / manual
  int door; //문의 개수
  
  Car() {}
  Car(String c, String g, int d){
    color = c;
    gearType = g;
    door = d;
  }
}

//인스턴스를 생성하여 변수의 값 변경
Car c = new Car();
c.color = "white";
c.gearType = "auto";
c.door = 4;

//매개변수가 있는 생성자를 이용하여 값 변경
Car c = new Car("white", "auto", 4);
```

### 생성자에서 다른 생성자 호출하기 - this(), this

- 생성자의 이름으로 클래스 이름 대신 this를 사용
- 한 생성자에서 다른 생성자를 호출할 때는 반드시 첫 줄에서만 호출 가능

```java
class Car{
	String color;
  String gearType; //auto / manual
  int door; //문의 개수
  
	Car() {
		this("white", "auto", 4);
	}
  Car(String color, String gearType, int door){
    this.color = color;
    this.gearType = gearType;
    this.door = door;
  }
}
```

