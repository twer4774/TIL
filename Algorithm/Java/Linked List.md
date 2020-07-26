# LinkedList(연결리스트)

- 리스트 : 데이터를 순서대로 나열한 자료구조
- 노드(요소) : 데이터

## 포인터를 이용한 연결리스트

- 일반 선형리스트의 문제점 - 배열로 구현
  - 배열로 구현하여 좋으나, 배열의 크기를 미리 알고 있어야 함
  - 데이터의 삽입, 삭제 시 데이터의 이동이 필요 - 효율이 떨어짐
- 포인터를 이용해 다음 노드의 값을 저장함

```java
class Node<E>{
  E data; //데이터
  Node<E> next; //다음 노드를 가리키는 포인터
}
```

### 코드

```java
import java.util.Comparator;

//연결리스트 구현

public class LinkedList<E> {

    //노드
    class Node<E>{
        private E data; //데이터
        private Node<E> next; //다음 포인터

        //노드의 생성자
        Node(E data, Node<E> next) {
            this.data = data;
            this.next = next;
        }
    }

    private Node<E> head; //머리 노드
    private Node<E> current; //선택 노드

    //LinkedList의 생성자
    public LinkedList(){
        head = current = null; //모두 null로 초기화
    }

    //노드 검색
    public E search(E obj, Comparator<? super E> c) {
        Node<E> ptr = head; //현재 스캔중인 노드

        while (ptr != null) {
            if (c.compare(obj, ptr.data) == 0) { //검색 성공
                current = ptr;
                return ptr.data;
            }
            ptr = ptr.next; //다음 노드 선택
        }
        return null; //검색 실패
    }

    //머리에 노드 삽입
    public void addFirst(E obj) {
        Node<E> ptr = head; //삽입전의 머리 노드
        head = current = new Node<E>(obj, ptr);
    }

    //꼬리에 노드 삽입
    public void addLast(E obj) {
        if (head == null) { //리스트가 비었으면
            addFirst(obj); //머리에 삽입
        } else {
            Node<E> ptr = head;
            while(ptr.next != null){
                ptr = ptr.next;
            }
            ptr.next = current = new Node<E>(obj, null);
        }
    }

    //머리 노드 삭제
    public void removeFirst(){
        if (head != null) { //리스트가 비어있지 않으면
            head = current = head.next;
        }
    }

    //꼬리 노드 삭제
    public void removeLast(){
        if (head != null) {
            if (head.next == null) { //노드가 하나만 존재
                removeFirst(); //머리 노드 삭제
            } else {
                Node<E> ptr = head; //스캔 중인 노드
                Node<E> pre = head; //스캔 중인 노드의 앞쪽 노드

                while (ptr.next != null) {
                    pre = ptr; //pre에 스캔중인 노드 저장
                    ptr = ptr.next; //ptr에 다음 노드 저장
                }

                pre.next = null; //pre는 삭제 후의 꼬리노드가 됨
                current = pre;
            }
        }
    }

    //노드 p 삭제 - 특정 노드 삭제
    public void remove(Node p) {
        if (head != null){
            if (p == head) { //p가 머리노드라면
                removeFirst(); //머리 노드 삭제
            } else {
                Node<E> ptr = head;

                while (ptr.next != p) {
                    ptr = ptr.next;
                    if (ptr == null) {
                        return; //p가 리스트에 없음
                    }

                    ptr.next = p.next;
                    current = ptr;
                }
            }
        }
    }

    //선택 노드 삭제
    public void removeCurrentNode() { remove(current); }

    //모든 논드 삭제
    public void clear() {
        while (head != null) { //노드에 아무것도 없을때까지
            removeFirst(); //머리 노드 삭제
        }
        current = null;
    }

    //선택 노드를 하나 뒤쪽으르 이동
    public boolean next(){
        if (current == null || current.next == null) {
            return false; //이동 할 수 없음
        }
        current = current.next;
        return true;
    }

    //선택 노드를 출력
    public void printCurrentNode(){
        if (current == null) {
            System.out.println("선택한 노드가 없습니다.");
        } else {
            System.out.println(current.data);
        }
    }

    //모든 논드 출력
    public void dump(){
        Node<E> ptr = head;

        while (ptr != null) {
            System.out.println(ptr.data);
            ptr = ptr.next;
        }
    }

    //compartor c에 의해 서로 같다고 보는 노드를 모두 삭제
    public void purge(Comparator<? super E> c) {
        Node<E> ptr = head;

        while (ptr != null) {
            int count = 0;
            Node<E> ptr2 = ptr;
            Node<E> pre = ptr;

            while(pre.next != null){
                ptr2 = pre.next;
                if (c.compare(ptr.data, ptr2.data) == 0) {
                    pre.next = ptr2.next;
                    count++;
                } else {
                    pre = ptr2;
                }
            }

            if (count == 0) {
                ptr = ptr.next;
            } else {
                Node<E> temp = ptr;
                remove(ptr);
                ptr = temp.next;
            }
        }
        current = head;
    }
}

```

