# Annotation (어노테이션)

- 자바 개발자들은 소스코드와 문서를 하나로 통합

  - /** ~ */ 를 이용하여 소스코드에 대한 정보를 저장하고, 소스코드의 주석으로부터 HTML 문서를 생성하는 javadoc.exe를 만들어서 사용 

  ```java
  /** 
  * Comment
  * @link
  * @author
  */
  public interface Annotation{ ... }
  ```

  - @ 태그는 주석 안에 정보를 저장하고 javadoc.exe라는 프로그램이 이 정보를 읽어서 문서를 작성하는데 사용됨
  - 프로그램의 소스코드 안에 다른 프로그램을 위한 정보를 미리 약속된 형식으로 함시킨 것이 어노테이션
  - 주석처럼 프로그램에 영향을 미치지 않지만, 프로그램에게 유용한 정보를 제공해 줌

## 표준 어노테이션

- 메타 에노테이션으로 어노테이션을 정의하는데 사용되는 어노테이션
- *가 붙은 것은 메타 어노테이션

| 어노테이션           | 설명                                                    |
| -------------------- | ------------------------------------------------------- |
| @Override            | 컴파일러에게 오바라이딩하는 메서드라는 것을 알림        |
| @Deprecated          | 앞으로 사용하지 않을 것을 권장하는 대상에게 붙임        |
| @SuppressWarnings    | 컴파일러의 특정 경고메시지가 나타나지 않게 해줌         |
| @SafeVarargs         | 제너릭 타입의 가변인자에 사용                           |
| @FunctionalInterface | 함수형 인터페이스라는 것을 알림                         |
| @Native              | native메서드에서 참조되는  상수 앞에 붙임               |
| @Target*             | 어노테이션이 적용가능한 대상을 지정하는데 사용          |
| @Documented*         | 어노테이션 정보가 javadoc으로 작성된 문서에 포함되게 함 |
| @Inherited*          | 어노테이션이 자손 클래스에 상속되도록 함                |
| @Retention*          | 어노테이션이 유지되는 범위를 지정하는데 사용            |
| @Repeatable*         | 어노테이션을 반복해서 적용할 수 있게 함                 |

### @Override

- 조상의 메서드를 오버라이딩할 때 쓰임. 조상 클래스의 메서드가 일치하도록 도움

```java
class Parent{
  void parentMethod() {}
}

class Child extends Parent {
  @Override
  void parentmethod() {} // 조상메서드의 이름을 잘못 적음 => 컴파일 에러 발생
}
```

### @Deprecated

- 더 이상 사용되지 않는 필드나 메서드에 붙임
- 다른 것으로 대체되었으니 더 이상 사용하지 않는 것을 권장함

```java
int getDate()
  Deprecated.
  As of JDK version 1.1, replaced by Calendar.get(Calendar.DAY_OF_MONTH).
  
//getDate()대신 get()을 사용하라는 메시지
```

### @FunctionalInterface

- 함수형 인터페이스를 선언할 때 사용
- 함수형 인터페이스를 올바르게 선언했는지 확인하고, 잘못된 ㅕㅇ우 에러를 발생

```java
@FunctionalInterface
public interface Runnable {
  public abstract void run();
}
```

### @SuppressWarnings

- 컴파일러가 보여주는 경고메시지가 나타나지 않게 억제함. 경고를 묵인해야할 경우 사용
  - deprecation : @Deprecated가 붙은 대상을 사용해 발생하는 경고 억제
  - unchecked : 제너릭 타입으로 지정하지 않았을 때 발생하는 경고 억제
  - rawtypes : 제너릭 타입을 사용하지 않았을 때 발생하는 경고 억제
  - varargs : 가변인자의 타입이 제너릭 타입일 때 발생하는 경고 억제

```java
@SuppressWarinings({"unchecked", "deprecation"}) //제너릭과 관련된 경고 억제
ArrayList list = new ArrayList();
list.add(obj);
```

### @SafeVarargs

- 메서드에 선언된 가변인자의 타입이 non-reifiable타입일 경우, 해당 메서드를 선언하는 부분과 호출하는 부분에서 "unchecked" 경고 발생 => 해당 코드에 문제가 없다면 경고를 억제하기 위해 @SafeVarargs 사용
- 이 어노테이션은 static이나 final이 붙은 메서드나 생성자에게만 붙일 수 있음



## 메타 어노테이션

- 어노테이션을 위한 어노테이션. 어노테션에 붙는 어노테이션으로 어노테이션을 지정할 때 사용

### @Traget

- 어노테이션이 적용가능한 대상을 지정하는데 사용

```java
@Target({TYPE, FIELD, METHOD, PARAMETER, CONSTRUCTOR, LOCAL_VARIABLE})
@Retention(RetentionPolicy.SOURCE)
public @interface SuppressWarnings{
  String[] value();
}
/*
ANNOTATION_TYPE : 어노테이션
CONSTRUCTOR : 생성자
FIELD : 필드(멤버변수, enum상수)
LOCAL_VARIABLE : 지역변수
METHOD : 메서드
PACKAGE : 패키지
PARAMETER : 매개변수
TYPE : 타입(클래스, 인터페이스, enum)
TYPE_PARAMETER : 타입 매개변수
TYPE_USE : 타입이 사용되는 모든 곳
*/
```

### @Retention

- 어노테이션이 유지되는 기간을 지정하는데 사용
- RUNTIME으로 지정시 리플렉션을 통해 클래스파일에 저장된 어노테이션 정보를 일겅서 처리 가능

