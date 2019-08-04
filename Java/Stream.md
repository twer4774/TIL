# Stream

- 데이터 소스를 추상화 하고 데이터를 다루는데 자주 사용되는 메서드들을 정의 => 코드의 재사용성을 높임
- 배열이나 컬렉션뿐만 아니라 파일에 저장된 데이터도 모두 같은 방식으로 다룰 수 있음
- '읽기 전용' => 데이터 소스를 변경하지 않는다. 필요하다면, 정렬된 결과를 컬렉션이나 배열에 담아서 반환은 할 수 있음
- Iterator처럼 일회용이다. 여러번 사용하려면 여러번 스트림을 생성해야한다.
- 작업을 내부 반복으로 처리한다.

```java
String [] strArr = { "aaa", "ddd", "ccc"};
List<String> strList = Arrays.asList(strArr);
//Convert Stream
Stream<String> strStream1 = strList.stream();
Stream<String> strStream2 = Arrays.stream(strArr);
//Output sorted data in stream
strStream1.sorted().forEach(System.out::println);
strStream2.sorted().forEach(System.out::println);
```

### 병렬 스트림

- 스트림으로 데이터를 처리할때 병렬처리가 쉽다.
- paralles()이라는 메서드를 호출하여 병렬로 연산을 수행할 수 있다 <=> 기본은 병렬스트림이 아니며, 혹시 병렬처리상태를 막기위해서는 sequential()을 호출한다. ==> sequential()을 이용해 paralles() 상태를 취소한다.

### 스트림 만들기

- 컬렉션: Collection에 stream()이 정의 되어 있다.

```java
Stream<T> Collection.stream()
  
List<Integer> list = Arrays.asList(1,2,3,4,5);
Stream<Integer> intStream = list.stream(); //list를 소스로 하는 컬렉션 생성
intStream.forEach(System.out::println); //스트림의 모든 요소를 출력한다.
intStream.forEach(System.out::println); //에러. 스트림은 일회용이므로 닫혀있다.
```

- 배열: Stream과 Arrays에 static메서드로 정의되어 있다.

```java
Stream<T> Stream.of(T... values) //가변인자
Strema<T> Stream.of(T[])
Strema<T> Arrays.Stream(T[])
Strema<T> Arrays.Stream(T[] array, int startInclusive, int endExclusive)
  
//문자열 스트림 생성 예
Stream<String> strStream = Stream.of("a","b","c"); //가변인자
Stream<String> strStream = Stream.of(new String[] {"a","b","c"}); 
Stream<String> strStream = Arrays.Stream(new String[] {"a","b","c"}); 
Stream<String> strStream = Arrays.Stream(new String[]{"a","b","c"}, 0, 3);

//특정 범위의 정수 생성
IntStream.range(int begin, int end) //end가 범위에 포함되지 않음
IntStream.rangeClosed(int begin, int end) //end가 범위에 포함됨
  
IntStream intStream = IntStream.range(1, 5); //1,2,3,4
IntStream intStream = IntStream.rangeClosed(1, 5); //1,2,3,4,5

//임의의 수
IntStream intStream = new Random().ints(); //무한 스트림
intStream.limit(5).forEach(System.out::println); //5개의 요소만 출력
```

- 람다식 =- iterate(), generate()

```java
static <T> Stream<T> interate(T seed, UnaryOperator<T> f)
static <T> Stream<T> generate(Supplier<T> s)
```

- 파일: 파일을 다루는데 필요한 유용한 메서드들을 제공.

```java
Stream<Path> Files.list(Path dir)
```

- 빈 스트림: 요소가 하나도 없을 때 null보다 빈 스트림을 반환하는 것이 낫다.

```java
Stream emptyStream = Stream.empty(); //empty()는 빈 스트림을 생성해서 반환한다.
long count = emptyStream.count(); //count의 값은 0
```

- Collect, optional 등 이용 예제

