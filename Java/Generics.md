# Generics

- 제너릭은 인스턴스별로 다르게 동작하려고 만드는것
- 다양한 타입의 객체들을 다루는 메서드나 컬렉션 클래스에 컴파일 시에 타입체크를 해주는 기능
  - 컴파일 시 타입체크의 장점
    - 타입의 안정성을 높임
      - 의도하지 않은 타입의 객체가 저장되는 것을 막고, 저장된 객체를 꺼내올 때 원래의 타입과 다른 타입으로 잘못 형변환되어 발생할 수 있는 오류를 줄여 줌
    - 형변환의 번거로움을 줄임
  - 주의 사항
    - 제너릭은 컴파일 시점에서 객체의 타입을 알아야함(컴파일 하기 전에 객체타입 지정이 되어야 함)

```java
//일반 클래스
class Box{
  Object item;
  
  void setItem(Object item) { this.item = item; }
  Object getItem() { return item; }
}

//제너릭 사용 클래스
class Box<T> {
  T item;
  
  void setItem(T item) { this.item = item; }
  T getItem(){ return item; }
}

//객체 생성시에는 참조변수와 생성자에 타입 T대신 실제 사용할 타이을 지정
Box<String> b = new Box<String>
b.setItem( new Object() );
b.setItem("ABC");
String item = b.getItem();
```

### 제네릭 용어

- Box\<T> : 제너릭 클래스
- T : 타입 변수 또는 타입 매개변수
- Box : 원시 타입

###  제너릭 제한

- 제너릭은 객체 마다 다른 타입으로 지정하는 것이 적절함 -> 제너릭은 인스턴스별로 다르게 동작하려고 만드는것

```java
Box<Apple> appleBox = new Box<Apple>();
Box<Grape> grapeBox = new Box<Grape>();
```

## 제너릭 클래스의 사용

```java
import java.util.ArrayList;

class Fruit {
    public String toString() { return "Fruit"; }
}

class Apple extends Fruit {
    public String toString() { return "Apple"; }
}

class Grape extends Fruit {
    public String toString() { return "Grape"; }
}

class Toy {
    public String toString() { return "Toy"; }
}

class Box<T> {
    ArrayList<T> list = new ArrayList<T>();

    void add(T item){ list.add(item); }

    T get(int i){ return list.get(i); }

    int size() { return list.size(); }

    public String toString() { return list.toString(); }
}


public class GenericExFruitBox {
    public static void main(String[] args) {
        Box<Fruit> fruitBox = new Box<Fruit>();
        Box<Apple> appleBox = new Box<Apple>();

        // GrapeBox는 생성하지 않음
        //Box<Grape> grapeBox = new Box<Grape>();

        // Fruit의 자손이 아닌 Toy
        Box<Toy> toyBox = new Box<Toy>();


        //fruitBox에는 Apple을 담을 수 있음
        fruitBox.add(new Fruit());
        fruitBox.add(new Apple());


        appleBox.add(new Apple());
        appleBox.add(new Apple());
        //appleBox에는 Toy를 담을 수 없음
        //appleBox.add(new Toy());
        
        toyBox.add(new Toy());
        //toyBox에는 Apple을 담을 수 없음
        //toyBox.add(new Apple());

        System.out.println("fruitBox : " + fruitBox);
        System.out.println("appleBox : " + appleBox);
        System.out.println("toyBox: " + toyBox);
    }
}
/*
fruitBox : [Fruit, Apple]
appleBox : [Apple]
toyBox: []
*/
```

## 제한된 제너릭 클래스

```java
FruitBox<Toy> fruitBox = new FruitBox<Toy>();
fruitBox.add(new Toy());
```

- 위와 같이 fruitBox에 toy가 들어가는 것을 방지하기 위한 방법

  - extends이용 - 자손클래스만 담을 수 있음

  ```java
  class FruitBox<T extends Fruit>{...}
  ```

## 와일드 카드

- 제너릭클래스에서 static으로 정의된 메서드의 경우 자손 클래스의 객체를 만들 수 없음
  - static은 인스턴스의 생성 없이 메서드를 사용하며, 이때 이미 매개변수타입이 지정되어있어야 하므로 자손클래스의 사용이 어려움

