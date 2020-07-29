# Hash(해시)

데이터의 검색, 추가, 삭제를 효율적으로 수행하는 자료구조

## Hasing(해시법)

- 데이터를 저장할 위치를 간단한 연산으로 구하는것 - 해시함수이용
- 해시함수를 이용해 해시테이블 작성
- 버킷 : 해시테이블의 요소

### Collision(충돌)

해시 값이 같은 경우 발생

해시 함수는 해시값이 치우치지 않도록 만들어야 함

#### 충돌 대처

- 체인법(오픈해시법) : 같은 해시값을 갖는 요소를 연결리스트로 관리
  - 69와 17을 13으로 나누면(해시함수) 해시값이 4로 중복됨
  - 연결리스트를 이용해 해시테이블 인덱스 4의 위치에 69 -> 17저장
- 오픈주소법(닫힌해시법) : 빈 버킷을 찾을 때 까지 해시를 반복

## 체인법

```java
public class ChainHash<K, V> {
    //해시를 구성하는 노드
    class Node<K, V> {
        private K key;
        private V data;
        private Node<K, V> next;

        //생성자
        Node(K key, V data, Node<K, V> next) {
            this.key = key;
            this.data = data;
            this.next = next;
        }

        //키 값을 반환
        K getKey() { return key; }

        //데이터 반환
        V getValue() { return data; }

        //키의 해시값을 반환
        public int hashCode() { return key.hashCode(); }
    }

    private int size; //해시 테이블의 크기
    private Node<K, V>[] table; //해시 테이블

    //생성자
    public ChainHash(int capacity){
        try{
            table = new Node[capacity];
            this.size = capacity;
        } catch (OutOfMemoryError e){ //데이터를 생성할 수 없음
            this.size = 0;
        }
    }

    //해시 값 구하기
    public int hashValue(Object key) { return key.hashCode() % size; }

    //검색 - 키 값이 가지는 데이터 반환
    public V search(K key){
        int hash = hashValue(key); //검색할 데이터의 해시값
        Node<K, V> p = table[hash]; //선택 노드

        while (p != null) {
            if (p.getKey().equals(key)) {
                return p.getValue(); //검색 성공
            }
        }

        return null; //검색 실패
    }


    //키 값 key, 데이터 data를 갖는 요소의 추가
    public int add(K key, V data){
        int hash = hashValue(key); //추가할 데이터의 해시 값
        Node<K, V> p = table[hash]; //선택 노드

        while(p != null){
            if (p.getKey().equals(key)) { //키 값이 이미 등록된 경우
                return 1;
            }
            p = p.next; //다음 노드설정
        }

        Node<K,V> temp = new Node<K,V>(key, data, table[hash]);
        table[hash] = temp; //노드 삽입
        return 0;
    }

    //키에 해당하는 요소 삭제
    public int remove(K key){
        int hash = hashValue(key); //삭제할 데이터의 해시 값
        Node<K,V> p = table[hash];
        Node<K,V> pp = null; //바로 앞의 선택 노드

        while (p != null) {
            if(p.getKey().equals(key)){ //해당 값을 찾으면
                if(pp == null){
                    table[hash] = p.next;
                } else {
                    pp.next = p.next;
                }
                return 0;
            }

            pp = p;
            p = p.next; //다음 노드를 가리킴
        }
        return 1; //키 값이 존재하지 않음
    }

    //해시 테이블을 덤프
    public void dump(){
        for(int i = 0; i < size; i++){
            Node<K,V> p = table[i];
            System.out.printf("%02d ", i);
            while(p != null){
                System.out.printf("-> %s (%s) ", p.getKey(), p.getValue());
                p = p.next;
            }
            System.out.println();
        }
    }
}
```

- 테스터

