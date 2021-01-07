# Stream - Optional\<T>와 OptionalInt

- 최종 연산의 결과 타입이 Optional

```java
public final class Optional<T>{
  private final T value; //T타입의 참조변수
  ...
}

String str = "abc";
Optional<Stirng> optVal = Optional.of(str);
Optional<String> optVal = Optional.of("abc");
Optional<String> optVal = Optional.of(new String("abc"));

//Optional객체에 저장된 값을 가져올 때는 get()사용
String str1 = optVal.get(); //null이면 예외 발생
String str2 = optVal.orElse(""); //null이면 ""반환
```

```java
T orEleseGet(Supplier<? extends T> other)
T orElseThrow(Supplier<? extends X> exceptionSupplier)
  
String str3 = optVal2.orElseGet(String::new); //() -> new String()와 동일
String str4 = optVal2.orElseThrow(NullPointerException::new); //널이면 예외 발생
```

### OptionalInt, OptionalLong, OptionalDouble

- IntStream과 같은 기본형 스트림에는 Optional도 기본형을 값으로 하는 OptionalInt, OptionalLong, OptionalDouble을 반환