- 연결리스트 테스터

```java
import java.util.Scanner;
import java.util.Comparator;

public class LinkedListTester {
    static Scanner stdIn = new Scanner(System.in);

    // 데이터(회원번호+이름)
    static class Data {
        static final int NO = 1; // 번호를 읽어 들일까요?
        static final int NAME = 2; // 이름을 읽어 들일까요?

        private Integer no; // 회원번호
        private String name; // 이름

        // 문자열 표현을 반환
        public String toString() {
            return "(" + no + ") " + name;
        }

        // 데이터를 입력 받음
        void scanData(String guide, int sw) {
            System.out.println(guide + "하는 데이터를 입력하세요.");

            if ((sw & NO) == NO) {
                System.out.print("번호：");
                no = stdIn.nextInt();
            }
            if ((sw & NAME) == NAME) {
                System.out.print("이름：");
                name = stdIn.next();
            }
        }

        // 회원번호에 의한 순서매기기를 수행하는 comparator
        public static final Comparator<Data> NO_ORDER = new NoOrderComparator();

        private static class NoOrderComparator implements Comparator<Data> {
            public int compare(Data d1, Data d2) {
                return (d1.no > d2.no) ? 1 : (d1.no < d2.no) ? -1 : 0;
            }
        }

        // 이름에 의한 순서매기기를 수행하는 comparator
        public static final Comparator<Data> NAME_ORDER = new NameOrderComparator();

        private static class NameOrderComparator implements Comparator<Data> {
            public int compare(Data d1, Data d2) {
                return d1.name.compareTo(d2.name);
            }
        }
    }

    // 메뉴열거형
    public enum Menu {
        ADD_FIRST("머리에 노드를 삽입 "), ADD_LAST("꼬리에 노드를 삽입 "), RMV_FIRST("머리 노드를 삭제"), RMV_LAST("꼬리 노드를 삭제"), RMV_CRNT(
                "선택 노드를 삭제"), CLEAR("모든 노드를 삭제"), SEARCH_NO("번호로 검색"), SEARCH_NAME("이름으로 검색"), NEXT(
                "선택 노드를 하나 뒤쪽으로 이동"), PRINT_CRNT("선택 노드를 출력"), PURGE_NO("같은 번호의 노드를 삭제"), PURGE_NAME(
                "같은 이름의 노드를 삭제"), RETRIEVE("임의의 노드를 출력"), DUMP("모든 노드를 출력"), TERMINATE("종료");

        private final String message; // 표시용 문자열

        static Menu MenuAt(int idx) { // 서수가 idx인 열거를 return
            for (Menu m : Menu.values())
                if (m.ordinal() == idx)
                    return m;
            return null;
        }

        Menu(String string) { // 생성자
            message = string;
        }

        String getMessage() { // 표시용 문자열을 반환
            return message;
        }
    }

    // 메뉴선택
    static Menu SelectMenu() {
        int key;
        do {
            for (Menu m : Menu.values()) {
                System.out.printf("(%d) %s  ", m.ordinal(), m.getMessage());
                if ((m.ordinal() % 3) == 2 && m.ordinal() != Menu.TERMINATE.ordinal())
                    System.out.println();
            }
            System.out.print("：");
            key = stdIn.nextInt();
        } while (key < Menu.ADD_FIRST.ordinal() || key > Menu.TERMINATE.ordinal());
        return Menu.MenuAt(key);
    }

    public static void main(String[] args) {
        Menu menu; // 메뉴
        Data data; // 추가용 데이터 참조
        Data ptr; // 검색용 데이터 참조
        Data temp = new Data(); // 입력 받는용 데이터

        LinkedList<Data> list = new LinkedList<Data>(); // 리스트를 생성

        do {
            switch (menu = SelectMenu()) {

                case ADD_FIRST: // 머리에 노드를 삽입
                    data = new Data();
                    data.scanData("머리에 삽입 ", Data.NO | Data.NAME);
                    list.addFirst(data);
                    break;

                case ADD_LAST: // 꼬리에 노드를 삽입
                    data = new Data();
                    data.scanData("꼬리에 삽입 ", Data.NO | Data.NAME);
                    list.addLast(data);
                    break;

                case RMV_FIRST: // 머리 노드를 삭제
                    list.removeFirst();
                    break;

                case RMV_LAST: // 꼬리 노드를 삭제
                    list.removeLast();
                    break;

                case RMV_CRNT: // 선택 노드를 삭제
                    list.removeCurrentNode();
                    break;

                case SEARCH_NO: // 회원번호로 검색
                    temp.scanData("검색", Data.NO);
                    ptr = list.search(temp, Data.NO_ORDER);
                    if (ptr == null)
                        System.out.println("그 번호의 데이터가 없습니다.");
                    else
                        System.out.println("검색성공：" + ptr);
                    break;

                case SEARCH_NAME: // 이름으로 검색
                    temp.scanData("검색", Data.NAME);
                    ptr = list.search(temp, Data.NAME_ORDER);
                    if (ptr == null)
                        System.out.println("그 이름의 데이터가 없습니다.");
                    else
                        System.out.println("검색성공：" + ptr);
                    break;

                case NEXT: // 선택 노드를 뒤쪽으로 진행
                    list.next();
                    break;

                case PRINT_CRNT: // 선택 노드의 데이터를 출력
                    list.printCurrentNode();
                    break;

                case DUMP: // 모든 노드를 리스트 순서로 출력
                    list.dump();
                    break;

                case CLEAR: // 모든 노드를 삭제
                    list.clear();
                    break;

                case PURGE_NO: // 같은 번호의 노드를 삭제
                    list.purge(Data.NO_ORDER);
                    break;

                case PURGE_NAME: // 같은 이름의 노드를 삭제
                    list.purge(Data.NAME_ORDER);
                    break;
            }
        } while (menu != Menu.TERMINATE);
    }
}
```



