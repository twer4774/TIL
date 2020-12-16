# CollectionFramwork - TreeSet

- 이진 검색 트리(binary search tree)라는 자료 구조의 형태로 데이터를 저장하는 컬렉션 클래스
  - 이진 검색 트리는 정렬, 검색, 범위검색에서 높은 성능을 보임
  - TreeSet은 이진검색트리의 성능을 향상 시킨 레드-블랙 트리로 구현됨
- 이진트리의 노드 코드

```java
class TreeNode{
  TreeNode left; //왼쪽 자식 노드
  Object element; //객체를 저장하기 위한 참조변수
  TreeNode right; //오른쪽 자식 노드
}
```

### 이진 검색 트리

- 모든 노드는 최대 2개의 자식노드를 가질 수 있음

- 왼쪽자식 노드의 값은 부모 노드의 값 보다 작음
- 오른쪽 자식 노드의 값은 부모 노드의 값 보다 큼
- Set이므로 중복된 값이 허용되지 않음
- 값을 저장하기 위해서는 객체가 Comparable을 구현하거나, Comparator를 제공해 두 객체를 비교할 방법을 알려줘야 함
- 장점
  - 검색 빠름
- 단점
  - 노드 추가삭제에 시간이 걸림(순차적으로 저장하지 않으므로)

| 생성자 또는 메서드                                           | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| TreeSet()                                                    |                                                              |
| TreeSet(Collection c)                                        |                                                              |
| TreeSet(Comparator comp)                                     | 주어진 정렬조건으로 정렬하는 TreeSet 생성                    |
| TreeSet(SortedSet s)                                         | 주어진 SortedSet을 구현한 컬렉션을 저장하는 TreeSet을 생성   |
| boolean add(Object o)<br />boolean addAll(Collection c)      |                                                              |
| Object ceiling(Object o)                                     | 지정된 객체와 같은 객체를 반환. 없으면 큰 값을 가진 객체 중 제일 가까운 값의 객체를 반환, 없으면 null |
| void clear() / Objec clone()                                 |                                                              |
| Comparator comparator()                                      | TreeSet의 정렬 기준(Comparator)를 반환                       |
| boolean contains(Object o)<br />boolean containsAll(Collection c) |                                                              |
| NavigableSet descendingSet()                                 | TreeSet에 저장된 요소들을 역순으로 정렬해서 반환             |
| Object first() / Object last()                               | 정렬된 순서에서 첫 번째 /마지막 객체 반환                    |
| Object floor(Object o)                                       | 지정된 객체와 같은 객체를 반환. 없으면 작은 객체 중 제일 가까운 값의 객체를 반환, 없으면 null |
| SortedSet headSet(Object toElement)                          | 지정된 객체보다 작은 값의 객체들 반환                        |
| NavigableSet headSet(Object toElement, boolean inclusive)    | 지정된 객체보다 작은 값의 객체들 반환. inclusive가 true이면 같은 값의 객체도 포함 |
| Object higher(Object o)<br />Object lower(Object o)          | 지정된 객체보다 큰 값을 가진 객체 중 제일 가까운 객체 반환. 없으면 null<br />지정된 객체보다 작은 값을 가진 객체 중 가장 가까운 값의 객체 반환. 없으면 null |
| boolean isEmpty()                                            |                                                              |
| Iterator iterator()                                          |                                                              |
| Object pollFirst()<br />Object pollLast()                    | TreeSet의 첫번째 요소(제일 작은 값의 객체)<br />TreeSet의 마지막 요소(제일 큰 값의 객체) |
| boolean remove(Object o)                                     |                                                              |
| boolean retainAll(Collection c)                              | 주어진 컬렉션과 공통 요소만 남기고 삭제(교집합)              |
| int size()                                                   |                                                              |
| Spliterator spliterator()                                    | TreeSet의 spliterator 반환                                   |
| SortedSet subSet(Object fromElement, Object toElement)       | 범위 검색의 결과 반환. toElement의 값은 범위에 포함되지 않음 |
| NavigableSet\<E> subSet(E fromElement, boolean fromInclusive, E toElement, boolean toInclusive) | 범위 검색의 결과 반환. Inclusive값이 true이면 범위에 포함    |
| SortedSet tailSet(Object fromElement)                        | 지정된 객체보다 큰 값의 객체들을 반환                        |
| Object[] toArray()                                           | 저장된 객체를 객체배열로 반환                                |
| Object[] toArray(Object[] a)                                 | 저장된 객체를 주어진 객체배열에 저장하여 반환                |

### TreeSetLotto

- HashSetLotto에서는 정렬이 필요하지만, TreeSet에서는 이미 정렬되어있으므로 정렬이 필요 없음

```java
import java.util.*;

class TreeSetLotto{
  public static vodim ain(String[] args){
    Set set = new TreeSet();
    
    for(int i = 0; set.size < 6; i++){
      int num = (int)(Math.random()*45) + 1;
      set.add(num);
    }
    
    System.out.println(set);
  }
}
```

### subSet

```java
import java.util.TreeSet;

public class TreeSetEx {

    public static void main(String[] args) {
        TreeSet set = new TreeSet();

        String from = "b";
        String to = "d";

        set.add("abc");
        set.add("alien");
        set.add("bat");
        set.add("cat");
        set.add("Car");
        set.add("disc");
        set.add("dance");
        set.add("dZZZZ");
        set.add("dzzzz");
        set.add("elephant");
        set.add("elevator");
        set.add("fan");
        set.add("flower");

        System.out.println(set);
        System.out.println("range search: from " + from + " to " + to);
        System.out.println("result1 : " + set.subSet(from, to));
      // d로 시작하는 단어를 포함하고 싶다면 범위 끝에 zzz와 같은 문자열을 붙임
        System.out.println("result2 : " + set.subSet(from, to + "zzz"));
    }
}

/*
[Car, abc, alien, bat, cat, dZZZZ, dance, disc, dzzzz, elephant, elevator, fan, flower]
range search: from b to d
result1 : [bat, cat]
result2 : [bat, cat, dZZZZ, dance, disc]
*/
```

### 트리 검색

```java
import java.util.TreeSet;

public class TreeSetHeadSet {
    public static void main(String[] args) {
        TreeSet set = new TreeSet();
        int[] score = {80, 95, 50, 35, 45, 65, 10, 100};

        for (int i = 0; i < score.length; i++) {
            set.add(new Integer(score[i]));
        }

        System.out.println("50보다 작은 값 : " + set.headSet(new Integer(50)));
        System.out.println("50보다 큰 값 : " + set.tailSet(new Integer(50)));

    }
}

/*
50보다 작은 값 : [10, 35, 45]
50보다 큰 값 : [50, 65, 80, 95, 100]
*/
```