```java
package Stream;

import java.util.Comparator;
import java.util.stream.Stream;

public class StreamEx1 {
    public static void main(String[] args) {
        Stream<Student2> Student2Stream = Stream.of(
                new Student2("이자바", 3, 300),
                new Student2("김자바", 1, 200),
                new Student2("안자바", 2, 100),
                new Student2("강자바", 2, 150),
                new Student2("소자바", 1, 200),
                new Student2("나자바", 3, 290),
                new Student2("감자바", 3, 180)
        );

        Student2Stream.sorted(Comparator.comparing(Student2::getBan) //반별 정렬
                .thenComparing(Comparator.naturalOrder())) //기본정렬r
                .forEach(System.out::println);
    }//main
}

class Student2 implements Comparable<Student2> {
    String name;
    int ban;
    int totalScore;

    Student2(String name, int ban, int totalScore) {
        this.name = name;
        this.ban = ban;
        this.totalScore = totalScore;
    }

    public String toString() {
        return String.format("[%s, %d, %d]", name, ban, totalScore);
    }//toString

    String getName() { return name; }
    int getBan() { return ban; }
    int getTotalScore() { return totalScore; }

    //총점 내림차순을 기본정렬로한다.
    public int compareTo(Student2 s){
        return s.totalScore - this.totalScore;
    }
} //class Student2

//결과
[이자바, 3, 300]
[김자바, 1, 200]
[안자바, 2, 100]
[강자바, 2, 150]
[소자바, 1, 200]
[나자바, 3, 290]
[감자바, 3, 180]
안자바-[안자바, 2, 100]
count=7
totalScore=1420
totalScore=1420
topStudent=[이자바, 3, 300]
IntSummaryStatistics{count=7, sum=1420, min=100, average=202.857143, max=300}
{이자바,김자바,안자바,강자바,소자바,나자바,감자바}
나자바-[나자바, 3, 290]
count=7
totalScore=1420
totalScore=1420
topStudent=[이자바, 3, 300]
IntSummaryStatistics{count=7, sum=1420, min=100, average=202.857143, max=300}
{이자바,김자바,안자바,강자바,소자바,나자바,감자바}
김자바-[김자바, 1, 200]
count=7
totalScore=1420
totalScore=1420
topStudent=[이자바, 3, 300]
IntSummaryStatistics{count=7, sum=1420, min=100, average=202.857143, max=300}
{이자바,김자바,안자바,강자바,소자바,나자바,감자바}
강자바-[강자바, 2, 150]
count=7
totalScore=1420
totalScore=1420
topStudent=[이자바, 3, 300]
IntSummaryStatistics{count=7, sum=1420, min=100, average=202.857143, max=300}
{이자바,김자바,안자바,강자바,소자바,나자바,감자바}
감자바-[감자바, 3, 180]
count=7
totalScore=1420
totalScore=1420
topStudent=[이자바, 3, 300]
IntSummaryStatistics{count=7, sum=1420, min=100, average=202.857143, max=300}
{이자바,김자바,안자바,강자바,소자바,나자바,감자바}
이자바-[이자바, 3, 300]
count=7
totalScore=1420
totalScore=1420
topStudent=[이자바, 3, 300]
IntSummaryStatistics{count=7, sum=1420, min=100, average=202.857143, max=300}
{이자바,김자바,안자바,강자바,소자바,나자바,감자바}
소자바-[소자바, 1, 200]
count=7
totalScore=1420
totalScore=1420
topStudent=[이자바, 3, 300]
IntSummaryStatistics{count=7, sum=1420, min=100, average=202.857143, max=300}
{이자바,김자바,안자바,강자바,소자바,나자바,감자바}
```

## 그룹 & 분할(GroupingBy & PartitioningBy)

- PartitioningBy

