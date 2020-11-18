# Join(), StringJoiner

- join()은 여러 문자열 사이에 구분자를 넣어서 결합
- split()과 반대 작업

```java
Stirng anmails = "dog, cat, bear";
String[] arr = animals.split(",");
String str = String.join("-", arr); //dog-cat-bear
```

### StringJoiner클래스

- java.util.StringJoiner

```java
StringJoiner sj = new StringJoiner(",", "[", "]");
String[] strArr = { "aaa", "bbb", "ccc" };

for(String s: strArr){
  sj.add(s.toUpperCase()); //[AAA,BBB,CCC]
}
```

