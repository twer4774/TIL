# Collection Framework - Iterator, ListIterator, Enumeration

- 컬렉션에 저장된 요소를 접근하는 데 사용되는 인터페이스
  - Enumeration은 Iterator의 구 버전이며, ListIterator는 Iterator의 기능을 향상한 것

## Iterator

- 컬렉션에 저자오딘 각 요소에 접근하는 기능을 가진 Iterator인터페이스를 정의 하고, Collection 인터페이스에는 Iterator를 반환하는 iterator()를 정의

```java
public interface Iterator{
  boolean hasNext();
  Object next();
  void remove();
}

public interface Collection{
  ...
    public Iteraotr iterator();
  ...
}
```

- Iterator()는 Collection 인터페이스 정의된 메서드이므로, Collecotion 인터페이스의 자손인 List, Set에도 포함되어 있음

  => 컬렉션 클래스에 대해 iteraotr()를 호출하여 Iterator를 얻은 다음 반복문, while문을 사용해 컬렉션 클래스의 요소들을 읽어 올 수 있음

  | 메서드            | 설명                                                         |
  | ----------------- | ------------------------------------------------------------ |
  | boolean hasNext() | 다음요소가 있는지 확인, true/false                           |
  | Object next()     | 다음요소를 읽어옴. 읽어오기 전에 다음 요소가 있는지 확인하는 hasNext() 사용권장 |
  | void remove()     | next()로 읽어 온 요소 삭제                                   |

```java
List list = new ArrayList();
Iterator it = list.iterator();

while(it.hasNext()){
  System.out.println(it.next());
}
```

- Map에서 Iterator 사용

  - key, value 값으로 저장하기 때문에 직접 iterator()를 사용할 수 없고, keySet()이나 entrySet()같은 메서드를 통해 키와 값을 따로 Set형태로 얻은 후 iterator()를 호출해야 함

  ```java
  Map map = new HashMap();
  
  Iteraotr it = map.keySet().iterator();
  ```

### Iterator 예제

```java
import java.util.*;

class IteratorEx{
  public static void main(String[] args){
    ArrayList list = new ArrayList();
    list.add("1");
    list.add("2");
    list.add("3");
    list.add("4");
    list.add("5");
    
    Iterator it = list.iterator();
    
    while(it.hasNext()){
      Object obj = it.next();
      System.out.println(obj);
    }
  }
}

/*
1
2
3
4
5
*/
```



## ListIterator

- Iterator를 상속받아 기능을 추가한 것
  - Iterator에 양방향 조회기능을 추가(List를 구현한 경우만 사용 가능)

| 메서드                | 설명                                                |
| --------------------- | --------------------------------------------------- |
| void add(Object o)    |                                                     |
| boolean hasNext()     |                                                     |
| booelan hasPrevious() |                                                     |
| Object next()         | 사용전 hasNext() 사용 권장                          |
| Object previous()     | 사용전 hasPrevious() 사용 권장                      |
| int nextIndex()       | 다음 요소의 인덱스 반환                             |
| int previousIndex()   | 이전 요소의 인덱스 반환                             |
| void remove()         | 반드시 next() 또는 previous() 호출 후 사용          |
| void set(Object o)    | 객체 변경. 반드시 next() 또는 previous 호출 후 사용 |

```java
import java.util.*;

class ListIteratorEx{
  public static void main(String[] args){
    ArrayList list = new ArrayList();
    list.add("1");
    list.add("2");
    list.add("3");
    list.add("4");
    list.add("5");
    
    ListIterator it = list.listIterator();
    
    while(it.hasNext()){
      System.out.print(it.next());
    }
    System.out.println();
    
    while(it.hasPrevious()){
      System.out.print(it.previous());
    }
    System.out.println();
  }
}

/*
12345
54321
*/
```

## Iterator 예제들

- 복사(copy)와 이동(move)

```java
package JavaStandard;

import java.util.ArrayList;
import java.util.Iterator;

public class IteratorExCopyMove {
    public static void main(String[] args) {

        ArrayList original = new ArrayList(10);
        ArrayList copy = new ArrayList(10);
        ArrayList move = new ArrayList(10);

        for (int i = 0; i < 10; i++) {
            original.add(i+"");
        }

        Iterator it = original.iterator();

        while (it.hasNext()) {
            copy.add(it.next());
        }

        System.out.println("= original에서 copy로 복사 =");
        System.out.println("original:" + original);
        System.out.println("copy:" + copy);

        //iterator는 재사용이 안되므로 다시 얻어와야 함
        it = original.iterator();

        while(it.hasNext()){
            move.add(it.next());
            it.remove();
        }

        System.out.println("= original에서 move로 이동 =");
        System.out.println("original:" + original);
        System.out.println("move:" + move);

    }
}

/*
= original에서 copy로 복사 =
original:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
copy:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
= original에서 move로 이동 =
original:[]
move:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
*/
```

- Vector클래스의 데이터 삭제
  - MyVector2 클래스는 따로 있지만 여기서는 생략함

```java
import java.util.*;

class MyVector2Test{
  public static void main(String args[]){
    MyVecor2 v = new MyVector2();
    v.add("0");
    v.add("1");
    v.add("2");
    v.add("3");
    v.add("4");
    
    System.out.println("삭제 전 : " + v);
    Iterator it = v.iterator();
    it.next();
    it.remove();
    it.next();
    it.remove();
    
    System.out.println("삭제 후 : " + v);
  }
}
/*
삭제 전 : [0, 1, 2, 3, 4]
삭제 후 : [2, 3, 4]
*/
```

