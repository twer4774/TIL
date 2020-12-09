# Collection Framwork - LinkedList

- 배열의 장점
  - 구조가 간단
  - 엑세스 시간이 빠름
- 배열의 단점
  - 크기를 변경할 수 없음 - 충분히 큰 크기의 배열 선언 => 메모리 낭비
  - 비순차적인 데이터의 추가, 삭제에 시간이 많이 걸림
- LinkedList : 배열의 단점들을 보완하기 위해 설계

```java
class Node {
  Node next; //다음 요소의 주소 저장
  Object obj; //데이터 저장
}
```

- Doubly Linked List : 링크드 리스트는 이동 방향이 단방향이기 때문에 다음 요소의 데이터 접근은 쉽지만, 이전 요소의 접근은 어려워 고안된 이중 연결 리스트

```java
class Node {
  Node next; //다음 요소의 주소 저장
  Node previous; //이전 요소의 주소 저장
  Object obj; //데이터 저장
}
```

- Doubly Circular Linked List : 이중 연결리스트 보다 접근성을 높임. 단순히 마지막 요소와 첫번째 요소를 연결
- 자바에서 쓰이는 LinkedList클래스는 실제로 이중연결리스트로 구현되어있음 => 접근성을 높이기 위함

### ArrayList와 LinkedList의 성능 비교

```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class ArrayListLinkedListTest {

    public static void main(String[] args) {
        //추가할 데이터의 개수를 고려하여 충분히 잡아야 함
        ArrayList al = new ArrayList(2000000);
        LinkedList ll = new LinkedList();

        System.out.println("=순차적으로 추가하기=");
        System.out.println("ArrayList : " + add1(al));
        System.out.println("LinkedList : " + add1(ll));
        System.out.println();
        System.out.println("=중간에 추가하기=");
        System.out.println("ArrayList : " + add2(al));
        System.out.println("LinkedList : " + add2(ll));
        System.out.println();
        System.out.println("=중간에서 삭제하기=");
        System.out.println("ArrayList : " + remove2(al));
        System.out.println("LinkedList : " + remove2(ll));
        System.out.println();
        System.out.println("=순차적으로 삭제하기=");
        System.out.println("ArrayList : " + remove1(al));
        System.out.println("LinkedList : " + remove1(ll));
         
    }

    public static long add1(List list) {
        long start = System.currentTimeMillis();
        for(int i=0; i<1000000; i++){
            list.add(i + "");
        }
        long end = System.currentTimeMillis();
        return end - start;
    }

    public static long add2(List list) {
        long start = System.currentTimeMillis();
        for(int i=0; i<10000; i++){
            list.add(500 + "X");
        }
        long end = System.currentTimeMillis();
        return end - start;
    }

    public static long remove1(List list){
        long start = System.currentTimeMillis();
        for(int i=list.size()-1; i>=0; i--){
            list.remove(i);
        }
        long end = System.currentTimeMillis();
        return end - start;
    }

    public static long remove2(List list){
        long start = System.currentTimeMillis();
        for(int i=0; i<10000; i++){
            list.remove(i);
        }
        long end = System.currentTimeMillis();
        return end - start;
    }

}

/*
=순차적으로 추가하기=
ArrayList : 238
LinkedList : 1379

=중간에 추가하기=
ArrayList : 3860
LinkedList : 13

=중간에서 삭제하기=
ArrayList : 3622
LinkedList : 150

=순차적으로 삭제하기=
ArrayList : 8
LinkedList : 22
*/
```

- 결론
  - 순차적으로 추가/삭제하는 경우 => ArrayList가 빠름
  - 중간에서 추가/삭제하는 경우 => LinkedList가 빠름