# Generic Method

## 제너릭 메서드

- 메서드 선언부에 제너릭 타입이 선언된 메서드

  - Collections.sort()

  ```java
  static <T> void sort(List<T> list, Comparator<? super T> c)
  ```

- 제너릭 클래스에서 선언된 \<T>와 메서드의 \<T>는 별개의 것

```java
static Juice makeJuice(FruitBox<? extends Fruit> box){
  String tmp = "";
  for(Fruit f : box.getList()) tmp += f + " ";
  return new Juice(tmp);
}

// => Generic Method로 변환
static <T extends Fruit> Juice makeJuice(FruitBox<T> box){
  String tmp = "";
  for(Fruit f : box.getList()) tmp += f + " ";
  return new Juice(tmp);
}
```

- 매개변수의 타입이 복잡할때도 유용

```java
public static void printAll(ArrayList<? extneds Product> list, ArrayList<? extends Product> list2){ ... }

// => <? extends Product> 줄이기
public static <T extends Product> void printAll(ArrayList<T> list, ArrayList<T> list2){ ...}
```

## 제너릭 타입의 제거

- 컴파일러는 제너릭 타입을 이용해 소스파일을 체크하고, 필요한 곳에 형변환을 넣어준 후 제너릭 제거
  - .class파일에는 제너릭이 없어짐 => 제너릭이 도입되기 이전의 소스코드와의 호환성 유지 때문. 현재는 원시타입을 배제하고 코딩하도록 권장