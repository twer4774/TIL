# CollectionFramewokr - Collections

- 컬렉션과 관련된 메서드 제공
  - fill(), copy(), sort(), binarySearch() 등

### 컬렉션 동기화

- 멀티 쓰레드 환경에서는 동기화가 필요
- Vector와 Hashtable 같은 구버전의 클래스들은 자체적으로 동기화처리가 되어 싱글쓰레드일 경우 불필요한 기능으로 성능저하의 요인이 됨
- ArrayList와 HashMap은 동기화를 자체적으로 처리하지 않으므로 필요한 경우 java.util.Collections 클래스의 동기화 메서드를 이용하여 동기화 처리를 함

```java
List syncList = Collections.synchronizedList(new ArrayList(...));
```

### 변경불가 컬렉션 만들기

- 저장된 데이터를 보호하기 위해 컬렉션을 변경불가로 만드는 경우(읽기전용)
- unmodifiableCollection(collection c) 처럼 unmoidfiable이 접두로 붙는 메서드들 이용

### 싱글톤 컬렉션 만들기

- 인스턴스를 new 연산자가 아닌 메서드를 이용해서만 생성할 수 있게하는 기능
- 접두에 singleton이 붙는 메서드 이용

### Collections예제

```java
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;
import static java.util.Collections.*;

public class CollectionsEx {
    public static void main(String[] args) {
        List list = new ArrayList();
        System.out.println(list);

        addAll(list, 1, 2, 3, 4, 5);
        System.out.println(list);

        rotate(list, 2); //오른쪽으로 두칸씩 이동
        System.out.println("오른쪽으로 두칸씩 이동: "+ list);

        swap(list, 0,2); //첫번째와 세번째 요소 교환
        System.out.println("첫번째와 세번째 요소 교환" + list);

        shuffle(list); //섞기
        System.out.println("shuffle: " +list);

        sort(list);
        System.out.println(list);


        sort(list, reverseOrder());
        System.out.println(list);

        int idx = binarySearch(list, 3); //3이 저장된 위치 반환
        System.out.println("3이 저장된 위치 반환 index of 3 = " + idx);

        System.out.println("max=" + max(list));
        System.out.println("min=" + min(list));
        System.out.println("min="+max(list, reverseOrder()));

        fill(list, 9); //list를 9로 채움
        System.out.println("list를 9로 채움 list="+list);

        //list와 같은 크기의 새로운 list를 생성하고 2로 채움. 단, 결과는 변경불가
        List newList = nCopies(list.size(), 2);
        System.out.println("list와 같은 크기의 새로운 list를 생성하고 2로 채움. 단, 결과는 변경불가 newList=" + newList);

        //공통요소가 없으면 true
        System.out.println("공통요소가 없으면 true " + disjoint(list, newList));


        copy(list, newList);
        System.out.println("newList="+newList);
        System.out.println("list="+list);
        replaceAll(list, 2, 1);
        System.out.println("list="+list);

        Enumeration e = enumeration(list);
        ArrayList list2 = list(e);

        System.out.println("list2="+list2);

    }

}

/*
[]
[1, 2, 3, 4, 5]
오른쪽으로 두칸씩 이동: [4, 5, 1, 2, 3]
첫번째와 세번째 요소 교환[1, 5, 4, 2, 3]
shuffle: [5, 3, 1, 4, 2]
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
3이 저장된 위치 반환 index of 3 = 2
max=5
min=1
min=1
list를 9로 채움 list=[9, 9, 9, 9, 9]
list와 같은 크기의 새로운 list를 생성하고 2로 채움. 단, 결과는 변경불가 newList=[2, 2, 2, 2, 2]
공통요소가 없으면 true true
newList=[2, 2, 2, 2, 2]
list=[2, 2, 2, 2, 2]
list=[1, 1, 1, 1, 1]
list2=[1, 1, 1, 1, 1]
*/
```

