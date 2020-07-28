# Tree(트리)

데이터 사이의 계층구조를 나타내는 자료구조

- 배열과 연결리스트로 구현 가능
  - 배열의 구현인 경우 힙(heap)과 관련됨
- 용어
  - 루트 : 트리의 시작이 되는 노드. 트리의 루트노드는 하나만 존재
  - 리프 : 끝 노드, 바깥 노드. 더 이상 자식노드가 없는 노드
  - 안쪽노드 : 루트, 리프 노드를 제외한 끝이 아닌 노드
  - 자식, 부모, 형제, 조상, 자손 노드들이 존재
  - 레벨 : 루트부터 레벨 0 순으로 레벨 1, 레벨 2… 증가
  - 차수 : 노드가 갖는 자식의 수. 모든 노드의 차수가 n이하인 트리 - n진트리
  - 높이 : 리프 레벨의 최댓값

## 순서트리 탐색

### 너비우선 탐색(breadth-first search, BFS)

- 낮은 레벨에서 시작해 왼쪽에서 오른쪽 노드로 탐색을 함
- 사용하는 경우
  - 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 사용
- 특징(그래프의 경우)
  - 직관적이지 않은 면이 있다 - 시작 노드에서 거리에 따라 단계별로 탐색한다고 볼 수 있다.
  - 재귀적으로 동작하지 않는다.
  - 그래프 탐색의 경우 어떤 노드를 방문했었는지 여부를 반드시 검사해야함 - 무한루프에 빠질 수 있음
  - 큐를 이용해 선입선출 원칙으로 탐색
  - Prim, Dijkstra 알고리즘과 유사
  - 시간복잡도
    - 인접리스트로 표현된 그래프 : O(N+E)
    - 인접행렬로 표현된 그래프 : O(N^2)
    - 인접리스트를 사용하는것이 유리할 수 있음

### 깊이우선 탐색(depth-first search, DFS)

- 리프까지 내려가면서 검색 실시. 리프에 도달 후 부모로 돌아감

- 중간 노드의 경우 여러번 지나칠 수 있음 - 지나치는 것과 방문은 다른 개념임을 숙지할 것

- 언제 방문하는가?

  - 전위 순회 : 노드방문 -> 왼쪽 자식 -> 오른쪽 자식

  - 중위 순회 : 왼쪽 자식 -> 노드방문 -> 오른쪽 자식

  - 후위 순회 : 왼쪽 자식 -> 오른쪽 자식 -> 노드방문

    => 중위 순회방식을 선호 - 이진탐색트리에서도 이용가능(중위 순회를 이용하면 오름차순 정렬 가능)

- 특징(그래프의 경우)
  - 재귀적으로 구현 가능
  - 어떤 노드를 방문했는지 반드시 검사해야 함 - 무한루프에 빠질 수 있음



## 이진트리와 이진검색트리

- 이진 트리 : 각 노드의 자식이 2 이하인 트리

- 완전 이진 트리 : 루트부터 노드가 채워져있으면서 같은 레벨에서는 왼쪽부터 자식이 채워짐

  - 마지막 레벨이 아니라면 노드가 가득차 있어야 함
  - 마지막 레벨은 왼쪽에서 오른쪽 순서대로 채워져야함(양쪽 가득일 필요는 없음)
  - 높이가 k인 완전 이진 트르의 최댓값 = 2^(k+1) - 1
  - n개의 노드를 저장할 수 있는 완전이진트리의 높이 : log n

- 이진검색트리 (DFS의 중위 순회 이용)

  - 조건

    - 어떤 노드 n을 기준으로 왼쪽서브트리 노드의 모든 키의 값은 노드 n의 키값보다 작아야 한다

    - 오른쪽 서브트리노드의 키값은 노드 n의 키값 보다 커야한다

    - 같은 키 값을 갖는 노드는 없다

      => 왼쪽 자식들은 부모보다 작아야 하며, 오른쪽은 커야한다. 중복되는 키 값은 없다

  - 특징

    - 구조가 단순하며 이진검색과 비슷한 방법
    - 노드 삽입이 쉬움

  - 검색 실패

    - 루트부터 실행하며 선택노드는 P

    - P가 Null이면 검색 실패

    - key 값과 P를 비교

      - 값이 같으면 검색 성공

      - key보다 작으면 왼쪽으로 검색(왼쪽노드를 대입)

      - key보다 크면 오른쪽으로 검색

        위의 과정 반복



