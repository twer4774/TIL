# Collection Framework - Stack, Queue

- Stack
  - LIFO(Last In FIrst Out)

  - ArrayList로 구현

    | 메서드                   | 설명                                                         |
    | ------------------------ | ------------------------------------------------------------ |
    | boolean empty()          | Stack이 비었는지 확인                                        |
    | Object peek()            | 가장 위에 있는 객체 반환. 데이터를 삭제하지 않음             |
    | Object pop()             | 가장 위에 있는 객체 반환. 데이터 삭제                        |
    | Object push(Object item) | Stack에 객체 저장                                            |
    | int search(Object o)     | Stack에서 주어진 객체를 찾아 그 위치를 반환, 못찾으면 -1 반환 |

  

- Queue

  - FIFO(First In FIrst Out)

  - LinkedList로 구현 : 항상 첫번째 요소를 삭제하므로 빈공간을 채우는 행위를 줄이기 위함

    | 메서드                  | 설명                                                         |
    | ----------------------- | ------------------------------------------------------------ |
    | boolean add(Object o)   | 객체를 저장. 성공 true, 저장공간 부족시 IllegalStateException발생 |
    | Object remove()         | 객체 반환. 비었으면 NoSuchElementException발생               |
    | Object element()        | 삭제없이 요소를 읽어 옴. 비었으면 NoSuchEelementException발생 |
    | boolean offer(object o) | 객체 저장. 성공 true, 실패 false                             |
    | Object poll()           | 객체 반환, 비었으면 null반환                                 |
    | Object peek()           | 삭제없이 요소를 읽어옴. 비었으면 null 반환                   |

## 스택, 큐 예제

```java
import java.util.*;

class StackQueueEx{
  public static void main(String[] args){
    Stack st = new Stack();
    Queue q = new LinkedList(); //Queue인터페이스의 구현체인 LinkedList사용
    
    st.push("0");
    st.push("1");
    st.push("2");
    
    q.offer("0");
    q.offer("1");
    q.offer("2");
    
    System.out.println("= Stack =");
    while(!st.empty()){
      System.out.println(st.pop()); 
    }
    
    System.out.println("= Queue =");
    while(!q.isEmpy()){
      System.out.println(q.poll());
    }
  }
}

/*
=Stack=
2
1
0
=Queue=
0
1
2
*/
```

## 스택 직접 구현

```java
import java.util.*;

public class MyStack extends Vector{
    
    public Object push(Object item){
        addElement(item);
        return item;
    }

    public Object pop() {
        Object obj = peek(); //마지막 요소 읽어오기
        
        //만일 스택이 비었으면 EmptyStackException 발생
        //마지막 요소 삭제. 인덱스가 0부터 시작이므로 1을 빼줌
        removeElementAt(size() -1);
        return obj;
    }

    public Object peek(){
        int len = size();
        
        if(len == 0){
            throw new EmptyStackException();
        }
        //마지막 요소 반환. 인덱스가 0부터 시작이므로 1을 빼줌
        return elementAt(len -1);
    }
    
    public boolean empty(){
        return size() == 0;
    }
    
    public int search(Object o){
      int i = lastIndexOf(o);
      
      if(i>=0){
          return size() - i;
      }
      
      return -1;
    }
}
```

## 스택의 활용 - 웹브라우저의 뒤로가기, 앞으로 가기

```java
import java.util.Stack;

public class StackExWebBrowser {
    public static Stack back = new Stack();
    public static Stack forward = new Stack();

    public static void main(String[] args) {
        goURL("1.nate");
        goURL("2.yahoo");
        goURL("3.naver");
        goURL("4.kakao");

        printStatus();

        goBack();
        System.out.println("=뒤로가기 버튼을 누룬 후=");
        printStatus();

        goBack();
        System.out.println("= '뒤로' 버튼을 누룬 후=");
        printStatus();

        goForward();
        System.out.println("='앞으로' 버튼을 누룬 후=");
        printStatus();

        goURL("codechobo.com");
        System.out.println("=새로운 주소 이동 후=");
        printStatus();

    }

    public static void printStatus(){
        System.out.println("back:"+back);
        System.out.println("forward:"+forward);
        System.out.println("현재 화면은 " + back.peek() + " 입니다");
        System.out.println();
    }

    public static void goURL(String url) {
        back.push(url);
        if (!forward.empty()) {
            forward.clear();
        }
    }

    public static void goForward(){
        if (!forward.empty()) {
            back.push(forward.pop());
        }
    }

    public static void goBack(){
        if (!back.empty()) {
            forward.push(back.pop());
        }
    }
}

/*
back:[1.nate, 2.yahoo, 3.naver, 4.kakao]
forward:[]
현재 화면은 4.kakao 입니다

=뒤로가기 버튼을 누룬 후=
back:[1.nate, 2.yahoo, 3.naver]
forward:[4.kakao]
현재 화면은 3.naver 입니다

= '뒤로' 버튼을 누룬 후=
back:[1.nate, 2.yahoo]
forward:[4.kakao, 3.naver]
현재 화면은 2.yahoo 입니다

='앞으로' 버튼을 누룬 후=
back:[1.nate, 2.yahoo, 3.naver]
forward:[4.kakao]
현재 화면은 3.naver 입니다

=새로운 주소 이동 후=
back:[1.nate, 2.yahoo, 3.naver, codechobo.com]
forward:[]
현재 화면은 codechobo.com 입니다
*/
```

