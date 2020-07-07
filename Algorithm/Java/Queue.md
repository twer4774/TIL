# Queue

데이터를 일시적으로 쌓아놓는 배열로 만든 자료구조

dequeue의 비효율때문에 Ring Buffer Queue를 기본적으로 사용함

- FIFO(First In First Out): 가장 먼저 넣은 데이터를 가장 먼제 꺼냄
- enqueue: 데이터를 넣는 작업 / dequeue: 데이터를 꺼내는 작업 / front: 데이터를 꺼내는 쪽 / rear: 데이터를 넣는 쪽
  - enqueue: rear + 1을 하여 데이터 저장. 시간복잡도는 O(1)
  - dequeue: front에 있는 데이터를 꺼낸 후 나머지 데이터들을 앞으로 옮겨야 한다. 꺼낼때마다 이런 작업을해야하므로, O(n)이 걸려서 비효율적임 => Ring buffer queue로 개선함

- Queue

  ```java
  //Int Queue
  
  public class IntQueue {
      
      //큐가 비었음
      public class EmptyIntArrQueueException extends RuntimeException{
          public EmptyIntArrQueueException(){}
      }
      //큐가 가득참
      public class OverflowIntArrQueueException extends RuntimeException{
          public OverflowIntArrQueueException(){}
      }
      
      private int max; //큐의 용량
      private int num; //현재 데이터 수
      private int[] que; //큐의 본체
      
      //생성자
      public IntQueue(int capacity){
          num = 0;
          max = capacity;
          
          try {
              que = new int[max];
          } catch (OutOfMemoryError e){
              max = 0; 
          }
      }
      
      //enqueue
      public int enqueue(int x) throws OverflowIntArrQueueException{
          if(num >= max){
              throw new OverflowIntArrQueueException(); //큐가 가득참
          }
          que[num++] = x; //enqueue
          return x;
      }
      
      //dequeue
      public int deque() throws EmptyIntArrQueueException{
          if(num <= 0){
              throw new EmptyIntArrQueueException(); //큐가 비었음
          }
          int x = que[0];
          for(int i = 0; i < num - 1; i++){
              que[i] = que[i + 1];
          }
          num--;
          return x;
      }
      
      //peek
      public int peek() throws EmptyIntArrQueueException{
          if (num <= 0){
              throw new EmptyIntArrQueueException();
          }
          return que[num - 1];
      }
      
      //index
      public int indexOf(int x){
          for (int i = 0; i < num; i++){
              if(que[i] == x)
                  return i;
          }
          return -1; //검색 실패
      }
      
      //clear
      public void clear() { num = 0; }
      //capcity
      public int capacity() { return max; }
      //size
      public int size() { return num; }
      //isEmpty
      public boolean isEmpty() { return num <= 0; }
      //isFull
      public boolean isFull() { return max <= num; }
      //dump - front-> rear순으로 차례로 출력
      public void dump(){
          if (num<=0){
              System.out.println("Queue is Empty");
          }
          else {
              for (int i=0; i<num; i++){
                  System.out.println(que[i]);
              }
          }
      }
      public static void main(String[] args) {
  
      }//main
  }
  ```

   

## Ring Buffer Queue

- 배열의 처음이 끝과 연결되어 있는 자료구조
- front: 맨 처음 요소의 인덱스 / rear: 맨 끝 요소의 하나 뒤의 인덱스(다음 요소를 인큐할 위치를 미리 지정)
- 일반 queue에서 발생했던 dequeue의 데이터 이동을 방지 할 수 있다. 시간복잡도가 O(n) -> O(1)로 변화

```java
//int 형 ring buffer queue

public class IntRingBufferQueue {
    
    private int max;
    private int front; //첫번째요소 커서
    private int rear; //마지막 요소 커서
    private int num; //현재 데이터 수
    private int[] que; //큐 본체
    
    //큐가 비었음
    public class EmptyIntRingQueueException extends RuntimeException{
        public EmptyIntRingQueueException() {}
    }
    //큐가 가득참
    public class OverflowIntRingQueueException extends RuntimeException{
        public OverflowIntRingQueueException() {}
    }
    
    //생성자
    public IntRingBufferQueue(int capacity){
        num = front = rear = 0;
        max = capacity;
        try {
            que = new int[max]; //큐 본체용 배열 생성
        } catch (OutOfMemoryError e) {
            max = 0;
        }
    }
    
    //enqueue
    public int enqueue(int x) throws OverflowIntRingQueueException{
        if(num >= max){
            throw new OverflowIntRingQueueException(); //큐가 가득 참
        }
        que[rear++] = x;
        num++;
        if(rear == max)
            rear = 0;
        return x;
    }
    
    //dequeue
    public int deque() throws EmptyIntRingQueueException {
        if (num <= 0)
            throw new EmptyIntRingQueueException(); // 큐가 비어 있음
        int x = que[front++];
        num--;
        if (front == max)
            front = 0;
        return x;
    }
    
    
    //peek
    public int peek() throws EmptyIntRingQueueException{
        if(num <= 0)
            throw new EmptyIntRingQueueException();
        return que[front];
    }
    
    //index
    public int indexOf(int x ){
        for (int i = 0; i < num; i++){
            int idx = (i + front) % max;
            if(que[idx] == x){
                return idx;
            }
        }
        
        return -1;
    }
    
    //clear
    public void clear() { num = front = rear = 0; }
    //capacity
    public int capacity() { return max; }
    //size
    public int size() { return num; }
    //isEmpty
    public boolean isEmpty() { return num <= 0; }
    //isFull
    public boolean isFull() { return num >= max; }
    //dump fornt->rear
    public void dump(){
        if(num <= 0){
            System.out.println("Queue is empty");
        } else {
            for (int i = 0; i < num; i++) {
                System.out.println(que[(i + front) % max]);
            }
        }
    }
    //search - key값이 몇번째 요소에 있는가 머리부터 검색
    public int search(int x) {
        for (int i = 0; i < num; i ++){
            if(que[(i + front) % max] == x){
                return i + 1;
            }
        }
        return 0; //검색 실패
    }
    public static void main(String[] args) {

    }//main
}
```