```java
import java.util.Comparator;

//이진 검색 트리

public class BinTree<K, V> {

    //노드
    static class Node<K, V>{
        private K key; //키 값
        private V data; //데이터
        private Node<K, V> left; //왼쪽 자식 노드
        private Node<K, V> right; //오른쪽 자식 노드

        //생성자
        Node(K key, V data, Node<K, V> left, Node<K, V> right) {
            this.key = key;
            this.data = data;
            this.left = left;
            this.right = right;
        }

        //키 값을 반환
        K getKey() { return key; }

        //데이터 반환
        V getValue() { return data; }

        //데이터 출력
        void print() {
            System.out.println(data);
        }
    }

    private Node<K, V> root; //루트
    private Comparator<? super K> comparator = null; //비교자

    //생성자
    public BinTree(){ root = null; }

    //생성자
    public BinTree(Comparator<? super K> c){
        this();
        comparator = c;
    }

    //두 키값을 비교
    private int comp(K key1, K key2){
        return (comparator == null) ? ((Comparable<K>) key1).compareTo(key2) : comparator.compare(key1, key2);
    }

    //키에 의한 검색
    public V search(K key) {
        Node<K, V> p = root;

        while (true) {
            if (p == null) {
                return null; //검색 실패
            }
            int cond = comp(key, p.getKey()); //key와 노드 p의 키 비교
            if (cond == 0) {
                return p.getValue(); //검색 성공
            } else if (cond < 0){ //key 값이 작으면
                p = p.left; //왼쪽 서브트리에서 검색
            } else { //key 값이 크면
                p = p.right; //오른쪽 서브트리에서 검색
            }
        }
    }

    //node를 루트로 하는 서브 트리에 노드 <K,V> 삽입
    private void addNode(Node<K, V> node, K key, V data) {
        int cond = comp(key, node.getKey());
        if (cond == 0) {
            return; //key가 이진검색트리에 이미 있음
        } else if(cond < 0){
            if (node.left == null) {
                node.left = new Node<K, V>(key, data, null, null);
            } else {
                addNode(node.left, key, data); //왼쪽 서브 트리에 주목
            }
        } else {
            if(node.right == null){
                node.right = new Node<K, V>(key, data, null, null);
            } else {
                addNode(node.right, key, data); //오른쪽 서브트리에 주목
            }
        }
    }

    //노드를 삽입
    public void add(K key, V data){
        if (root == null) {
            root = new Node<K, V>(key, data, null, null);
        } else {
            addNode(root, key, data);
        }
    }

    //키 값이 key인 노드 삭제
    public boolean remove(K key){
        Node<K, V> p = root; //스캔 중인 노드
        Node<K, V> parent = null; //스캔 중인 노드의 부모 노드
        boolean isLeftChild = true; //p는 parent의 왼쪽 자식 노드인가?

        while(true){
            if (p == null) {
                return false; //그 키 값은 없음
            }
            int cond = comp(key, p.getKey()); //key와 노드 p의 키 값을 비교
            if (cond == 0) {
                break; //검색 성공
            } else {
                parent = p; //가지로 내려가 진에 부모를 설정
                if(cond < 0){ //key쪽이 작으면
                    isLeftChild = true; //왼쪽 자식으로 내려감
                    p = p.left; //왼쪽 서브트리에서 검색
                } else { //key쪽이 크면
                    isLeftChild = false; //오른쪽 자식으로 내려감
                    p = p.right; //오른쪽 서브트리에서 검
                }
            }
        }

        if(p.left == null){ //p에는 왼쪽 자식이 없음
            if(p == root){
                root = p.right;
            } else if(isLeftChild){
                parent.left = p.right; //부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            } else {
                parent.right = p.right; //부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
            }
        } else if (p.right == null){ //p에는 오른쪽으 자식이 없음
            if(p == root){
                root = p.left;
            } else if (isLeftChild){
                parent.left = p.left; //부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            } else {
                parent.right = p.left; //부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
            }
        } else {
            parent = p;
            Node<K, V> left = p.left; //서브 트리 가운데 가장 큰 노드
            isLeftChild = true;
            while(left.right != null){ //가장 큰 노드 left를 검색
                parent = left;
                left = left.right;
                isLeftChild = false;
            }
            p.key = left.key; //left의 키 값을 p로 옮김
            p.data = left.data; //left의 데이터를 p로 옮김
            if(isLeftChild){
                parent.left = left.left; //left를 삭제
            } else {
                parent.right = left.left; //left를 삭제
            }
        }
        return true;
    }

    //node를 루트로 하는 서브 트리의 노드를 키 값의 오름차순으로 출력
    private void printSubTree(Node node){
        if(node != null){
            printSubTree(node.left); //왼쪽 서브 트리를 키 값의 오름차순으로 출력
            System.out.println(node.key + " " + node.data); //node를 출력
            printSubTree(node.right); //오른쪽 서브 트리를 키 값의 오름차순으로 출력
        }
    }

    //모든 노드를 키값의 오름차순으로 출력
    public void print() { printSubTree(root); }

    //최소 key의 값을 갖는 노드를 반환
    private Node<K, V> getMinNode(){
        if (root == null) {
            return null;
        } else {
            Node<K, V> p = root;

            while(p.left != null){
                p = p.left;
            }
            return p;
        }
    }

    //최대 key의 값을 갖는 노드 반환
    private Node<K, V> getMaxNode(){
        if (root == null) {
            return null;
        } else {
            Node<K, V> p = root;

            while (p.right != null) {
                p = p.right;
            }
            return p;
        }
    }

    //최소 key의 값을 갖는 노드 반환
    private K getMinkey(){
        Node<K, V> minNOde = getMinNode();
        return (minNOde == null ? null : minNOde.getKey());
    }

    // 최소 key의 값을 갖는 노드의 데이터를 반환
    public V getDataWithMinKey() {
        Node<K, V> minNode = getMinNode();
        return (minNode == null ? null : minNode.getValue());
    }

    // 최대 key의 값을 반환
    public K getMaxKey() {
        Node<K, V> maxNode = getMaxNode();
        return (maxNode == null ? null : maxNode.getKey());
    }

    // 최대 key의 값을 갖는 노드의 데이터를 반환
    public V getDataWithMaxKey() {
        Node<K, V> maxNode = getMinNode();
        return (maxNode == null ? null : maxNode.getValue());
    }
}
```

