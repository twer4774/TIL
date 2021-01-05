# Stream(Review)

- 데이터 소스를 추상화하고 데이터를 다루는데 자주 사용되는 메서드들을 정의해 놓음

  - 데이터 소스 추상화 : 데이터 소스가 무엇이던 간에 같은 방식으로 다룰 수 있게 됨 => 재사용성 증가

    - List 정렬 - Collections.sort()

    - Array 정렬 - Arrays.sort() 

      => 이 두 가지를 같은 방식으로 정렬 할 수 있게 됨

      ```java
      String[] strArr = { "aaa", "ddd", "ccc"};
      List<String> strList = Arrays.asList(strArr);
      
      Stream<String> strStream1 = strList.stream(); //스트림 생성
      Stream<String> strStream2 = Arrays.stream(strArr); //스트림 생성
      
      strStream1.sorted().forEach(System.out::println);
      strStream2.sorted().forEach(System.out::println);
      ```

- 스트림의 특성

  - 스트림은 데이터 소스를 변경하지 않음 => 읽기전용
  - 일회용 - 사용할 때마다 다시 생성해야 함
  - 작업을 내부 반복으로 처리
    - forEach로 매개변수로 받고 내부적으로 for문 실행

## 스트림의 연산

- 스트림이 제공하는 연산은 중간 연산과 최종 연산으로 분류

  - 중간 연산 : 연산 결과가 스트림인 연산. 스트림에 연속해서 중간 연산을 할 수 있음
  - 최종 연산 : 연산 결과가 스트림이 아닌 연산. 스트림의 요소를 소모하므로 단 한번만 가능

  => stream.distinct().limit(5).sorted().forEach(System.out::println) ==> forEach()만 최종 연산

- 중간 연산

| 중간 연산                                                    | 설명                     |
| ------------------------------------------------------------ | ------------------------ |
| Stream<T> distinct()                                         | 중복 제거                |
| Stream<T> filter(Predicate<T> predicate)                     | 조건에 안 맞는 요소 제외 |
| Stream<T> limit(long maxSize)                                | 스트림의 일부를 잘라냄   |
| Stream<T> skip(long n)                                       | 스트림의 일부를 건너 띔  |
| Stream<T> peek(Consumer<T> action)                           | 스트림의 요소에 작업수행 |
| Stream<T> sorted()<br />Stream<T> sorted(Comparator<T> comparator) | 스트림의 요소를 정렬     |
| Stream<R> map(Function<T,R> mapper)<br />DoubleStream mapToDouble(ToDoubleFunction<T> mapper)<br />IntStream mapToInt(ToIntFunction<T> mapper)<br />LongStream mapToLong(ToLongFunction<T> mapper)<br /><br />Stream<R> flatMap(Function<T, Stream<R>> mapper)<br />DoubleStream flatMapToDouble(Function<T, DoubleStream> mapper)<br />IntStream mapToInt(Function<T, IntStream> mapper)<br />LongStream mapToLong(Function<T, LongStream> mapper) | 스트림의 요소를 변환     |

- 최종 연산

| 최종 연산                                                    | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| void forEach(Consumer<? super T> action)<br />void forEachOrdered(Consumer<? super T> action) | 각 요소에 지정된 작업 수행                                   |
| long count()                                                 | 스트림의 요소의 개수 반환                                    |
| Optional<T> max(Comparator<? super T> comparator)<br />Optional<T> min(Comparaotr<? usper T> comparator) | 스트림의 초대값/최소값을 반환                                |
| Optional<T> findAny() //아무거나 하나<br />Optional<T> findFirst() //첫번째 요소 | 스트림의 요소 하나를 반환                                    |
| boolean allMatch(Predicate<T> p) //모두 만족하는지<br />boolean anyMatch(Predicate<T> p) //하나라도 만족하는지<br />booelan noneMatch(Predicate<> p) //모두 만족하지 않는지 | 주어진 조건을 모든 요소가 만족시키는지, 만족시키지 않는지 확인 |
| Object[] toArray()<br />A[] toArray(IntFunction<A[]> generator) | 스트림의 모든 요소를 배열로 반환                             |
| Optional<T> reduce(BinaryOperator<T> accumulator)<br />T reduce(T identity, BinaryOperator<T> accumulator)<br />U reduce(U identity, BiFunction<U,T,U> accumulator, BinaryOperator<U> combiner) | 스트림의 요소를 하나씩 줄여가면서(리듀싱) 계산               |
| R collect(Collector<T,A.R> collector)<br />R collect(Supplier<R> supplier, BiConsumer<R,T> accumulator, BiConsumer<R, R> combiner) | 스트림의 요소를 수집. 주로 요소를 그룹화하거나 분할한 결과를 컬렉션에 담아 반환하는데 사용 |

