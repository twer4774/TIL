# StringBuffer, StringBuilder

## StringBuffer

- String 클래스는 인스턴스를 생성할 때 지정된 문자열을 변경할 수 없지만 StringBuffer클래스는 변경이 가능함
  - 문자열의 길이를 고려하여 버퍼의 길이를 충분히 잡아주는 것이 좋음
  - char[]형 배열을 참조하는 것은 String 클래스와 동일

### StringBuffer의 생성자

- 인스턴스를 생성할 때, 적절한 길이의 char형 배열이 생성되고, 이 배열은 문자열을 저장하고 편집하기 위한 buffer로 사용됨
- 여유 있는 크기로 지정할 것

```java
public StringBuffer(int length){
  value = new char[length];
  shared = false;
}

public StringBuffer(){
  this(16); //버퍼의 크기를 지정하지 않으면 16이 기본 크기가 됨
}
public StringBuffer(String str){
  this(str.length() + 16); //지정한 문자의 길이보다 16 더 크가 버퍼 생성
  append(str);
}
```

### StringBuffer의 변경

- String과 달리 StringBuffer는 내용을 변경할 수 있음

```java
StringBuffer sb = new StringBuffer("abc");
sb.append("123"); //sb내용 뒤에 123 추가
```

### StringBuffer의 비교

- String 클래스에서는 equals메서드를 오버라이딩하여 문자열을 비교하도록 되어 있지만 StringBuffer는 equals를 오버라이딩 하지 않으므로 ==와 같은 결과를 냄(String Class.md 참고)
- toString()은 오버라이딩되어 있어 담고 있는 문자열을 String으로 반환 가능
- equals를 사용하려면 toString()으로 String 객체로 반환 후 equals 사용

## StringBuilder

- StringBuffer는 멀티쓰레드에 thread safe하도록 동기화 되어있음
  - 동기화가 StringBuffer의 성능을 떨어뜨림
- StringBuilder는 StringBuffer에서 동기화만 뺀 것
  - 기능은 StringBuffer와 동일