- 실행

```java
import java.util.Scanner;
import java.util.Comparator;

//이진 검색트리 실행

public class BinTreeTester {

    static Scanner stdIn = new Scanner(System.in);

    //데이터 (회원번호 + 이름)
    static class Data{
        public static final int NO = 1; //번호를 입력 받습니까?
        public static final int NAME = 2; //이름을 입력 받습니까?


        private Integer no; //키값 (회원번호)
        private String name; //이름

        //키 값
        Integer keyCode() { return no; }

        //문자열 반환
        public String toString() { return name; }

        //데이터 입력을 받음
        void scanData(String guide, int sw){
            System.out.println(guide + "하는 데이터를 입력하세요");

            if((sw & NO) == NO){
                System.out.println("번호 : ");
                no = stdIn.nextInt();
            }

            if((sw & NAME) == NAME){
                System.out.println("이름:");
                name = stdIn.next();
            }
        }
    }

    // 메뉴열거형
    enum Menu {
        ADD("삽입 "), REMOVE("삭제"), SEARCH("검색"), PRINT("출력"), TERMINATE("종료");

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

        String getMessage() { // 출력용 문자열 반환
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
        } while (key < Menu.ADD.ordinal() || key > Menu.TERMINATE.ordinal());

        return Menu.MenuAt(key);
    }

    public static void main(String[] args) {
        Menu menu; // 메뉴
        Data data; // 추가용 데이터 참조
        Data ptr; // 검색용 데이터 참조
        Data temp = new Data(); // 입력 받기용 데이터

        class IntegerDecComparator implements Comparator<Integer> {
            public int compare(Integer n1, Integer n2) {
                return (n1 > n2) ? 1 : (n1 < n2) ? -1 : 0;
            }
        }

        // 정수의 내림차순으로 순서매기기를 수행하는 comparator
        final IntegerDecComparator INT_DEC_COMP = new IntegerDecComparator();
        BinTree<Integer, Data> tree = new BinTree<Integer, Data>(INT_DEC_COMP);

        //BinTree<Integer, Data> tree = new BinTree<Integer, Data>();

        do {
            switch (menu = SelectMenu()) {
                case ADD: // 노드의 삽입
                    data = new Data();
                    data.scanData("삽입 ", Data.NO | Data.NAME);
                    tree.add(data.keyCode(), data);
                    break;

                case REMOVE: // 노드의 삭제
                    temp.scanData("삭제", Data.NO);
                    tree.remove(temp.keyCode());
                    break;

                case SEARCH: // 노드의 검색
                    temp.scanData("검색", Data.NO);
                    ptr = tree.search(temp.keyCode());
                    if (ptr != null)
                        System.out.println("그 번호의 이름은 " + ptr + "입니다.");
                    else
                        System.out.println("해당 데이터가 없습니다.");
                    break;

                case PRINT : // 노드의 출력
                    tree.print();
                    break;
            }
        } while (menu != Menu.TERMINATE);
    }
}
```

