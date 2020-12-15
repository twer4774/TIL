# CollectionFramework - HashSet

- 중복된 요소를 제거하는 Set의 사용의 대표적인 컬렉션
- 리스트와 달리 순서를 유지하지 않음
  - 순서를 유지하고 싶다면 LinkedHashSet을 사용

| 생성자 또는 메서드                | 설명                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| HashSet()                         | HashSet 객체 생성                                            |
| HashSet(Collection c)             | 주어진 컬렉션을 포함하는 HashSet개겣 생성                    |
| HashSet(int initialCapacity)      | 주어진 값을 초기용량으로하는 HashSet객체 생성                |
| boolean add(Object o)             | 새로운 객체 저장                                             |
| boolean addAll(Collection c)      | 주어진 컬렉션에 저장된 모든 객체들을 추가(합집합)            |
| void clear()                      | 모든 객체 삭제                                               |
| Object clone                      | HashSet 복제(얕은 복사)                                      |
| booelan contains(Object o)        | 저자왼 객체가 포함되어 있는지 확인                           |
| boolean containsAll(Collection c) | 주어진 컬렉션에 저장된 모든 객체들을 포함하고 있는지 알려줌  |
| boolean isEmpty()                 | HashSet이 비었는지 확인                                      |
| Iterator iterator()               | Iterator반환                                                 |
| boolean remove(Object o)          |                                                              |
| boolean revmoeAll(Collection c)   | 주어진 컬렉션에 저장된 모든 객체와 동일한 것들을 HashSet에서 모두 삭제(차집합) |
| boolean retainAll(Collection c)   | 주어진 컬렉션에 저장된 객체와 동일한 것만 남기고 삭제(교집합) |
| int size()                        |                                                              |

```java
import java.util.*;

class HashSetEx{
  public static vodi main(String[] args){
    Object[] objArr = {"1", new integer(1),"2","2","3","3","4","4","4"};
    
   	Set set = new HahsSet();
    
    for(int i=0; i<objArr.length; i++){
      set.add(objArr[i]); //HashSet에 objArr의 요소들을 저장
    }
    
    //HashSet에 저장된 요소들을 출력
    System.out.println(set);
  }
}

// [1, 1, 2, 3, 4]
// String 1과, Integer 1은 다른 객체이므로 중복으로 간주하지 않음
```

### HashSetLotto

```java
import java.util.*;

class HashSetLotto{
  public static void main(String[] args){
    Set set = new HashSet();
    
    for(int i=0; set.size()<6; i++){
      int num = (int)(Math.random()*45) + 1;
      set.add(new Integer(num));
    }
    
    List list = new LinkedList(set); //LinkedList(Collection c)
    Collections.sort(list); //Collections.sort(List list)
    System.out.println(list);
  }
}

// [7, 11, 17, 18, 24, 28]
```

### 이름과 나이가 같으면 동일인으로 인식하는 코드

```java
package JavaStandard;

import java.util.HashSet;

/**
 * 이름과 나이가 같으면 동일인으로 인식하도록 하는 목적을 가진 코드
 */
public class HashSetPerson {

    public static void main(String[] args) {
        HashSet set = new HashSet();

        set.add("abc");
        set.add("abc");
        set.add(new Person("walter", 29));
        set.add(new Person("walter", 29));

        System.out.println(set);
    }
}

class Person{
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public boolean equals(Object obj) {
        if(obj instanceof Person){
            Person person = (Person) obj;
            return name.equals(person.name) && age==person.age;
        }

        return false;
    }

    public int hashCode(){
        //return (name + age).hashCode();
      return Objects.hash(name, age); //이게 최신버전의 hash 사용법
    }

    public String toString(){
        return name + ":" + age;
    }
}

/*
[abc, walter:29]
*/
```

- HashCode의 add는 새로운 요소 추가시 equals와 hashCode를 호출하기 때문에 목적에 맞게 오버라이딩 필요