```java
import java.util.Scanner;

//체인법에 의한 해시 사용
public class ChainHashTester {
    static Scanner stdIn = new Scanner(System.in);

    // 데이터(회원번호+이름)
    static class Data {
        static final int NO = 1; // 번호를 입력 받습니까?
        static final int NAME = 2; // 이름을 입력 받습니까?

        private Integer no; // 회원번호 (키값)
        private String name; // 이름

        // 키값
        String keyCode() {
            return name;
        }

        // 문자열을 반환합니다.
        public String toString() {
            return Integer.toString(no);
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
    }

    // 메뉴열거형
    enum Menu {
        ADD("데이터 추가"), REMOVE("데이터 삭제"), SEARCH("데이터 검색"), DUMP("모든  데이터 출력"), TERMINATE("종료");

        private final String message; // 표시용 문자열

        static Menu MenuAt(int idx) { // 서수가 idx임. 열거를 반환
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
        } while (key < Menu.ADD.ordinal() || key > Menu.TERMINATE.ordinal());

        return Menu.MenuAt(key);
    }

    public static void main(String[] args) {
        Menu menu; // 메뉴
        Data data; // 추가용 데이터 참조
        Data temp = new Data(); // 입력 받기용 데이터

        ChainHash<String, Data> hash = new ChainHash<String, Data>(13);

        do {
            switch (menu = SelectMenu()) {
                case ADD:
                    data = new Data(); // 추가
                    data.scanData("추가", Data.NO | Data.NAME);
                    int k = hash.add(data.keyCode(), data);
                    switch (k) {
                        case 1:
                            System.out.println("그 키값은 이미 등록되어 있습니다.");
                            break;
                        case 2:
                            System.out.println("해시 테이블이 가득 찼습니다.");
                            break;
                    }
                    break;

                case REMOVE: // 삭제
                    temp.scanData("삭제", Data.NAME);
                    hash.remove(temp.keyCode());
                    break;

                case SEARCH: // 검색
                    temp.scanData("검색", Data.NAME);
                    Data t = hash.search(temp.keyCode());
                    if (t != null)
                        System.out.println("그 키를 갖는 데이터는 " + t + "입니다.");
                    else
                        System.out.println("해당 하는 데이터가 없습니다.");
                    break;

                case DUMP: // 출력
                    hash.dump();
                    break;
            }
        } while (menu != Menu.TERMINATE);
    }
}
```

```
0으로 데이터 추가
1
붉은꼬리

2로 붉은꼬리 검색 => 1
```



## 오픈주소법

```java
//오픈 주소법에 의한 해시

public class OpenAddressHash<K, V> {
    
    //버킷의 상태
    enum Status { OCCUPIED, EMPTY, DELETED};
    
    //버킷
    static class Bucket<K,V>{
        private K key;
        private V data;
        private Status stat; //상태
        
        //생성자
        Bucket() { stat = Status.EMPTY; }
        
        //모든 필드에 값을 설정
        void set(K key, V data, Status stat){
            this.key = key;
            this.data = data;
            this.stat = stat;
        }
        
        //상태 설정
        void setStat(Status stat) { this.stat = stat; }
        
        //키 값 반환
        K getKey() { return key; }
        
        //데이터 반환
        V getValue() { return data; }
        
        //키의 해시 값 반환
        public int hashCode() { return key.hashCode(); }
    }
    
    private int size;
    private Bucket<K, V>[] table; //해시 테이블
    
    //생성자
    public OpenAddressHash(int size){
        try{
            table = new Bucket[size];
            for (int i = 0; i < size; i++) {
                table[i] = new Bucket<K,V>();
            }
            this.size = size;
        } catch (OutOfMemoryError e){
            this.size = 0;
        }
    }
    
    //해시 값을 구함
    public int hashValue(Object key) { return key.hashCode() % size; }
    
    //재해시값을 구함
    public int rehashValue(int hash) { return (hash + 1) % size; }
    
    
    //키 값 key를 갖는 버킷의 검색
    private Bucket<K, V> searchNode(K key){
        int hash = hashValue(key); //검색할 데이터의 해시 값
        Bucket<K,V> p = table[hash]; //선택 버킷

        for (int i = 0; p.stat != Status.EMPTY && i < size; i++) {
            if (p.stat == Status.OCCUPIED && p.getKey().equals(key)) {
                return p;
            }
            hash = rehashValue(hash); //재해시
            p = table[hash];
        }
        return null;
    }
    
    //키 값을 갖는 요소 검색 - 데이터 반환
    public V search(K key){
        Bucket<K,V> p = searchNode(key);
        if(p != null){
            return p.getValue();
        } else {
            return null;
        }
    }
    
    //키 값, 데이터를 갖는 요소의 추가
    public int add(K key, V data) {
        if(search(key) != null){
            return 1;
        }
        
        int hash = hashValue(key); //추가할 데이터의 해시 값
        Bucket<K,V> p = table[hash]; //선택 버킷
        for (int i = 0; i < size; i++) {
            if (p.stat == Status.EMPTY || p.stat == Status.DELETED) {
                p.set(key, data, Status.OCCUPIED);
                return 0;
            }

            hash = rehashValue(hash);
            p = table[hash];
        }
        return 2; //해시 테이블이 가득참
    }
    
    
    //키 값 key를 갖는 요소 삭제
    public int remove(K key){
        Bucket<K, V> p = searchNode(key); //키 값 검색
        
        if(p == null){
            return 1; //없는 키 값
        }
        
        p.setStat(Status.DELETED);
        return 0;
    }
    
    //해시테이블 덤프
    public void dump(){
        for (int i = 0; i < size; i++) {
            System.out.printf("%02d ", i);
            switch (table[i].stat){
                case OCCUPIED:
                    System.out.printf("%s (%s)\n", table[i].getKey(), table[i].getValue());
                    break;
                case EMPTY:
                    System.out.printf("--- 미등록 ---");  break;
                    
                case DELETED:
                    System.out.printf("---- 삭제 마침 ----"); break;
            }
        }
    }
  
}
```

