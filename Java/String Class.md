# String Class

## 변경 불가능한(immutable) 클래스

- String 클래스에는 문자열을 저장하기 위해서 문자형 배열 변수(char[]) value를 인스턴스 변수로 정의해 놓고 있음
- 인스턴스 생성 시 생성자의 매개변수로 입력받는 문자열은 char[]배열로 저장됨

```java
public final class String implements java.io.Serializable, Comparalbe{
  private char[] value;
  ...
}
```

- 한번 생성된 String인스턴스가 갖고 있는 문자열은 읽어 올 수만 있고, 변경할 수는 없음
- 문자열간의 결합이나 추출 등 문자열을 다루는 작업이 많이 필요한 경우 String클래스 대신 StringBuffer 클래스를 사용하는 것이 좋음
  - StringBuffer인스턴스에 저장된 문자열은 변경이 가능하므로 하나의 StringBuffer인스턴스만으로도 문자열을 다루는 것이 가능

## 문자열 비교

### 문자열 리터럴 지정

```java
String str1 = "abc"; //문자열 리터럴 "abc"의 주소가 str1에 저장
String str2 = "abc"; //문자열 리터럴 "abc"의 주소가 str2에 저장
```

- 클래스가 메모리에 로드 될 때 자동적으로 미리 생성

### String클래스의 생성자를 사용해 만드는 방법

```java
String str3 = new String("abc"); //새로운 String인스턴스를 생성
String str4 = new String("abc"); //새로운 String인스턴스를 생성
```

- new연산자에 의해 메모리할당이 이루어지기 때문에 항상 새로운 String인스턴스가 생성됨

### 비교

- 리터럴 지정인 경우 단순 복사이므로 == 과 equlas 모두 true
- 생성자를 이용한 경우 new로 새로운 메모리가 할당 되므로 ==일때는 false, equlas는 true
  - equals는 단순히 객체에 저장된 문자열을 비교하는 것
  - ==는 객체 인스턴스의 주소를 비교하는 것

```java
class StringEx{
  public static void main(String[] args){
    String str1 = "abc";
    String str2 = "abc";
    
    System.out.println("str1 == str2 ? " + (str1 == str2)); //true
    System.out.println("str1.equals(str2) ? " + str1.equals(str2)); //true;
    
    String str3 = new String("abc");
    String str4 = new String("abc");
    
    System.out.println("str3 == str4 ? " + (str3 == str4)); //false
    System.out.println("str3.equals(str4) ? " + str3.equals(str4)); //true;    
  }
}
```