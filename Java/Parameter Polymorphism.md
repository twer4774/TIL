# 매개변수의 다형성(Parameter Polymorphism)

```java
class Product {
  int price;
  int bonusPoint;
}
class Tv extends Product { Tv(){super(100);}} //100만원
class Computer extends Product { Computer() { super(200); }}
class Audio extends Product { Audio() { super(50) }}

class Buyer { //고객, 물건을 사는 사람
  int money = 1000; //소유금액
  int bonusPoint = 0; //보너스점수
  
  //Tv를 구매하는 경우
  void buy(Tv t){
    money = money - t.pirce;
    
    //Buyer의 보너스 점수에 제품의 보너스 점수를 더함
    bonusPoint = bonusPoint + t.bonusPoint;
  }
  //Computer를 구매하는 경우
  void buy(Computer c) {
    ...
  }
  //Audio를 구매하는 경우
  void buy(Audio a){
    ...
  }
  
  //위의 3가지 buy에 대해 매개변수의 다형성을 이용하면 아래와 같이 변경 가능
  void buy(Product p){
    money = money - p.price;
    bonusPoint = bonusPoint + p.bonusPoint;
  }
}

Buyer b = new Buyer();
Tv t = new Tv();
computer c = new Computer();
b.buy(t);
b.buy(c);
```

- Tv, Computer, Audio 클래스가 Product 클래스를 상속받기 때문에 buy의 메서드를 간단하게 표현 가능함