- 테스터

```java
import java.util.Scanner;

public class OpenAddressHashTester {
    static Scanner stdIn = new Scanner(System.in);

    // 데이터(회원번호+이름)
    static class Data {
        static final int NO = 1; // 번호를 입력 받습니까?
        static final int NAME = 2; // 이름을 입력 받습니까?

        private Integer no; // 회원번호 (키값)
        private String name; // 이름

        // 키 값
        String keyCode() {
            return name;
        }

        // 문자열을 반환합니다.
        public String toString() {
            return Integer.toString(no);
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
    }

    // 메뉴열거형
    enum Menu {
        ADD("데이터 추가"), REMOVE("데이터 삭제"), SEARCH("데이터 검색"), DUMP("모든  데이터 출력"), TERMINATE("종료");

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
        } while (key < Menu.ADD.ordinal() || key > Menu.TERMINATE.ordinal());

        return Menu.MenuAt(key);
    }

    public static void main(String[] args) {
        Menu menu; // 메뉴
        Data data; // 추가용 데이터 참조
        Data temp = new Data(); // 입력 받기용 데이터

        OpenAddressHash<String, Data> hash = new OpenAddressHash<String, Data>(13);

        do {
            switch (menu = SelectMenu()) {
                case ADD:
                    data = new Data(); // 추가
                    data.scanData("추가", Data.NO | Data.NAME);
                    int k = hash.add(data.keyCode(), data);
                    switch (k) {
                        case 1:
                            System.out.println("그 키값은 이미 등록되어 있습니다.");
                            break;
                        case 2:
                            System.out.println("해시 테이블이 가득 찼습니다.");
                            break;
                    }
                    break;

                case REMOVE: // 삭제
                    temp.scanData("삭제", Data.NAME);
                    hash.remove(temp.keyCode());
                    break;

                case SEARCH: // 검색
                    temp.scanData("검색", Data.NAME);
                    Data t = hash.search(temp.keyCode());
                    if (t != null)
                        System.out.println("그 키를 갖는 데이터는 " + t + "입니다.");
                    else
                        System.out.println("해당 하는 데이터가 없습니다.");
                    break;

                case DUMP: // 나타냄
                    hash.dump();
                    break;
            }
        } while (menu != Menu.TERMINATE);
    }
}
```

