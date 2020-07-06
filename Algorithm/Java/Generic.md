# Generic

- 처리해야할 대상의 자료형에 의존하지 않는 클래스(인터페이스) 구현 방식
- 클래스 이름 뒤에 <Type> 같은 형식의 파라미터를 붙여 선언

```
class 클래스 이름 <파라미터1, 2> { }
interface 인터페이스 이름 <파라미터, 2> { }
```

- 매개 변수로 정의한 자료형을 전달 받을 수 있음

- 파라미터 이름을 작성하는 방법

  - 1개의 대문자를 사용
  - 컬렉션의 자료형은 element의 앞글자인 E 사용
  - 맵의 키, 값은 K,V 사용
  - 일반적으로는 T

- 와일드 카드 지정 가능

- ```
  <? extends T> : 클래스 T의 서브 클래스를 전달받습니다.
  <? super T> : 클래스 T의 슈퍼 클래스를 전달받습니다.
  ```

- 

```java
//Genric Example

class GenericClassTester{
  //제너릭 클래스의 파라미터를 T라고 작성
  static class GenericClass<T>{
    private T xyz;
    GenericClass(T t) {//생성자
      this.xyz = t;
    }
    T getXyz(){
      return xyz;
    }
  }
  
  public static void main(String[] args){
    //다음과 같이 파라미터에 String을 넘길 수도 있고 Integer를 넘길 수도 있음
    GenericClass<String> s = new GenericClass<String>("ABC");
    GenericClass<Integer> n = new GenericClass<Integer>(15);
    
    System.out.prinln(s.getXyz());
    System.out.prinln(n.getXyz());
  }
}
```