- 내장 Queue함수 이용

```java
import java.util.Scanner;

//int queue 사용 예
public class IntQueueTester {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        IntQueue s = new IntQueue(64);
        
        while (true) {
            System.out.println("현재 데이터 수 : " + s.size() + " / " + s.capacity());
            System.out.println("1인큐 / 2디큐 / 3피크 / 4덤프 / 0종료");
            
            int menu = stdIn.nextInt();
            if (menu == 0) break;
            
            int x; 
            switch (menu) {
                case 1:
                    System.out.println("데이터: ");
                    x = stdIn.nextInt();
                    try {
                        s.enqueue(x);
                    } catch (IntQueue.OverflowIntArrQueueException e){
                        System.out.println("큐가 가득 참");
                    }
                    break;
                case 2:
                    try{
                        x = s.deque();
                        System.out.println("디큐한 데이터 : " + x);
                    } catch (IntQueue.EmptyIntArrQueueException e){
                        System.out.println("큐가 비어 있음");
                    }
                    break;
                case 3:
                    try{
                        x = s.peek();
                        System.out.println("피크한 데이터 : " + x);
                    } catch (IntQueue.EmptyIntArrQueueException e){
                        System.out.println("큐가 비었음");
                    }
                    break;
                case 4:
                    s.dump();
                    break;
            }
        }
    }//main
}
```



- Generic Queue

```java
public class Gqueue<E> {
	// 실행할 때 예외：큐가 비어 있음
	public static class EmptyGqueueException extends RuntimeException {
		public EmptyGqueueException() {
		}
	}

	// 실행할 때 예외：큐가 가득 참
	public static class OverflowGqueueException extends RuntimeException {
		public OverflowGqueueException() {
		}
	}

	private int max; // 큐의 용량
	private int num; // 현재의 데이터 수
	private int front; // 맨 앞 커서
	private int rear; // 맨 뒤 커서
	private E[] que; // 큐의 본체

	// 생성자
	public Gqueue(int capacity) {
		num = front = rear = 0;
		max = capacity;
		try {
			que = (E[]) new Object[max]; // 큐 본체용 배열을 생성
		} catch (OutOfMemoryError e) {   // 생성할 수 없습니다.
			max = 0;
		}
	}

	// 큐에 데이터를 인큐
	public E enque(E x) throws OverflowGqueueException {
		if (num >= max)
			throw new OverflowGqueueException(); // 큐가 가득 참
		que[rear++] = x;
		num++;
		if (rear == max)
			rear = 0;
		return x;
	}

	// 큐에서 데이터를 디큐
	public E deque() throws EmptyGqueueException {
		if (num <= 0)
			throw new EmptyGqueueException(); // 큐가 비어 있음
		E x = que[front++];
		num--;
		if (front == max)
			front = 0;
		return x;
	}

	// 큐에서 데이터를 피크(머리데이터를 살펴봄)
	public E peek() throws EmptyGqueueException {
		if (num <= 0)
			throw new EmptyGqueueException(); // 큐가 비어 있음
		return que[front];
	}

	// 큐에서 x를 검색하여 index(찾지 못하면 -1)를 반환
	public int indexOf(E x) {
		for (int i = 0; i < num; i++)
			if (que[(i + front) % max] == x) // 검색성공
				return i + front;
		return -1; // 검색실패
	}

	// 큐에서 x를 검색하여 머리부터 몇 번 째인가(찾지 못하면 -1)를 반환
	public int search(E x) {
	      for (int i = 0; i < num; i++)
	         if (que[(i + front) % max].equals(x))   // 검색 성공
	            return i + 1;
	      return -1;                            	 // 검색 실패
	}

	// 큐를 비움
	public void clear() {
		num = front = rear = 0;
	}

	// 큐의 용량을 반환
	public int capacity() {
		return max;
	}

	// 큐에 쌓인 데이터 수를 반환
	public int size() {
		return num;
	}

	// 큐가 비어 있는가?
	public boolean isEmpty() {
		return num <= 0;
	}

	// 큐가 가득 찼는가?
	public boolean isFull() {
		return num >= max;
	}

	// 큐 안의 데이터를 머리→꼬리의 차례로 나타냄
	public void dump() {
		if (num <= 0)
			System.out.println("큐가 비었습니다.");
		else {
			for (int i = 0; i < num; i++)
				System.out.print(que[(i + front) % max].toString() + " ");
			System.out.println();
		}
	}
}
```