## 스택의 활용 - 괄호 체크하기

```java
import java.util.EmptyStackException;
import java.util.Stack;

/**
 * 스택을 이용한 괄호 체크
 */
public class StackExValidCheck {

    public static void main(String[] args) {
        if(args.length !=1 ){
            System.out.println("Usage: java ExpValidCheck \"EXPRESSION\"");
            System.out.println("Example: java ExpValidCheck \"((2+3)*1)+3\"");
            System.exit(0);
        }

        Stack stack = new Stack();
        String expression = args[0];

        System.out.println("expression: " + expression);

        try{
            for (int i = 0; i < expression.length(); i++) {
                char ch = expression.charAt(i);
                if(ch=='('){
                    stack.push(ch+"");
                } else if (ch == ')') {
                    stack.pop();
                }


                if (stack.isEmpty()) {
                    System.out.println("괄호가 일치합니다.");
                } else {
                    System.out.println("괄호가 일치하지 않습니다.");
                }
            }
        } catch (EmptyStackException e){
            System.out.println("괄호가 일치하지 않음");
        } //try
    }
}
```

## 큐 예제 - 터미널 히스토리

```java
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Queue;
import java.util.Scanner;

public class QueueExTerminalHistory {

    static Queue q = new LinkedList();
    static final int MAX_SIZE = 5;


    public static void main(String[] args) {

        System.out.println("help를 입력하면 도움말을 볼 수 있음");

        while(true) {
            System.out.println(">>");
            try {
                Scanner s = new Scanner(System.in);
                String input = s.nextLine().trim();

                if("".equals(input)) continue;

                if(input.equalsIgnoreCase("q")){
                    System.exit(0);
                }
                else if(input.equalsIgnoreCase("help")){
                    System.out.println("help - 도움말 보이기");
                    System.out.println("q 또는 Q - 프로그램 종료");
                    System.out.println("history - 최근 입력 명령어 " + MAX_SIZE +"개 보이기");
                } else if(input.equalsIgnoreCase("history")){
                    int i = 0;
                    //입력받은 명령 저장
                    save(input);

                    //링크드 리스트의 내용 보이기
                    LinkedList tmp = (LinkedList)q;
                    ListIterator it = tmp.listIterator();

                    while (it.hasNext()) {
                        System.out.println(++i+"."+it.next());
                    }
                } else {
                    save(input);
                    System.out.println(input);
                }
            } catch (Exception e) {
                System.out.println("입력 오류");
            } //try
        } //while
    }

    public static void save(String input) {
        //queue에 저장
        if (!"".equals(input)) {
            q.offer(input);
        }

        //queue의 최대 크기를넘으면 제일 처음 입력된 것을 삭제
        if(q.size() > MAX_SIZE) {
            q.remove();
        }
    }
}

/*
help를 입력하면 도움말을 볼 수 있음
>> help
help - 도움말 보이기
q 또는 Q - 프로그램 종료
history - 최근 입력 명령어 5개 보이기
>> dir
dir
>> cd
cd
>> mkdir
mkdir
>> dir
dir
>> history
1.dir
2.cd
3.mkdir
4.dir
5.history
>> q
*/
```

## 우선순위 큐

- 각 요소를 heap이라는 자료구조 형태로 저장하여 가장 크거나 작은 값을 빠르게 찾을 때 이용

```java
import java.util.PriorityQueue;
import java.util.Queue;

public class PriorityQueueEx {
    public static void main(String[] args) {
        Queue pq = new PriorityQueue();
        pq.offer(3); //pq.offer(new Integer(3)) 오토박싱
        pq.offer(1);
        pq.offer(5);
        pq.offer(2);
        pq.offer(4);

        System.out.println(pq); //pq내부 배열 출력

        Object obj = null;

        //Priority Queue에 저장된 요소를 하나씩 꺼냄
        while ((obj = pq.poll()) != null) {
            System.out.println(obj);
        }
    }

}

/*
[1, 2, 5, 3, 4] //힙형태로 저장하는 pq의 내부배열
1
2
3
4
5
*/
```

