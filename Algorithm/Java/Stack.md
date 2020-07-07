# Stack

데이터를 일시적으로 저장하기 위한 <u>배열</u>로 이루어진 자료구조

LIFO(Last In First Out) : 가장 늦게 들어간 데이터가 가장 빨리 나온다.

- Push: 데이터를 넣는 작업 / Pop: 데이터를 꺼내는 작업 / Top: 꼭대기 / Bottom: 가장 아랫부분

## 스택 만들기

```java
//int형 스택

public class IntStack {

    private int max; //용량
    private int ptr; //포인터 = 스택에 쌓여있는 데이터의 수
    private int[] stk; //스택 본체

    //실행시 예외 : 스택이 비어있음
    public class EmptyIntStackException extends RuntimeException{
        public EmptyIntStackException() {}
    }

    //실행시 예외 : 스택이 가득 참
    public class OverflowIntStackException extends RuntimeException {
        public OverflowIntStackException() {}
    }

    //스택에 x를 푸시
    public int push(int x) throws OverflowIntStackException{
        if( ptr >= max ){
            throw new OverflowIntStackException();
        }
        return stk[ptr++] = x; //ptr++는 후위증가이므로 stk[ptr]에 x를 저장한 후 ptr값이 올라간다.
    }

    //스택에서 팝(정상에 있는 데이터를 꺼냄)
    public int pop() throws EmptyIntStackException{
        if( ptr <= 0 ){
            throw new EmptyIntStackException();
        }
        return stk[--ptr];
    }

    //스택에서 데이터를 피크(저애상에 있는 데이터를 들여다 봄)
    public int peek() throws EmptyIntStackException{
        if (ptr <=0 ){
            throw new EmptyIntStackException();
        }
        return stk[ptr - 1]; //스택이 비어 있지 안으면 꼭대기의 요소 stk[ptr -1] 반환. 이때 포이넡는 변화 없음
    }

    //스택에 x를 찾아 인덱스(없으면 -1) 반환
    public int indexOf(int x){
        for (int i = ptr - 1; i >= 0; i--){ //정상쪽에서 선형검색
            if(stk[i] == x){
                return i; //검색 성공
            }
        }
        return -1; //검색 실패
    }

    //스택 비움 - ptr을 0으로 설정
    public void clear() {
        ptr = 0;
    }

    //스택의 용량을 바ㅏㄴ환
    public int capacity() {
        return max;
    }

    //스택에 쌓여 있는 데이터 수를 반환
    public int size(){
        return ptr;
    }

    //스택이 비었는지 확인
    public boolean isEmpty() {
        return ptr <= 0;
    }

    //스택이 가득 찼는지 확인
    public boolean isFull(){
        return ptr >= max;
    }

    //스택 안의 모든 데이터를 바닥 -> 꼭대기 순으로 출력
    public void dump(){
        if(ptr <= 0){
            System.out.println("스택이 비었습니다.");
        } else {
            for(int i = 0; i < ptr; i++){
                System.out.println(stk[i] + " ");
            }
        }
    }
    //생성자
    public IntStack(int capacity){
        ptr = 0;
        max = capacity;
        try {
            stk = new int[max]; //스택 본체용 배열 생성
        } catch (OutOfMemoryError e) { //생성할 수 없을 때
            max = 0;
        }
    }
    public static void main(String[] args) {

    }//main
}
```



### 스택 사용하기

```java
import java.util.Scanner;

//int형 스택의 사용


public class IntStackTester {

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        IntStack s = new IntStack(64); //최대 64개의 크기

        while (true ) {
            System.out.println("현재 데이터 수 : " + s.size() + " / " + s.capacity()); //size는 데이터의 수 / capacity는 스택의 크기

            System.out.println("1푸시 / 2팝 / 3피크 / 4덤프 / 5검색 / 6비움 / 7정보표시 / 0종료 ");

            int menu = stdIn.nextInt();
            if (menu == 0) break;

            int x;
            switch (menu){
                case 1:
                    System.out.println("데이터 : ");
                    x = stdIn.nextInt();

                    try {
                        s.push(x);
                    } catch (IntStack.OverflowIntStackException e){
                        System.out.println("스택이 가득 찼습니다.");
                    }
                    break;

                case 2:
                    try {
                        x = s.pop();
                        System.out.println("팝한 데이터는 : " + x);
                    } catch (IntStack.EmptyIntStackException e) {
                        System.out.println("스택이 비었습니다.");
                    }
                    break;
                case 3:
                    try {
                        x = s.peek();
                        System.out.println("피크한 데이터는 " + x);
                    } catch(IntStack.EmptyIntStackException e){
                        System.out.println("스택이 비었습니다.");
                    }
                    break;

                case 4:
                    s.dump();
                    break;
                    
                case 5:
                    System.out.println("찾을 데이터 : ");
                    x = stdIn.nextInt();
                    int n = s.indexOf(x);
                    if ( n >= 0){
                        System.out.println("꼭대기부터 " + (s.size() - n) + "번 째에 있습니다.");
                    } else {
                        System.out.println("해당 데이터가 없습니다.");
                    }
                    break;
                case 6:
                    s.clear();
                    break;
                    
                case 7:
                    System.out.println("용량 " + s.capacity());
                    System.out.println(" 데이터 수 " + s.size());
                    System.out.println("비어 " + (s.isEmpty() ? "있습니다." : "있지 않습니다."));
                    System.out.println("가득 " + (s.isFull() ? "찼습니다." : "차지 않았습니다."));
            }
        }
    }//main
}
```

