# Java.lang - hashCode()

- 해싱 기법에 사용되는 해시함수를 구현한 것
- 다량의 데이터를 저장하고 검색하는데 유용
- 해싱 기법을 사용하는 HashMap이나 HashSet 같은 클래스에 저장할 객체라면 반드시 hashCode메서드를 오버라이딩해야 함

```java
class HashCodeEx{
  public static void main(String[] args){
    String str1 = new String("abc");
    String str2 = new String("abc");
    
    System.out.println(str1.hashCode()); //916354
    System.out.println(str2.hashCode()); //916354
		System.out.println(System.identityHashCode(str1)); //214058
    System.out.println(System.identityHashCode(str2)); //123522
  }
}
```

- 동일한 문자열에 대해서는 같은 해시값을 반환하도록 hashCode()에서 정의 되어 있으며, System.identityHashCode()메서드에서는 객체의 주소값으로 해시코드를 생성하기 때문에 모든 객체에 대해 항상 다른 해시 코드값을 반환함