## 스트림 만들기

### 컬렉션

- 컬렉션의 최고 조상인 Collection에 stream()이 정의되어 있음

```java
Stream<T> Collection.stream();

List<Integer> list = Arrays.asList(1,2,3,4,5); //가변인자
Stream<Integer> intStrea = list.stream(); //list를 소스로 하는 컬렉션 생성

intStream.forEach(System.out::pirntln); //스트림의 모든 요소를 출력
intStream.forEach(System.out::pirntln); //스트림은 일회성이므로 에러 발생
```

### 배열

- Stream과 Arrays에 static 메서드로 정의되어 있음

```java
Stream<T> Stream.of(T... values) //가변인자
Strema<T> Stream.of(T[])
Stream<T> Arrays.stream(T[])
Stream<T> Arrays.stream(T[] array, int startInclusive, int endExclusive)
```

### 특정 범위의 정수

- IntStream과 LongStream은 연속된 정수를 스트림으로 생성해서 반환하는 range()와 rangeClosed()를 가짐

```java
IntStream IntStream.range(int begin, int end)
IntStream IntStream.rangeClosed(int begin, int end)
  
IntStream intStream = IntStream.range(1, 5); //1,2,3,4
IntStream intStream = IntStream.rangeClosed(1, 5); //1,2,3,4,5
```

### 임의의 수

```java
IntStream intSteam = new Random().ints() //무한 스트림
IntStream.limit(5).forEach(System.out::println); //5개의 요소만 출력

//유한 스트림
IntStream ints(long streamSize)
IntStream intStream = new Random().ints(5); //크기가 5인 난수 스트림 반환
```

### 람다식 - iterate(), generate()

- Stream클래스의 iterate()와 generate()는 람다식을 매개변수로 받아 무한 스트림을 생성
- 주의사항
  - iterate()와 generate()는 기본형 스트림으로 반환할 수 없음
    - IntStream evenStream = Stream.iterate(0, n->n+2); //에러
    - 필요하다면, mapToInt()와 같은 메서드로 반환해야 함

```java
static <T> Stream<T> iterate(T seed, UnaryOperator<T> f)
static <T> Stream<T> generate(Supplier<T> s)
  
Stream<Integer> evenStream = Stream.iterate(0, n->n+2); //0, 2, 4, 6...

//generate()는 이전 결과를 이용해 다음요소를 계산하지 않음 (2+2=4, 4+2=6 이 아니라 계속 2+2=4가됨)
```

### 파일

- java.noio.file.Files는 파일을 다루는데 필요한 유용한 메서드들을 제공하는데, list()는 지정된 디렉토리에 있는 파일의 목록을 소스로 하는 스트림을 생성해서 반환

```java
Stream<Path> Files.list(Path dir)

Stream<String> Files.lines(Path path)
Stream<String> Files.lines(Path path, Charset cs)
Stream<STring> lines() //BufferedReader클래스의 메서드
```

### 스트림의 연결

- concat()을 사용하면 두 스트림을 하나로 연결할 수 있음
  - 두 스트림의 요소는 같은 타입이어야 함

```java
String[] str1 = {"123", "456", "789"};
String[] str2 = {"ABC", "abc", "DEF"};
Stream<String> strs1 = Stream.of(str1);
Stream<String> strs2 = Stream.of(str2);
Stream<String> strs3 = Stream.concat(strs1, strs2); //두 스트림을 하나로 연결
```