| 유지 정책 | 의미                                             |
| --------- | ------------------------------------------------ |
| SOURCE    | 소스 파일에만 존재. 클래스파일에는 존재하지 않음 |
| CLASS     | 클래스 파일에 존재. 실행시에 사용불가. 기본값    |
| RUNTIME   | 클래스 파일에 존재. 실행시에 사용가능            |

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.SOURCE)
public @interface Override {}
```

### @Documented

- 어노테이션에 대한 저보가 javadoc으로 작성한 문서에 포함되도록 함
- @Override와 @SuppressWarnings를 제외하고 모두 이 메타 어노테이션이 붙어있음

### @Inherited

- 에노테이션이 자손 클래스에 상속되도록 함
- 조상클래스에 붙이면 자손 클래스도 이 어노테이션이 붙은것과 같이 인식됨

```java
@Inherited
@interface SupperAnno {}

@SuperAnno
class Parent{}

class Child extends Parent{} //Child에 어노테이션이 붙은 것으로 인식
```

### @Repeatable

- 여러 종류의 어노테이션을 붙일 수 있게 만듦. 보통 하나의 대상에 한 종류의 어노테이션이 붙음

- ```java
  @Repeatable(ToDos.class) //ToDo어노테이션을 여러 번 반복해서 쓸 수 있게 함
  @interface ToDo{
    String value();
  }
  
  @ToDo("delete test codes.")
  @ToDo("override inherited methods")
  class MyClass{
    ...
  }
  ```

### @Native

- 네이티브 메서드에 의해 참조되는 상수필드에 붙이는 어노테이션
  - 네이티브 메서드 : JVM이 설치된 OS의 메서드. 메서드의 선언부만 정의하고 구현하지 않음

## 어노테이션 타입 정의

```java
@interface annotationName {
  타입 요소 이름();
}
```

### 어노테이션의 요소

- 어노테이션 내에 선언된 메서드

- 아래에 선언된 TestInfo 어노테이션은 5개의 요소를 가짐

```java
@interface TestInfo {
  int count();
  String testedBy();
  String testTools();
  TestType testType(); //enum TestType { FIRST, FINAL }
  DateTime testDate(); //자신이 아닌 다른 어노테이션(@DateTime)을 포함할 수 있음
}

@interface DateTime{
  String yymmdd();
  String hhmmss();
}
```

### java.lang.annotation.Annotation

- Annotation은 모든 어노테이션의 조상
- 상속은 허용되지 않으며 interface로 정의 되어 있음

```java
package java.lang.annotation;

public interface Annotation{
  boolean equals(Object obj);
  int hashCode();
  String toString();
  
  Calss<? extneds Annontation> annotationType(); //어노테이션의 타입 반환
}

Class<AnnotationTest> cls = AnnotationTest.class;
Annotation[] annoArr = AnnotationTest.class.getAnnotations();

for(Annotation a : annoArr){
  System.out.println("toString():" + a.toString());
  System.out.println("hashCode():" + a.hashCode());
  System.out.println("equals():" + a.equals(a));
  System.out.println("annotationType():" + a.annotationType());
}
```

### Marker Annotation

- 값을 지정할 필요가 업슨ㄴ 경우, 어노테이션의 요소를 하나도 정의하지 않을 수 있음
- Serializable이나 Cloneable인터페이스 처럼, 요소가 하나도 정의되지 않은 어노테이션

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.SOURCE)
public @interface Override {} //마커 어노테이션. 정의된 요소가 하나도 없음

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.SOURCE)
public @interface Test {} //마커 어노테이션
```



## 어노테이션 예제

- 어노테이션을 직접 정의하고, 요소의 값을 출력하는 방법

```java
package JavaStandard;

import java.lang.annotation.*;

/**
 * 직접 어노테이션을 정의하고 출력하는 얘제
 */

@Deprecated
@SuppressWarnings("1111") //유효하지 않은 어노테이션은 무시됨
@TestInfo(testedBy = "aaa", testDate = @DateTime(yymmdd = "160101", hhmmss = "235959"))
public class AnnotationEx {
    public static void main(String[] args) {
        //Annotation class의 객체를 얻음
         Class<AnnotationEx> cls = AnnotationEx.class;

        TestInfo anno = (TestInfo) cls.getAnnotation(TestInfo.class);
        System.out.println("anno.testedBy()="+anno.testedBy());
        System.out.println("anno.testDate().yymmdd()="+anno.testDate().yymmdd());
        System.out.println("anno.testDate().hhmmss()="+anno.testDate().hhmmss());

        for (String str : anno.testTools()) {
            System.out.println("testTools="+str);
        }

        //AnnotationEx에 적용된 모든 어노테이션을 가져옴
        Annotation[] annoArr = cls.getAnnotations();
        for(Annotation a : annoArr){
            System.out.println(a);
        }
    }
}

@Retention(RetentionPolicy.RUNTIME) //실행시에 사용가능하도록 지정
@interface TestInfo{
    int count() default 1;
    String testedBy();
    String[] testTools() default "JUnit";
    TestType testType() default TestType.FIRST;
    DateTime testDate();
}

@Retention(RetentionPolicy.RUNTIME)
@interface DateTime{
    String yymmdd();
    String hhmmss();
}

enum TestType { FIRST, FINAL }

/*
anno.testedBy()=aaa
anno.testDate().yymmdd()=160101
anno.testDate().hhmmss()=235959
testTools=JUnit
@java.lang.Deprecated()
@JavaStandard.TestInfo(count=1, testType=FIRST, testTools=[JUnit], testedBy=aaa, testDate=@JavaStandard.DateTime(yymmdd=160101, hhmmss=235959))
*/
```

