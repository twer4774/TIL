# 람다식(lambda)

- JDK1.8부터 추가됨. 람다식의 도입으로 인해 자바는 객체지향언어이자, 함수형언어가 되었음
- 람다식 = 메서드를 하나의 식으로 표현한 것 = 익명함수(anonymous function)

```java
int[] arr = new int[5];
Arrays.setAll(arr, (i) -> (int)(Math.random()*5)+1);
```

```java
(매개변수 선언) -> {
	문장들
}

(int a, int b) -> {
	return a > b ? a : b;
}
//=>
(int a, int b) -> a > b ? a : b // retur문 대신 '식'으로 인식하므로 ;을 붙이지 않는다.
//=>
(a, b) -> a > b ? a : b
```

- 인터페이스를 통해 람다식을 다루기로 결정 => '함수형 인터페이스'

```java
@FunctionalInterface
interface MyFunction {
  public abstract int max(int a, int b);
}
// 단, 함수형 인터페이스에서는 오직 하나의 추상 메서드만 정의되어야 하는 제약이 존재 => 람다식과 인터페으싀 메서드가 1:1로 연결되기 위함. static메서드와 default메서딍 갯수는 제약이 없음
```