## 커서를 이용한 연결리스트

- 배열의 크기와 커서(포인터역할을 하는 인덱스)를 이용할 수 있음
- 포인터를 이용한 연결리스트의 경우 - 노드의 삽입, 삭제 시 노드 객체를 위한 메모리의 생성 및 해제가 필요함
- 데이터의 수가 크게 바뀌지 않고 최대 데이터의수를 알 수 있을 경우 이용하면 좋음 - 서비스에서 이러한 경우가 있을까?

```java
import java.util.Comparator;

//커서를 이용한 연결리스트

public class CursorLinkedList<E> {

    //노드
    class Node<E>{
        private E data; //데이터
        private int next; //리스트의 뒤쪽 포인터(뒤쪽 노드의 index)
        private int dnext; //free 리스트의 뒤쪽데이터(뒤쪽 노드의 index)

        //data와 next 설정
        void set(E data, int next) {
            this.data = data;
            this.next = next;
        }
    }

    private Node<E>[] n; //리스트 본체
    private int size; //리스트 용량
    private int max; //사용중인 꼬리 record
    private int head; //머리노드
    private int tail; //꼬리노드
    private int current; //선택노드
    private int deleted; //free 리스트의 머리 노드
    private static final int NULL = -1; //뒤쪽 노드는 없습니다.

    //생성자
    public CursorLinkedList(int capacity){
        head = tail = current = max = deleted = NULL;

        try{
            n = new Node[capacity];
            for (int i = 0; i < capacity; i++) {
                n[i] = new Node<E>();
            }
            size = capacity;
        } catch (OutOfMemoryError e){ //배열 생성에 실패
            size = 0;
        }
    }

    //다음에 삽입하는 record의 index를 구함
    private int getInsertIndex(){
        if(deleted == NULL) { //삭제할 record가 없음
            if(max < size){
                return ++max; //새 record를 사용
            } else {
                return NULL; //용량 초과
            }
        } else {
            int rec = deleted; //free 리스트에서
            deleted = n[rec].dnext; //머리 rec를 꺼냄
            return rec;
        }
    }

    //record index를 free 리스트에 등록
    private void deleteIndex(int idx){
        if(deleted == NULL ){
            deleted = idx; //idx를 free리스트의
            n[idx].dnext = NULL; //머리에 등록
        } else {
            int rec = deleted; //idx를 free리스트의
            deleted = idx; //머리에 삽입
            n[idx].dnext = rec;
        }
    }

    //노드 검색
    public E search(E o, Comparator<? super E> c) {
        int ptr = head; //현재 스캔중인 노드

        while(ptr != NULL){
            if (c.compare(o, n[ptr].data) == 0) {
                current = ptr;
                return n[ptr].data; //검색성공
            }
            ptr = n[ptr].next; //뒤쪽 노드에 주목
        }
        return null; //검색 실패
    }

    //머리에 노드 삽입
    public void addFirst(E o){
        boolean empty = (tail == NULL);
        int ptr = head;
        int rec = getInsertIndex();
        if(rec != NULL){
            head = current = rec; //인덱스 rec인 record 삽입
            n[head].set(o, ptr);
            if(empty){
                tail = current;
            }
        }
    }

    //꼬리에 노드 삽입
    public void addLast(E o){
        if(head == NULL){
            addFirst(o);
        } else {
            int rec = getInsertIndex();
            if(rec != NULL){
                n[tail].next = current = rec;
                n[rec].set(o, NULL);
                tail = rec;
            }
        }
    }

    //머리노드를 삭제
    public void removeFirst(){
        if(head != NULL){
            int ptr = n[head].next;
            deleteIndex(head);
            head = current = ptr;
            if(head == NULL){
                tail = NULL;
            }
        }
    }

    //꼬리 노드 삭제
    public void removeLast(){
        if(head != NULL){
            if(n[head].next == NULL){
                removeFirst();
            } else {
                int ptr = head; //스캔중인 노드
                int pre = head; //스캔중인 노드의 앞쪽 노드

                while(n[ptr].next != NULL){
                    pre = ptr;
                    ptr= n[ptr].next;
                }
                n[pre].next = NULL; //pre 삭제 뒤의 꼬리노드
                deleteIndex(ptr);
                tail = current = pre;
            }
        }
    }

    //record p를 삭제
    public void remove(int p) {
        if(head != NULL){
            if (p == head) { //p가 머리노드면
                removeFirst(); //머리노드 삭제
            } else if (p == tail){ //p가 꼬리노드면
                removeLast(); //꼬리노드 삭제
            }  else {
                int ptr = head;

                while (n[ptr].next != p){
                    ptr = n[ptr].next;
                    if(ptr == NULL){
                        return; //p가 리스트에 없음
                    }
                }
                    n[ptr].next = n[p].next;
                    deleteIndex(p);
                    current = ptr;
            }

        }
    }

    //선택 노드를 삭제
    public void removeCurrentNode() { remove(current); }

    //모든 노드를 삭제
    public void clear(){
        while(head != NULL){
            removeFirst();
        }
        current = NULL;
    }

    //선택 노드를 하나 뒤쪽으로 진행
    public boolean next(){
        if(current == NULL || n[current].next == NULL){
            return false; //나아갈 수 없음
        }
        current = n[current].next;
        return true;
    }

    //선택노드를 출력
    public void printCurrentNode(){
        if(current == NULL){
            System.out.println("선택 노드가 없음");
        } else {
            System.out.println(n[current].data.toString());
        }
    }

    //모든 노드 출력
    public void dump(){
        int ptr = head;

        while(ptr != NULL){
            System.out.println(n[ptr].data.toString());
            ptr = n[ptr].next;
        }
    }

    //comparator c에 의해 서로 같다고 보는 노드를 모두 삭제
    public void purge(Comparator<? super E> c){
        int ptr = head;

        while(ptr != NULL){
            int count = 0;
            int ptr2 = ptr;
            int pre = ptr;

            while(n[pre].next != NULL){
                ptr2 = n[pre].next;
                if (c.compare(n[ptr].data, n[ptr2].data) == 0) {
                    remove(ptr2);
                    count++;
                } else {
                    pre = ptr2;
                }
            }
            if(count == 0){
                ptr = n[ptr].next;
            } else {
                int temp = n[ptr].next;
                remove(ptr);
                ptr = temp;
            }
        }
            current = head;
    }

    //머리부터 n개 뒤 노드의 데이터에 대한 참조를 반환
    public E retrieve(int n){
        int ptr = head;

        while (n >= 0 && ptr != NULL) {
            if (n-- == 0) {
                current = ptr;
                return this.n[ptr].data; //검색 성공
            }
            ptr = this.n[ptr].next; //뒤쪽 노드에 주목
        }
        return (null);
    }
}
```

