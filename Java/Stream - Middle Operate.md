# Stream - Middle Operate

## 스트림 자르기 - skip(), limit()

- 스트림의 일부를 잘라낼 때 사용

```java
Stream<T> skip(long n)
Stream<T> limit(long maxSize)
  
IntStream = IntStream.rangeClosed(1, 10); //1~10의 요소를 가진 스트림
intStream.skip(3).limit(5).forEach(System.out::println); //45678
```

## 스트림의 요소 걸러내기 - filter(), distinct()

- distinct() : 스트림에서 중복된 요소들을 제거
- filter() : 주어진 조건에 맞지 않는 요소를 걸러냄

```java
InStream intStream = IntStream.of(1,2,3,3,3,4,5,5,6);
intStream.distinct().forEach(System.out:print); //123456

InStream intStream = IntStream.rangeCloseD(1, 10); //1~10
intStream.filter(i -> i%2==0).forEach(System.out::print); //246810

//아래의 두 문장은 동일한 결과를 얻음
intStream.filter(i -> i%2!=0 && i%3!=0).forEach(System.out::print); //157
intStream.filter(i->i%2!=0).filter(i>i%3!=0).forEach(System.out::print);
```

## 정렬 - sorted()

```java
Stream<String> strStream = Stream.of("dd", "aaa", "CC", "cc", "b");
strStream.sorted().forEach(System.out::print); //CCaabcccdd
```

```java
import java.util.Comparator;
import java.util.stream.Stream;

/**
 * 학생의 성적을 반별 오름차순, 총점별 내림차순으로 정렬하여 출력
 */
public class StreamEx {
    public static void main(String[] args) {
        Stream<Student> studentStream = Stream.of(
                new Student("이자바", 3, 300),
                new Student("김자바", 1, 200),
                new Student("안자바", 2, 100),
                new Student("박자바", 2, 150),
                new Student("소자바", 1, 200),
                new Student("나자바", 3, 290),
                new Student("감자바", 3, 180)
        );

        studentStream.sorted(Comparator.comparing(Student::getBann) //반별 정렬
                .thenComparing(Comparator.naturalOrder())) //기본 정렬
                .forEach(System.out::println);
    }
}

class Student implements Comparable<Student>{
    String name;
    int ban;
    int totalScore;

    Student(String name, int ban, int totalScore) {
        this.name = name;
        this.ban = ban;
        this.totalScore = totalScore;
    }

    public String toString(){
        return String.format("[%s, %d, %d]", name, ban, totalScore);
    }

    String getName() {return name;}
    int getBann() {return ban;}
    int getTotalScore() {return totalScore;}

    //총점 내림차순을 기본정렬로 함
    @Override
    public int compareTo(Student s) {
        return s.totalScore - this.totalScore;
    }
}
/*
[김자바, 1, 200]
[소자바, 1, 200]
[박자바, 2, 150]
[안자바, 2, 100]
[이자바, 3, 300]
[나자바, 3, 290]
[감자바, 3, 180]
*/
```

## 변환 - map()

- 원하는 필드만 뽑아 내거나 특정 형태로 변환해야 할때 사용

```java
Stream<R> map(Function<? super T,? extends R> mapper)
  
Stream<File> fileStream = Stream.of(new File("Ex1.java"), new File("Ex1"), new File("Ex1.bak"), new File("Ex2.java"), new File("Ex1.txt"));

//map()으로 Stream<File>을 Stream<String>으로 변환
Stream<String> filenameStream = fileStream.map(File::getName);
filenameStream.forEach(System.out::println); //스트림의 모든 파일이름을 출력
```

## 조회 - peek()

- 연산과 연산 사이에 올바르게 처리되었는지 확인

```java
filterStream.map(File::getName)
  .filter(s -> s.indexOf('.')!=-1) //확장자가 없는 것은 제외
  .peek(s -> System.out.printf("filename=%s%n", s)) //파일명 출력
  .map(s -> s.subString(s.indexOf('.')+1)) //확장자만 추출
  .peek(s -> System.out.printf("extension=%s%n", s)) //확장자 출력
  .forEach(System.out::println);
```

## mapToInt(), mapToLong, mapToDouble()

- 기본형 스트림으로 변환하는 메서드들

## flatMap() - Stream<T[]>를 Stream\<T>로 변환

- 스트림의 요소가 배열이거나 map()의 연산결과가 배열인 경우 스트림 타입으로 변환
  - Stream<T[]> -> Stream\<T>

```java
Stream<String[]> strArrStrm = Stram.of(
	new String[] {"abc", "def", "ghi" },
	new String[] {"ABC", "GHI", "JKIMN"}
);
```

- map()과 flatMap()의 차지

```java
//map()
Stream<String> => map(s->Stream.of(split(" +"))) => Stream<Stream<String>>

//flatMap()
Stream<String> => flatMap(s->Stream.of(s.split(" +"))) => Stream<String>

strStream.map(String::toLowerCase) //모든 단어를 소문자로 변경
					.distinct() //중복된 단어제거
					.sorted() //사전순으로 정렬
					.forEach(System.out::println); //화면에 출력
```

```java
import java.util.Arrays;
import java.util.stream.Stream;

/**
 * Map()과 flatMap() 사용
 */
public class StreamExMapFlatMap {
    public static void main(String[] args) {
        Stream<String[]> strArrStrm = Stream.of(
                new String[] {"abc", "Def", "jkl"},
                new String[] {"ABC", "GHI", "JKL"}
        );

//        Stream<Stream<String>> strStrmStrm = strArrStrm.map(Arrays::stream);
        Stream<String> strStrm = strArrStrm.flatMap(Arrays::stream);

        strStrm.map(String::toLowerCase)
                .distinct()
                .sorted()
                .forEach(System.out::println);
        System.out.println();

        String[] lineArr = {
                "Believe or not It is true",
                "Do or do not There is no try",
        };

        Stream<String> lineStream = Arrays.stream(lineArr);
        lineStream.flatMap(line -> Stream.of(line.split(" +")))
                .map(String::toLowerCase)
                .distinct()
                .sorted()
                .forEach(System.out::println);
        System.out.println();

        Stream<String> strStrm1 = Stream.of("AAA", "ABC", "bBb", "Dd");
        Stream<String> strStrm2 = Stream.of("bbb", "aaa", "ccc", "dd");

        Stream<Stream<String>> strStrmStrm = Stream.of(strStrm1, strStrm2);
        Stream<String> strStream = strStrmStrm.map(s -> s.toArray(String[]::new))
                .flatMap(Arrays::stream);

        strStream.map(String::toLowerCase)
                .distinct()
                .forEach(System.out::println);
    }
}
/*
abc
def
ghi
jkl

believe
do
is
it
no
not
or
there
true
try

aaa
abc
bbb
dd
ccc
*/
```

