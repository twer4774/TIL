# 여러 종류의 객체를 배열로 다루기

```java
Product p1 = new Tv();
Product p2 = new Computer();
Product p3 = new Audio();

//Product 참조 변수 배열로 처리
Product p[] = new Product[3];
p[0] = new Tv();
p[1] = new Computer();
p[2] = new Audio();
```

- 위와 같이 공통의 조상(Product)를 가진 클래스의 경우 조상을 참조변수로 배열처리가 가능함
- 하지만, 갯수가 늘어난다면? => Vector로 처리

### Vector

- 이름 때문에 기능을 오해할 수 있지만, 단지 동적으로 크기가 관리되는 개체배열일 뿐
- import java.util.*; 로 import 필요
- 메서드
  - Vector() : 인스턴스 생성
  - boolean add(Object o) : 추가
  - boolean remove(Object o) : 삭제
  - boolean isEmpty() : 비었는지 검사
  - Object get(int index) : 지정된 위치의 객체 반환. 반환타입이 Object타입이므로 적절한 타입으로의 형변환 필요
  - int size() : 저장된 객체의 개수 반환

```java
import java.util.*;

class Product{
  int price;
  int bonusPoint;

  Product(){
  	price = 0;
    bonusPoint = 0;
  }
  
  Product(int price){
    this.price = price;
    bonusPoint = (int) (price/10.0);
  }
}

class Tv extends Product {
  Tv() { super(100); }
}

class Computer extends Product {
  Computer() { super(200); }
}

class Audio extends Product {
  Audio() { super(50); }
}

class Buyer{
  int money = 1000;
  int bonusPoint = 0;
 	Vector item = new Vector(); //제품 저장의 vector객체
  
  void buy(Product p){
    if(money < p.price){
      System.out.println("잔액이 부족");
      return;
    }
    
    money -= p.price;
    bonusPoint += p.bonusPoint;
    item.add(p);
    System.out.println(p + "을/를 구입하였습니다.")
  }
  
  void summary(){
    int sum =0;
    String itemList = ""; //구매 물품목록
    
    if(item.isEmpty()) {
      System.out.println("구입한 제품이 없음");
      return;
    }
  }
}
```