```java
package Stream;

import com.sun.org.apache.xpath.internal.operations.Bool;

import java.util.*;
import java.util.function.*;
import java.util.stream.*;
import static java.util.stream.Collectors.*;
import static java.util.Comparator.*;

public class StreamEx7PartitioningBy {
    public static void main(String[] args) {
        Student3[] stuArr = {
                new Student3("나자바", true, 1, 1, 300),
                new Student3("김지미", false, 1, 1, 250),
                new Student3("김자바", true, 1, 1, 200),
                new Student3("이지미", false, 1, 1, 150),
                new Student3("남자바", true, 1, 1, 100),
                new Student3("안지미", false, 1, 1, 50),
                new Student3("황지미", false, 1, 1, 100),
                new Student3("강지미", false, 1, 1, 150),
                new Student3("이자바", true, 1, 1, 200),

                new Student3("나자바", true, 2, 1, 300),
                new Student3("김지미", false, 2, 1, 250),
                new Student3("김자바", true, 2, 1, 200),
                new Student3("이지미", false, 2, 2, 150),
                new Student3("남자바", true, 2, 2, 100),
                new Student3("안지미", false, 2, 2, 50),
                new Student3("황지미", false, 2, 3, 100),
                new Student3("강지미", false, 2, 3, 150),
                new Student3("이자바", true, 2, 3, 200)
        };

        System.out.printf("1. 단순분할(성별로 분할) %n");
        Map<Boolean, List<Student3>> stuBySex = Stream.of(stuArr).collect(partitioningBy(Student3::isMale));
        List<Student3> maleStudent = stuBySex.get(true);
        List<Student3> femaleStudent = stuBySex.get(false);
        for(Student3 s : maleStudent) System.out.println(s);
        for(Student3 s : femaleStudent) System.out.println(s);

        System.out.printf("%n2. 단순분할 + 통계(성별 학생수) %n");
        Map<Boolean, Long> stuNumBySex = Stream.of(stuArr).collect(partitioningBy(Student3::isMale, counting()));
        System.out.println("남학생 수 : " + stuNumBySex.get(true));
        System.out.println("여학생 수 : " + stuNumBySex.get(false));

        System.out.printf("%n3. 단순분할 + 통계(성별 1등)%n");
        Map<Boolean, Optional<Student3>> topScoreBySex = Stream.of(stuArr).collect(partitioningBy(Student3::isMale, maxBy(comparingInt(Student3::getScore))));
        System.out.println("남학생 1등 :" + topScoreBySex.get(true));
        System.out.println("여학생 1등 :" + topScoreBySex.get(false));

        Map<Boolean, Student3> topScoreBySex2 = Stream.of(stuArr).collect(partitioningBy(Student3::isMale, collectingAndThen(maxBy(comparingInt(Student3::getScore)), Optional::get)));
        System.out.println("남학생 1등 :" + topScoreBySex2.get(true));
        System.out.println("여학생 1등 :" + topScoreBySex2.get(false));

        System.out.printf("%n4. 다중분할(성별 불합격자, 100점 이하)%n");
        Map<Boolean, Map<Boolean, List<Student3>>> failedStuBySex = Stream.of(stuArr).collect(partitioningBy(Student3::isMale, partitioningBy(s -> s.getScore() <= 100)));
        List<Student3> failedMaleStu = failedStuBySex.get(true).get(true);
        List<Student3> failedFemaleStu = failedStuBySex.get(false).get(false);

        for(Student3 s : failedMaleStu) System.out.println(s);
        for(Student3 s : failedFemaleStu) System.out.println(s);
    }//main
}

class Student3{
    String name;
    boolean isMale; //성별
    int hak; //학년
    int ban;
    int score;

    Student3(String name, boolean isMale, int hak, int ban, int score) {
        this.name = name;
        this.isMale = isMale;
        this.hak = hak;
        this.ban = ban;
        this.score = score;
    }//Student3

    String getname() { return name; }
    boolean isMale() { return isMale; }
    int gethak() { return hak; }
    int getBan() { return ban; }
    int getScore() { return score; }


    public String toString(){
        return String.format("[%s, %s, %d학년 %d반, %3d점]", name, isMale ? "남" : "여", hak, ban, score);
    }//toString

    //groupingBy()에서 사용
    enum Level { HIGH, MID, LOW } //성적을 상, 중, 하로 나눈다.
} //class Student3

//결과
1. 단순분할(성별로 분할) 
[나자바, 남, 1학년 1반, 300점]
[김자바, 남, 1학년 1반, 200점]
[남자바, 남, 1학년 1반, 100점]
[이자바, 남, 1학년 1반, 200점]
[나자바, 남, 2학년 1반, 300점]
[김자바, 남, 2학년 1반, 200점]
[남자바, 남, 2학년 2반, 100점]
[이자바, 남, 2학년 3반, 200점]
[김지미, 여, 1학년 1반, 250점]
[이지미, 여, 1학년 1반, 150점]
[안지미, 여, 1학년 1반,  50점]
[황지미, 여, 1학년 1반, 100점]
[강지미, 여, 1학년 1반, 150점]
[김지미, 여, 2학년 1반, 250점]
[이지미, 여, 2학년 2반, 150점]
[안지미, 여, 2학년 2반,  50점]
[황지미, 여, 2학년 3반, 100점]
[강지미, 여, 2학년 3반, 150점]

2. 단순분할 + 통계(성별 학생수) 
남학생 수 : 8
여학생 수 : 10

3. 단순분할 + 통계(성별 1등)
남학생 1등 :Optional[[나자바, 남, 1학년 1반, 300점]]
여학생 1등 :Optional[[김지미, 여, 1학년 1반, 250점]]
남학생 1등 :[나자바, 남, 1학년 1반, 300점]
여학생 1등 :[김지미, 여, 1학년 1반, 250점]

4. 다중분할(성별 불합격자, 100점 이하)
[남자바, 남, 1학년 1반, 100점]
[남자바, 남, 2학년 2반, 100점]
[김지미, 여, 1학년 1반, 250점]
[이지미, 여, 1학년 1반, 150점]
[강지미, 여, 1학년 1반, 150점]
[김지미, 여, 2학년 1반, 250점]
[이지미, 여, 2학년 2반, 150점]
[강지미, 여, 2학년 3반, 150점]
```