```java
class Juicer{
  static Juice makeJuice(FruitBox<Fruit> box){
    ...
  }
}

FruitBox<Furit> furitBox = new FruitBox<Fruit>();
FruitBox<Furit> appleBox = new FruitBox<Apple>();

System.out.println(Juicer.makeJuice(fruitBox));
System.out.println(Juicer.makeJuice(appleBox)); //에러 발생 => static에서 FruitBox<Fruit>로 고정되었기 때문
```

- '?'를 이용한 와일드카드로 해결
  - <? extends T> 와일드 카드의 상한 제한. T와 그 자손들만 가능
  - <? Super T> 와일드 카드의 하한 제한. T와 그 조상들만 가능
  - <?> 제한 없음. 모든 타입 가능. <? extends Object>와 동일

```java
class Juicer{
  static Juice makeJuice(FruitBox<? extneds Fruit> box){
    ...
  }
}
```

### 와일드카드 예제

- AppleCom()와 GrapeComp()는 동일코드임 => 과일이 추가되면 갯수를 늘려야 함

- FruitComp() 처럼 조상클래스를 이용해 과일의 무게를 잴 수 있게 만듦

- => Collection.sort()로 정렬을 하는데, 내부적으로 <? super T>와 같이 하한제한(T와 그 조상들만 가능)을 두어 Apple, Grape 처럼 Fruit를 상속받은 클래스 객체도 정렬할 수 있게 됨

- ```
  static <T> void sort(List<T> list, Comparator<? super T> c)
  ```

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Fruit {
    String name;
    int weight;

    Fruit(String name, int weight) {
        this.name = name;
        this.weight = weight;
    }

    public String toString() { return name+"("+weight+")";}
}


class Apple extends Fruit {
    Apple(String name, int weight){
        super(name, weight);
    }
}

class Grape extends Fruit {
    Grape(String name, int weight){
        super(name, weight);
    }
}

class FruitCom implements Comparator<Fruit>{
    public int compare(Fruit f1, Fruit f2){
        return f1.weight - f2.weight;
    }
}

class AppleCom implements Comparator<Apple>{
    public int compare(Apple a1, Apple a2){
        return a2.weight - a1.weight;
    }
}

class GrapeCom implements Comparator<Grape>{
    public int compare(Grape g1, Grape g2){
        return g2.weight - g1.weight;
    }
}

class FruitBox<T extends Fruit> extends Box<T>{}
class Box<T> {
    ArrayList<T> list = new ArrayList<T>();

    void add(T item){ list.add(item); }

    T get(int i) { return list.get(i); }

    ArrayList<T> getList() { return list; }

    int size() { return list.size(); }

    public String toString(){ return list.toString(); }
}

class GenericExWildCard {
    public static void main(String[] args) {
        FruitBox<Apple> appleBox = new FruitBox<Apple>();
        FruitBox<Grape> grapeBox = new FruitBox<Grape>();

        appleBox.add(new Apple("GreenApple", 300));
        appleBox.add(new Apple("GreenApple", 100));
        appleBox.add(new Apple("GreenApple", 200));


        grapeBox.add(new Grape("GreenGrape", 200));
        grapeBox.add(new Grape("GreenGrape", 500));
        grapeBox.add(new Grape("GreenGrape", 100));

        Collections.sort(appleBox.getList(), new AppleCom());
        Collections.sort(grapeBox.getList(), new GrapeCom());
        System.out.println(appleBox);
        System.out.println(grapeBox);
        System.out.println();

        Collections.sort(appleBox.getList(), new FruitCom());
        Collections.sort(grapeBox.getList(), new FruitCom());
        System.out.println(appleBox);
        System.out.println(grapeBox);
    }
}

/*
[GreenApple(300), GreenApple(200), GreenApple(100)]
[GreenGrape(500), GreenGrape(200), GreenGrape(100)]

[GreenApple(100), GreenApple(200), GreenApple(300)]
[GreenGrape(100), GreenGrape(200), GreenGrape(500)]
*/
```

