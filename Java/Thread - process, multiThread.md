# Thread - process, multiThread

## 프로세스와 쓰레드

프로세스 : 실행 중인 프로그램

- 프로그램을 실행하면 OS로부터 실행에 필요한 자원을 할당받아 프로세스가 됨

프로세스는 프로그램을 수행하는 데 필요한 데이터와 메모리 등의 자원, 그리고 쓰레드로 구성

- 쓰레드 : 프로세스의 자원을 이용해서 실제로 작업을 수행하는 것

모든 프로세스에는 최소한 하나 이상의 쓰레드가 존재하며, 둘 이상의 쓰레드를 가진 프로세스를 '멀티쓰레드 프로세스'라고 함

- 하나의 프로세스가 가질 수 있는 쓰레드의 개수는 제한되어 있지 않으나, 쓰레드가 작업을 수행하는데 개별적인 메모리공간(호출스택)을 필요로 하기 때문에 프로세스의 <u>메모리 한계</u>에 따라 생성할 수 있는 쓰레드의 수가 결정 됨

### 멀티태스크와 멀티쓰레딩

- 우리가 사용하고 있는 윈도나 유닉스를 포함한 대부분의 OS는 멀티태스킹(다중작업)을 지원하기 때문에 여러 프로세스가 동시에 실행될 수 있음
- 멀티 쓰레딩 : 하나의 프로세스 내에서 여러 쓰레드가 동시에 작업을 수행하는 것
  - CPU의 코어가 한 번에 단 하나의 작업만 수행할 수 있으므로, 실제로 동시에 처리되는 작업의 개수는 코어의 개수와 일치
  - 처리해야할 쓰레드의 수는 항상 코어의 개수보다 많으므로 코어는 쓰레드를 번걸아가면서 처리함

### 멀티쓰레딩의 장단점

- 장점
  - CPU의 사용률 향상
  - 자원을 효율적으로 사용
  - 사용자에 대한 응답성 향상
  - 작업이 분리되어 코드가 간결해짐
- 단점
  - 자원 공유시 동기화 문제
  - 교착상태 문제
    - 두 쓰레드가 자원을 점유한 상태에서 서로 상대편이 점유한 자원을 사용하려고 기다리느라 진행이 멈춰있는 상태

## 쓰레드의 구현과 실행

- 쓰레드를 구현한다 => run() 메서드의 몸통을 채운다

- 쓰레드를 구현하는 방법
  - Thread클래스를 상속받는 방법
    - 이 방법을 사용하면 다른 클래스를 상속받을 수 없기 때문에 아래의 방법 이용
  - Runnable 인터페이스를 구현하는 방법(일반적인 방법)
    - 재사용성을 높이고 코드의 일관성을 유지할 수 있기 때문에 보다 객체지향적인 방법이라고 할 수 있음
    - run()만 정의되어 있는 Runnable인터페이스를 구현 함
    - Thread클래스의 메서드를 호출하려면 currentThread()를 이용해 쓰레드에 대한 참조를 얻어야 함

```java
//Thread 클래스를 상속받는 방법
class MyThread extends Thread{
  public void run() { /* 작업 내용 */ } //Thread클래스의 run()을 오버라이딩
}

//Runnable 인터페이스 구현
class MyThread implements Runnable {
  public void run() { /* 작업 내용 */ } //Runnable 인터페이스의 run()을 구현
}
```

```java
/**
 * Thread의 구현방식
 *  1. Thread 클래스 상속
 *  2. Runnable 인터페이스 구현(일반적인 방법)
 *  여기서는 두 방법을 모두 구현하여 차이점을 알아본다
 */
public class ThreadEx {

    public static void main(String[] args) {
        ThreadEx_1 t1 = new ThreadEx_1();

        Runnable r = new ThreadEx_2();
        Thread t2 = new Thread(r); //생성자 Thread(Runnable Target)

        t1.start();
        t2.start();
    }

}

//1.Thread 클래스 상속
class ThreadEx_1 extends Thread{
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println(getName()); //조상인 Thread의 getName()을 호출
        }
    }
}

//2. Runnable 인터페이스 구현
class ThreadEx_2 implements Runnable{
    public void run(){
        for (int i = 0; i < 5; i++) {
            //Thread.currentThread() - 현재 실행중인 Thread 반환
            System.out.println(Thread.currentThread().getName());
        }
    }
}
/*
Thread-0
Thread-0
Thread-0
Thread-0
Thread-0
Thread-1
Thread-1
Thread-1
Thread-1
Thread-1
*/
```

## start()와 run()

- run() :  생성된 쓰레드를 실행시키는 것이 아니라 단순히 클래스에 선언된 메서드를 호출하는 것일 뿐
- start() : 새로운 쓰레드가 작업을 실행하는데 필요한 호출스택을 생성한 다음에 run()을 호출해서, 생성된 호출스택에 run()이 첫번째로 올라가게 함
- 모든 쓰레드는 독립적인 작업을 수행하기 위해 자신만의 호출스택을 필요로 하기 때문에 새로운 쓰레드를 생성하고 실행시킬 때마다 새로운 호출스택이 생성되고 쓰레드가 종료되면 작업에 사용된 호출스택은 소멸됨

## 싱글쓰레드와 멀티쓰레드

### 싱글쓰레드 작업시간

```java
/**
 * 싱글쓰레드로 작업시간 측정
 */
public class ThreadExSingThread {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();

        for (int i = 0; i < 300; i++) {
            System.out.printf("%s", new String("-"));
        }

        System.out.print("소요시간1:" + (System.currentTimeMillis() - startTime));

        for (int i = 0; i < 300; i++) {
            System.out.printf("%s", new String("|"));
        }

        System.out.print("소요시간2:" + (System.currentTimeMillis() - startTime));
    }

}
/*
---- 소요시간1: 59
|||| 소요시간2: 81
*/
```

### 멀티쓰레드에서 작업시간

```java
/**
 * 멀티쓰레드에서 작업시간 측정
 */
public class ThreadExMultiThread {

    static long startTime = 0;

    public static void main(String[] args) {
        ThreadExMultiThread_1 th1 = new ThreadExMultiThread_1();
        th1.start();
        startTime = System.currentTimeMillis();

        for (int i = 0; i < 300; i++) {
            System.out.printf("%s", new String("-"));
        }
        System.out.println("소요시간1:" + (System.currentTimeMillis() - ThreadExMultiThread.startTime));
    }
}

class ThreadExMultiThread_1 extends Thread{
    public void run(){
        for (int i = 0; i < 300; i++) {
            System.out.printf("%s", new String("|"));
        }

        System.out.print("소요시간2: " + (System.currentTimeMillis() - ThreadExMultiThread.startTime));
    }
}
/*
-|... 소요시간2: 45
|--...	소요시간1: 54
*/
```

- 거의 동시에 작업이 완료됨

### 멀티쓰레드로 화면출력 작업

```java
import javax.swing.*;

/**
 * 쓰레드를 이용해 사용자 입력부분과 화면에 숫자를 출력하는 부분을 나눔
 */
public class ThreadExConsole {
    public static void main(String[] args) {
        ThreadExConsole_1 th1 = new ThreadExConsole_1();
        th1.start();

        String input = JOptionPane.showInputDialog("아무 값이나 입력하세요.");
        System.out.println("입력하신 값은 " + input + "입니다.");
    }
}

class ThreadExConsole_1 extends Thread{
    public void run() {
        for (int i = 10; i > 0 ; i++) {
            System.out.println(i);

            try{
                sleep(1000);
            } catch (Exception e){}
        }
    } //run()
}
```