- GroupingBy

```java
package Stream;

import java.util.*;
import java.util.function.*;
import java.util.stream.*;
import static java.util.stream.Collectors.*;
import static java.util.Comparator.*;

public class StreamEx8GroupingBy {
    public static void main(String[] args) {
        Student4[] stuArr = {
                new Student4("나자바", true, 1, 1, 300),
                new Student4("김지미", false, 1, 1, 250),
                new Student4("김자바", true, 1, 1, 200),
                new Student4("이지미", false, 1, 1, 150),
                new Student4("남자바", true, 1, 1, 100),
                new Student4("안지미", false, 1, 1, 50),
                new Student4("황지미", false, 1, 1, 100),
                new Student4("강지미", false, 1, 1, 150),
                new Student4("이자바", true, 1, 1, 200),

                new Student4("나자바", true, 2, 1, 300),
                new Student4("김지미", false, 2, 1, 250),
                new Student4("김자바", true, 2, 1, 200),
                new Student4("이지미", false, 2, 2, 150),
                new Student4("남자바", true, 2, 2, 100),
                new Student4("안지미", false, 2, 2, 50),
                new Student4("황지미", false, 2, 3, 100),
                new Student4("강지미", false, 2, 3, 150),
                new Student4("이자바", true, 2, 3, 200)
        };

        System.out.printf("1. 단순그룹화(반별로 그룹화)%n");
        Map<Integer, List<Student4>> stuByBan = Stream.of(stuArr).collect(groupingBy(Student4::getBan));
        for (List<Student4> ban : stuByBan.values()) {
            for(Student4 s : ban){
                System.out.println(s);
            }//for
        }//for

        System.out.printf("%n2. 단순그룹화(성적별로 그룹화)%n");
        Map<Student4.Level, List<Student4>> stuByLevel = Stream.of(stuArr).collect(groupingBy(s-> {
            if(s.getScore() >= 200) return Student4.Level.HIGH;
            else if(s.getScore() >= 100) return Student4.Level.MID;
            else return Student4.Level.LOW;
        }));
        TreeSet<Student4.Level> keySet = new TreeSet<>(stuByLevel.keySet());

        for (Student4.Level key : keySet) {
            System.out.println("[" + key + "]");
            for (Student4 s : stuByLevel.get(key)) {
                System.out.println(s);
            }//for
            System.out.println();
        }//for

        System.out.printf("%n3. 단순그룹화 + 통계(성적별 학생수)%n");
        Map<Student4.Level, Long> stuCntByLevel = Stream.of(stuArr).collect(groupingBy(s-> {
            if(s.getScore() >= 200) return Student4.Level.HIGH;
            else if(s.getScore() >= 100) return Student4.Level.MID;
            else return Student4.Level.LOW;
        }, counting()));

        for (Student4.Level key : stuCntByLevel.keySet()) {
            System.out.printf("[%s] - %d명, ", key, stuCntByLevel.get(key));
        }//for
        System.out.println();

        System.out.printf("%n4. 다중그룹화(학년별, 반별)");
        Map<Integer, Map<Integer, List<Student4>>> stuByHakAndBan = Stream.of(stuArr).collect(groupingBy(Student4::getHak, groupingBy(Student4::getBan)));
        for (Map<Integer, List<Student4>> hak : stuByHakAndBan.values()) {
            for(List<Student4> ban : hak.values()){
                System.out.println();
                for (Student4 s : ban) {
                    System.out.println(s);
                }//for
            } //for
        }//for

        System.out.printf("%n5. 다중그룹화 + 통계(학년별, 반별 1등)%n");
        Map<Integer, Map<Integer, Student4>> topStuByHakAndBan = Stream.of(stuArr).collect(groupingBy(Student4::getHak, groupingBy(Student4::getBan, collectingAndThen(maxBy(comparingInt(Student4::getScore)), Optional::get))));
        for (Map<Integer, Student4> ban : topStuByHakAndBan.values()) {
            for (Student4 s : ban.values()) {
                System.out.println(s);
            }//for
        }//for

        System.out.printf("%n6. 다중그룹화 + 통계(학년별, 반별 성적그룹)%n");
        Map<String, Set<Student4.Level>> stuByScoreGroup = Stream.of(stuArr).collect(groupingBy(s -> s.getHak() + "-" + s.getBan(),
                mapping(s -> {
                    if(s.getScore() >= 200) return Student4.Level.HIGH;
                    else if(s.getScore() >= 100) return Student4.Level.MID;
                    else return Student4.Level.LOW;
                }, toSet()
                )));

        Set<String> keySet2 = stuByScoreGroup.keySet();

        for(String key : keySet2){
            System.out.println("["+key+"]" + stuByScoreGroup.get(key));
        }
    }//main
}

class Student4 {
    String name;
    boolean isMale; //성별
    int hak; //학년
    int ban;
    int score;

    Student4(String name, boolean isMale, int hak, int ban, int score) {
        this.name = name;
        this.isMale = isMale;
        this.hak = hak;
        this.ban = ban;
        this.score = score;
    }//Student3

    String getName() { return name; }
    boolean isMale() { return isMale; }
    int getHak() { return hak; }
    int getBan() { return ban; }
    int getScore() { return score; }


    public String toString(){
        return String.format("[%s, %s, %d학년 %d반, %3d점]", name, isMale ? "남" : "여", hak, ban, score);
    }//toString

    enum Level { HIGH, MID, LOW } //성적을 상, 중, 하로 나눈다.
}

//결과
1. 단순그룹화(반별로 그룹화)
[나자바, 남, 1학년 1반, 300점]
[김지미, 여, 1학년 1반, 250점]
[김자바, 남, 1학년 1반, 200점]
[이지미, 여, 1학년 1반, 150점]
[남자바, 남, 1학년 1반, 100점]
[안지미, 여, 1학년 1반,  50점]
[황지미, 여, 1학년 1반, 100점]
[강지미, 여, 1학년 1반, 150점]
[이자바, 남, 1학년 1반, 200점]
[나자바, 남, 2학년 1반, 300점]
[김지미, 여, 2학년 1반, 250점]
[김자바, 남, 2학년 1반, 200점]
[이지미, 여, 2학년 2반, 150점]
[남자바, 남, 2학년 2반, 100점]
[안지미, 여, 2학년 2반,  50점]
[황지미, 여, 2학년 3반, 100점]
[강지미, 여, 2학년 3반, 150점]
[이자바, 남, 2학년 3반, 200점]

2. 단순그룹화(성적별로 그룹화)
[HIGH]
[나자바, 남, 1학년 1반, 300점]
[김지미, 여, 1학년 1반, 250점]
[김자바, 남, 1학년 1반, 200점]
[이자바, 남, 1학년 1반, 200점]
[나자바, 남, 2학년 1반, 300점]
[김지미, 여, 2학년 1반, 250점]
[김자바, 남, 2학년 1반, 200점]
[이자바, 남, 2학년 3반, 200점]

[MID]
[이지미, 여, 1학년 1반, 150점]
[남자바, 남, 1학년 1반, 100점]
[황지미, 여, 1학년 1반, 100점]
[강지미, 여, 1학년 1반, 150점]
[이지미, 여, 2학년 2반, 150점]
[남자바, 남, 2학년 2반, 100점]
[황지미, 여, 2학년 3반, 100점]
[강지미, 여, 2학년 3반, 150점]

[LOW]
[안지미, 여, 1학년 1반,  50점]
[안지미, 여, 2학년 2반,  50점]


3. 단순그룹화 + 통계(성적별 학생수)
[HIGH] - 8명, [MID] - 8명, [LOW] - 2명, 

4. 다중그룹화(학년별, 반별)
[나자바, 남, 1학년 1반, 300점]
[김지미, 여, 1학년 1반, 250점]
[김자바, 남, 1학년 1반, 200점]
[이지미, 여, 1학년 1반, 150점]
[남자바, 남, 1학년 1반, 100점]
[안지미, 여, 1학년 1반,  50점]
[황지미, 여, 1학년 1반, 100점]
[강지미, 여, 1학년 1반, 150점]
[이자바, 남, 1학년 1반, 200점]

[나자바, 남, 2학년 1반, 300점]
[김지미, 여, 2학년 1반, 250점]
[김자바, 남, 2학년 1반, 200점]

[이지미, 여, 2학년 2반, 150점]
[남자바, 남, 2학년 2반, 100점]
[안지미, 여, 2학년 2반,  50점]

[황지미, 여, 2학년 3반, 100점]
[강지미, 여, 2학년 3반, 150점]
[이자바, 남, 2학년 3반, 200점]

5. 다중그룹화 + 통계(학년별, 반별 1등)
[나자바, 남, 1학년 1반, 300점]
[나자바, 남, 2학년 1반, 300점]
[이지미, 여, 2학년 2반, 150점]
[이자바, 남, 2학년 3반, 200점]

6. 다중그룹화 + 통계(학년별, 반별 성적그룹)
[1-1][HIGH, MID, LOW]
[2-1][HIGH]
[2-2][MID, LOW]
[2-3][HIGH, MID]
```

