# Circle Double Linked List(원형 이중 연결리스트)

- 연결리스트의 꼬리가 머리를 가리킴
- 고리모양으로 나열된 데이터를 저장할때 알맞음(버스, 지하철 노선등)
- 노드클래스 Node<E>
  - Node()
    - data가 NULL이고 앞,뒤 포인터가 this인 노드 생성
    - 자기 자신의 노드가 앞쪽 노드이면서 동시에 다음 노드가 됨
  - Node(E obj, Node<E> prev, Node<e> next)
    - data가 obj이고, 앞쪽 포인터가 prev, 뒤쪽 포인터가 next인 노드 생성

```java
import java.util.Comparator;

//원형 이중 연결리스트
public class CircleDobuleLinkedList<E> {

    //노드
    class Node<E> {
        private E data;
        private Node<E> prev;
        private Node<E> next;

        //생성자1
        Node(){
            data = null;
            prev = next = this;
        }

        //생성자2
        Node(E obj, Node<E> prev, Node<E> next){
            data = obj;
            this.prev = prev;
            this.next = next;
        }
    }
    
    private Node<E> head; //머리 노드 (더미노드) - 자기 자신을 가리킴
    private Node<E> current; //선택 노드
    
    //생성자
    public CircleDobuleLinkedList() { 
        head = current = new Node<E>(); //더미노드 생성
    }
    
    //비었는지 확인
    public boolean isEmpty() {
        return head.next == head;
    }
    
    //검색
    public E search(E obj, Comparator<? super E> c){
        Node<E> ptr = head.next; //현재 스캔중인 노드

        while (ptr != head) {
            if (c.compare(obj, ptr.data) == 0) {
                current = ptr;
                return ptr.data; //검색 성공
            }
            //다음노드로 선택
            ptr = ptr.next;
        }
        //검색 실패
        return null;
    }
    
    //선택노드 출력
    public void printCurrentNode(){
        if(isEmpty()){
            System.out.println("선택 노드가 없습니다.");
        } else {
            System.out.println(current.data);
        }
    }
    
    //모든 노드 출력
    public void dump(){
        Node<E> ptr = head.next; //더미 노드의 다음 논드

        while (ptr != head) {
            System.out.println(ptr.data);
            ptr = ptr.next;
        }
    }
    
    //모든 노드를 거꾸로 출력
    public void dumpReverse() {
        Node<E> ptr = head.prev;

        while (ptr != head) {
            System.out.println(ptr.data);
            ptr = ptr.prev;
        }
    }
    
    //선택 노드를 하나 뒤쪽으로 이동
    public boolean next() {
        if (isEmpty() || current.next == head) {
            return false; //이동 할 수 없음
        }
        current = current.next;
        return true;
    } 
    
    //선택 노드를 하나 앞쪽으로 이동
    public boolean prev(){
        if (isEmpty() || current.prev == head) {
            return false; //이동 할 수 없음
        }
        current = current.prev;
        return true;
    }
    //선택노드의 바로 뒤에 노드를 삽입
    public void add(E obj) {
        Node<E> node = new Node<E>(obj, current, current.next);
        current.next =current.next.prev = node;
        current = node;
    }
    
    //머리노드에 노드 삽입
    public void addFirst(E obj) {
        current = head; //더미 노드 head의 바로 뒤에 삽입
        add(obj);
    }
    
    //꼬리 노드에 노드 삽입
    public void addLast(E obj) {
        current = head.prev; //꼬리 노드 head.prev의 바로 뒤에 삽입
        add(obj);
    }
    
    //선택 노드 삭제
    public void removeCurrentNode(){
        if (!isEmpty()) {
            current.prev.next = current.next;
            current.next.prev = current.prev;
            current = current.prev;
            if (current == head) {
                current = head.next;
            }
        }
    }
    
    //노드 p를 삭제
    public void remove(Node p) {
        Node<E> ptr = head.next;

        while (ptr != head) {
            if(ptr == p){ //p를 찾음
                current = p;
                removeCurrentNode();;
                break;
            }
            ptr = ptr.next;
        }
    }
    
    //머리 노드를 삭제
    public void removeFirst(){
        current = head.next; //머리 노드 head.next를 삭제
        removeCurrentNode();
    }
    
    //꼬리 노드를 삭제
    public void removeLast() {
        current = head.prev; //꼬리 노드 head.prev삭제
        removeCurrentNode();
    }
    
    //모든 노드 삭제
    public void clear(){
        while (!isEmpty()) { //텅 빌 때 까지
            removeFirst(); //머리노드 삭제
        }
    }
    
    //머리부터 n개 뒤 노드의 데이터에 대한 참조를 반환
    public E retrieve(int n){
        Node<E> ptr = head.next;

        while (n >= 0 && ptr.next.next != head) {
            if (n-- == 0) {
                current = ptr;
                return ptr.data; //검색 성공
            }
            ptr = ptr.next; //뒤족노드에 주목
        }
        return (null);
    }

}
```