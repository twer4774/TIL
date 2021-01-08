# Stream - End Operate(forEach, match, reduce)

- 최종 연산은 스트림의 요소를 소모해서 결과를 만들어 냄
  - 연산이 끝난 스트림은 닫히므로 필요에 따라 다시 생성해야 함

## forEach()

- peek()과 달리 스트림의 요소를 소모하는 최종 연산
- 반환 타입이 void이므로 스트림의 요소를 출력하는 용도로 많이 사용

```java
void forEach(Consumer<? super T> action)
```

## 조건 검사 - allMatch(), anyMatch(), noneMatch(), findFirst(), findAny()

- 스트림의 요소에 대해 지정된 조건에 모든 요소가 일치하는지, 일부가 일치하는지 등의 조건 확인

```java
//총점이 100 이하인 학생 확인(낙제생)
boolean noFailed = stuStream.anyMatch(s->s.getTotalScore() <= 100)
//낙제생 중 첫 요소 반환  
Optional<Student> stu = stuStream.filter(s->s.getTotalScore() <= 100).findFirst()
//병렬 스트림인 경우 findFirst()대신에 findAny() 사용  
Optional<Student> stu = parallelStream.filter(s->s.getTotalScore() <= 100).findFirst()
```

## 통계 - count(), sum(), average(), max(), min()

- 기본형 스트림에는 스트림의 요소들에 대한 통계정보를 얻을 수 있는 메서드들이 있음
- 기본형 스트림이 아닌 경우에는 통계와 관련된 메서드들이 count, max, min 밖ㅇ 사용하지 못함
- 나머지는 reduce()와 collect()를 사용해 통계 정보를 얻음

## 리듀싱 - reduce()

- 스트림의 요소를 줄여나가면서 연산을 수행하고 최종 결과를 반환

```java
Optional<T> reduce(BinaryOperator<T> accumulator)
  
int count = intStream.reduce(0, (a,b)->a+1); //count()
int sum = intStream.reduce(0, (a,b)->a+b); //sum()
int max = intStream.reduce(Integer.MIN_VALUE, (a,b)-> a>b ? a:b); //max()
int min = intStream.reduce(Integer.MAX_VALUE, (a,b)-> a<b ? a:b); //min()
```

```java
import java.util.*;
import java.util.stream.*;

public class StreamExReducing {
    public static void main(String[] args) {
        String[] strArr = {
                "Inheritance", "Java", "Lambda", "stream",
                "OptionalDouble", "IntStream", "count", "sum"
        };
        Stream.of(strArr).forEach(System.out::println);

        boolean noEmptyStr = Stream.of(strArr).noneMatch(s->s.length() == 0);
        Optional<String> sWord = Stream.of(strArr).filter(s->s.charAt(0) == 's').findFirst();

        System.out.println("noEmptyStr=" + noEmptyStr);
        System.out.println("sWord="+ sWord.get());

        //Stream<String[]>을 IntStream으로 변환
        IntStream intStream1 = Stream.of(strArr).mapToInt(String::length);
        IntStream intStream2 = Stream.of(strArr).mapToInt(String::length);
        IntStream intStream3 = Stream.of(strArr).mapToInt(String::length);
        IntStream intStream4 = Stream.of(strArr).mapToInt(String::length);

        int count = intStream1.reduce(0, (a,b) -> a+1);
        int sum = intStream2.reduce(0, (a,b) -> a+b);

        OptionalInt max = intStream3.reduce(Integer::max);
        OptionalInt min = intStream4.reduce(Integer::min);

        System.out.println("count="+count);
        System.out.println("sum="+sum);
        System.out.println("max="+max.getAsInt());
        System.out.println("min="+min.getAsInt());
    }


}
/*
Inheritance
Java
Lambda
stream
OptionalDouble
IntStream
count
sum
noEmptyStr=true
sWord=stream
count=8
sum=58
max=14
min=3
*/
```

