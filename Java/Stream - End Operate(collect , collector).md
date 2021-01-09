# Stream - End Operate(collect , collector)

## collect()

- 스트림의 최종 연산중 가장 복잡하면서도 유용한 메서드

```java
collect() //스트림의 최종 연산. 매개변수로 컬렉터를 필요로 함
Collector //인터페이스, 컬렉터는 이 인터페이스를 구현해야 함
Collectors //클래스, static메서드로 미리 작성된 컬렉터를 제공
```

### 스트림을 컬렉션과 배열로 변환 - toList(), toSet(), toMap(), toCollection(), toArray()

```java
List<String> names = studStream.map(Student::getName).collect(Collectors.toList());
ArrayList<String> list = names.stream().collect(Collectors.toCollection(ArrayList::new));

//Person타입인 스트림에서 사람의 주민번호(regId)를 키로하고 값으로 Person객체 그대로 저장
Map<String, Person> map = personStream.collect(Collectors.toMap(p->p.getRegId(), p->p));
//toArray()로 배열반환, 단 생성자 참조를 매개변수로 지정해줘야 함
Student[] stuNames = studentStream.toArray(Student[]::new);
```

### 통계 - counting(), summingInt(), averagingInt(), maxBy(), minBy()

### 리듀싱 - reducing()

```java
IntStream intStream = new Random().ints(1,46).distinct().limit(6);

OptionalInt max = intStream.reduce(Integer::max);
Optional<Integer> max = intStream.boxed().collect(reducing(Integer::max));

long sum = intStream.reduce(0, (a,b) -> a+b);
long sum = intStream.boxed().collect(reducing(0, (a,b) -> a+b));

int grandTotal = stuStream.map(Student::getTotalScore).reduce(0, Integer::sum);
int grandTotal = stuStream.collect(reducing(0, Student::getTotalScore, Integer::sum));
```

### 문자열 결합 - joining()

```java
String studentNames = stuStream.map(Student::getName).collect(joining());
String studentNames = stuStream.mmap(Student::getName).collect(joining(","));
String studentNames = stuStream.mmap(Student::getName).collect(joining(",","[","]"));
```

### 그룹화와 분할 - groupingBy(), partitioningBy()

- collect()의 유용함을 알 수 있게 해주는 그룹화와 분할
- 그룹화 : 스트림의 요소를 특정 기준으로 그룹화
- 분할 : 스트림의 요소를 두 가지, 지정된 조건에 일치하는 그룹과 일치하지 않는 그룹으로 분할

```java
Collector groupingBy(Function classifier)
Collector groupingBy(Function classifier, Collector downstream)
Collector groupingBy(Function classifier, Supplier mapFactory, Collector downstream)
Collector partitioningBy(Predicate predicate)
Collector partitioningBy(Predicate predicate, Collector downstream)
```

```java
class Student{
  String name;
  boolean isMale;
  int hak;
  int ban;
  int score;
  
  Student(String name, boolean isMale, int hak, int ban, int score){
    this.name = name;
    this.isMale = isMale;
    this.hak = hak;
    this.ban = ban;
    this.score = score;
  }
  
  String getName() { return name; }
  boolean isMale() { return isMale; }
  int getHak() { return hak; }
  int getBan() { return ban; }
  int getScore() { return score; }
  
  public String toString(){
    return String.format("[%s, %s, %d학년 %d반, %3d점]", name, isMale ? "남":"여", hak, ban, score);
  }
  
  enum Level { HIGH, MID, LOW } //성적을 상, 중, 하 세단계로 분류
}

Stream<Student> stuStream = Stream.of(
	new Student("나자바", true, 1, 1, 300),
  ...
);

/* partitioningBy()에 의한 분류 */

//1. 기본 분할
//성별로 분할
Map<Boolean, List<Student>> stuBySex = stuStream.collect(partitioningBy(Student::isMale)); 
//Map에서 남학생 목록을 얻음
List<Student> maleStudent = stuBySex.get(true);

//2. 기본 분할 + 통계 정보
Map<Boolean, Long> stuNumBySex = stuStream.collect(partitioningBy(Student::isMale, counting()));
System.out.println("남학생수 : " + stuNumBySex.get(true));

// 총점구하기
Map<Boolean, Optional<Student>> topScoreBySex = stuStream.collect(partitioningBy(Student::isMale, collectingAndThen(maxBy(comparingInt(Student::getScore)), Optional::get)));
System.out.println("남학생 1등 : " + topScoreBySex.get(true));
```

### groupingBy()에 의한 분류

```java
Map<Integer, List<Student>> stuByBan = stuStream.collect(groupingBy(Student::getBan, toList())); 

//stuStream의 성적의 등급(Student.Level)로 그룹화 (HIGHT, MID, LOW)
Map<Student.Level, Long> stuByLevel = stuStream.collect(groupingBy(s->{ if(s.getScore() >= 200) else if(s.getScore() >= 100) else }, counting()));

//다중 그룹화 - 학년별 -> 반별
Map<Integer, Map<Integer, List<Student>>> stuByHakAndBan = stuStream.collect(groupingBy(Student::getHak, groupingBy(Student::getBan)));

//각 반의 1등 출력
Map<Integer, Map<Integer, Student>> topStuByHakAndBan = stuStream.collect(groupingBy(Student::getHak, groupingBy(Student::getBan, collectingAndThen(maxBy(comparingInt(Student::getScore)), Optional::get))));
```

## Collector 구현하기

- 직접 컬렉터를 작성 => Collector인터페이스를 구현한다는 의미

```java
//Collector인터페이스
public interface Collector<T, A, R>{
  Supplier<A> supplier();
  BiConsumer<A, T> accumulator();
  ...
}

supplier() 작업 결과를 저장할 공간 제공
accumulator() 스트림의 요소를 수집할 방법 제공
combiner() 두 저장공간을 병합할 방법을 제공(병렬 스트림)
finisher() 결과를 최종적으로 변환할 방법을 제공
```

- Stream<String>의 모든 문자열을 하나로 결합해서 String으로 반환하는 ConcatCollector

```java
import java.util.*;
import java.util.function.*;
import java.util.stream.*;

/**
 * Stream<String>의 모든 문자열을 하나로 결합해서 String으로 반화
 */
public class CollectorEx {

    public static void main(String[] args) {
        String[] strArr = { "aaa", "bbb", "ccc" };
        Stream<String> strStream = Stream.of(strArr);

        String result = strStream.collect(new ConcatCollector());

        System.out.println(Arrays.toString(strArr));
        System.out.println("result=" + result);
    }
}

class ConcatCollector implements Collector<String, StringBuilder, String> {

    @Override
    public Supplier<StringBuilder> supplier() {
        return StringBuilder::new;
    }

    @Override
    public BiConsumer<StringBuilder, String> accumulator() {
        return StringBuilder::append;
    }

    @Override
    public BinaryOperator<StringBuilder> combiner() {
        return StringBuilder::append;
    }

    @Override
    public Function<StringBuilder, String> finisher() {
        return StringBuilder::toString;
    }

    @Override
    public Set<Characteristics> characteristics() {
        return Collections.emptySet();
    }
}

/*
[aaa, bbb, ccc]
result=aaabbbccc
*/
```