- 테스터

```java
package chap09;
import java.util.Scanner;
import java.util.Comparator;

public class CursorLinkedListTester {
    static Scanner stdIn = new Scanner(System.in);

    // 데이터(회원번호+이름)
    static class Data {
        static final int NO = 1; // 번호를 입력 받습니까?
        static final int NAME = 2; // 이름을 입력 받습니까?

        private Integer no; // 회원번호
        private String name; // 이름

        // 문자열을 반환합니다.
        public String toString() {
            return "(" + no + ") " + name;
        }

        // 데이터를 입력 받음
        void scanData(String guide, int sw) {
            System.out.println(guide + "하는 데이터를 입력하세요.");

            if ((sw & NO) == NO) {
                System.out.print("번호：");
                no = stdIn.nextInt();
            }
            if ((sw & NAME) == NAME) {
                System.out.print("이름：");
                name = stdIn.next();
            }
        }

        // 회원번호에 의한 순서매기기를 수행하는 comparator
        public static final Comparator<Data> NO_ORDER = new NoOrderComparator();

        private static class NoOrderComparator implements Comparator<Data> {
            public int compare(Data d1, Data d2) {
                return (d1.no > d2.no) ? 1 : (d1.no < d2.no) ? -1 : 0;
            }
        }

        // 이름에 의한 순서매기기를 수행하는 comparator
        public static final Comparator<Data> NAME_ORDER = new NameOrderComparator();

        private static class NameOrderComparator implements Comparator<Data> {
            public int compare(Data d1, Data d2) {
                return d1.name.compareTo(d2.name);
            }
        }
    }

    // 메뉴열거형
    public enum Menu {
        ADD_FIRST("머리에 노드를 삽입 "), ADD_LAST("꼬리에 노드를 삽입 "), RMV_FIRST("머리 노드를 삭제"), RMV_LAST("꼬리 노드를 삭제"), RMV_CRNT(
                "선택 노드를 삭제"), CLEAR("모든 노드를 삭제"), SEARCH_NO("번호로 검색"), SEARCH_NAME("이름으로 검색"), NEXT(
                "선택 노드를 하나 뒤쪽으로 이동"), PRINT_CRNT("선택 노드를 출력"), PURGE_NO("같은 번호의 노드를 삭제"), PURGE_NAME(
                "같은 이름의 노드를 삭제"), RETRIEVE("임의의 노드를 출력"), DUMP("모든 노드를 출력"), TERMINATE("종료");

        private final String message; // 표시용 문자열

        static Menu MenuAt(int idx) { // 서수가 idx인 열거를 반환
            for (Menu m : Menu.values())
                if (m.ordinal() == idx)
                    return m;
            return null;
        }

        Menu(String string) { // 생성자
            message = string;
        }

        String getMessage() { // 표시용 문자열을 반환
            return message;
        }
    }

    // 메뉴선택
    static Menu SelectMenu() {
        int key;
        do {
            for (Menu m : Menu.values()) {
                System.out.printf("(%d) %s  ", m.ordinal(), m.getMessage());
                if ((m.ordinal() % 3) == 2 && m.ordinal() != Menu.TERMINATE.ordinal())
                    System.out.println();
            }
            System.out.print("：");
            key = stdIn.nextInt();
        } while (key < Menu.ADD_FIRST.ordinal() || key > Menu.TERMINATE.ordinal());
        return Menu.MenuAt(key);
    }

    public static void main(String[] args) {
        Menu menu; // 메뉴
        Data data; // 추가용 데이터 참조
        Data ptr; // 검색용 데이터 참조
        Data temp = new Data(); // 입력 받기용 데이터

      	//리스트의 크기를 미리 알고 있어야 한다.
        CursorLinkedList<Data> list = new CursorLinkedList<Data>(100);// 리스트를 생성

        do {
            switch (menu = SelectMenu()) {

                case ADD_FIRST: // 머리에 노드를 삽입
                    data = new Data();
                    data.scanData("머리에 삽입 ", Data.NO | Data.NAME);
                    list.addFirst(data);
                    break;

                case ADD_LAST: // 꼬리에 노드를 삽입
                    data = new Data();
                    data.scanData("꼬리에 삽입 ", Data.NO | Data.NAME);
                    list.addLast(data);
                    break;

                case RMV_FIRST: // 머리 노드를 삭제
                    list.removeFirst();
                    break;

                case RMV_LAST: // 꼬리 노드를 삭제
                    list.removeLast();
                    break;

                case RMV_CRNT: // 선택 노드를 삭제
                    list.removeCurrentNode();
                    break;

                case SEARCH_NO: // 회원번호로 검색
                    temp.scanData("검색", Data.NO);
                    ptr = list.search(temp, Data.NO_ORDER);
                    if (ptr == null)
                        System.out.println("그 번호의 데이터가 없습니다.");
                    else
                        System.out.println("검색성공：" + ptr);
                    break;

                case SEARCH_NAME: // 이름으로 검색
                    temp.scanData("검색", Data.NAME);
                    ptr = list.search(temp, Data.NAME_ORDER);
                    if (ptr == null)
                        System.out.println("그 이름의 데이터가 없습니다.");
                    else
                        System.out.println("검색성공：" + ptr);
                    break;

                case NEXT: // 선택 노드를 뒤쪽으로 진행
                    list.next();
                    break;

                case PRINT_CRNT: // 선택 노드의 데이터를 출력
                    list.printCurrentNode();
                    break;

                case DUMP: // 모든 노드를 리스트 순서로 출력
                    list.dump();
                    break;

                case CLEAR: // 모든 노드를 삭제
                    list.clear();
                    break;

                case PURGE_NO: // 같은 번호의 노드를 삭제
                    list.purge(Data.NO_ORDER);
                    break;

                case PURGE_NAME: // 같은 이름의 노드를 삭제
                    list.purge(Data.NAME_ORDER);
                    break;

                case RETRIEVE: { // 임의의 노드를 출력
                    System.out.print("머리부터 몇 번 째：");
                    int no = stdIn.nextInt() - 1;
                    ptr = list.retrieve(no);
                    if (ptr == null)
                        System.out.println("데이터가 없습니다.");
                    else
                        System.out.println("데이터는 " + ptr.toString() + "입니다.");
                }
            }
        } while (menu != Menu.TERMINATE);
    }
}
```

