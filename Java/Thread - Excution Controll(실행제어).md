# Thread - Excution Controll(실행제어)

- 쓰레드 프로그래밍이 어려운 이유는 동기화와 스케줄링 때문
  - 우선순위로 스케줄링기법을 사용할 수 있지만 정교함이 떨어짐

| 메서드                                                       | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| satic void sleep(long millis)<br />static void sllep(long millis, int nanos) | 지정된 시간(천분의 일초 단위)동안 쓰레드를 일시정지 시킴<br />저장한 시간이 지나고 나면 자동으로 다시 실행대기 상태가 됨 |
| void join()<br />void join(long millis)<br />void join(long millis, int nanos) | 지정된 시간동안 쓰레드가 실행<br />지정된 시간이 지나거나 작업이 종료되면 join()을 호출한 쓰레드로 다시 돌아와 실행을 계속함 |
| void interrup()                                              | sleep()이나 join()에 의해 일시정지상태인 쓰레드를 깨워서 실행대기 상태로 만듦<br />해당 쓰레드에서는 InterruptedException이 발생함으로써 일시정지상태를 벗어나게 됨 |
| void stop()                                                  | 쓰레드를 즉시 종료                                           |
| void suspend()                                               | 쓰레드를 일시정지. resume()를 호출하면 다시 실행대기 상태가 됨 |
| void resume()                                                |                                                              |
| static void yield()                                          | 실행 중에 자신에게 주어진 실행시간을 다른 쓰레드에게 양보하고 자신은 실행대기 상태가 됨 |

### 쓰레드의 상태

| 상태                   | 설명                                                         |
| ---------------------- | ------------------------------------------------------------ |
| NEW                    | 쓰레드가 생성되가 start()가 호출되지 않은 상태               |
| RUNNABLE               | 실행 중 또는 실행 가능한 상태                                |
| BLOCKED                | 동기화 블럭에 의해 일시정지된 상태(lock이 풀릴 때까지 기다리는 상태) |
| WAITING, TIMED_WAITING | 쓰레드의 작이 종료되지는 않았지만 실행가능하지 않은 일시정지 상태 |
| TERMINATED             | 쓰레드의 작업이 종료된 상                                    |

### sleep(long millis) - 일정시간동안 쓰레드를 멈춤

```java
static void sleep(long millis)
static void sleep(long millis, int nanos)
  
try{
  Thread.sleep(1, 500000); //쓰레드를 0.0015초 동안 멈추게 함
} catch(InterruptedException e){}
```

### interrupt()와 interrupted() - 쓰레드의 작업 취소

- 진행중인 쓰레드의 작업이 끝나기 전에 취소할 때 이용 => 다운로드파일 정지

```java
Thread th = new Thread();
th.start();

th.interrupt(); //쓰레드 th에 interrupt()를 호출

class MyThread extends Thread {
  public void run(){
    while(!interrupted()){ //interrupted()의 결과가 false인 동안 반복
      ...
    }
  }
}

void intterupt() //쓰레드의 interrupted상태를 false에서 true로 변경
boolean isInterrupted() //쓰레드의 interrupted상태 반환
static boolean interrupted() //현재 쓰레드의 interrupted상태 반환 후 fasle로 변경
```

- 카운트 다운 중에 사용자의 입력이 들어오면 카운트다운 종료

```java
import javax.swing.*;

/**
 * 입력이 들어오면 카운트다운 종료
 */
public class ThreadExInterrupt {
    public static void main(String[] args) {
        ThreadExInterrupt_1 th1 = new ThreadExInterrupt_1();
        th1.start();
        String input = JOptionPane.showInputDialog("아무값이나 입력");
        System.out.println("입력하신 값은 " + input + "입니다.");
        th1.interrupt(); //interrupt()를 호출하면 interrupted상태가 true가 됨
        System.out.println("isInterrupted():" + th1.isInterrupted()); //true
    }
}

class ThreadExInterrupt_1 extends Thread{
    public void run(){
        int i = 10;

        while (i != 0 && !isInterrupted()) {
            System.out.println(i--);
            for (long x = 0; x < 2500000000L; x++) { //시간지연

            }
        } //while
        System.out.println("카운트가 종료되었습니다.");
    }
}
/*
10
9
8
7
6
5
4
입력하신 값은 9입니다.
isInterrupted():true
카운트가 종료되었습니다.
*/
```

### suspend(), resume(), stop()

- 쓰레드의 실행을 제어하는 가장 손쉬운 방법들이지만, 교착상태를 일으키기 때문에 권장하지 않음
- 현재 deprecated 됨
- 메서드가 아닌 boolean 변수로 flag 역할을 주어 작업을 통제하는 방법 이용

### yield() - 다른 쓰레드에게 양보

- 쓰레드 자신에게 주어진 실행시간을 다음 차례의 쓰레드에게 양보
  - 1초의 실행 시간을 할당받은 쓰레드가 0.5초 작업한 뒤 yield()를 호출하면 나머지 시간을 포기하고 대기상태가 됨
- yield()와 intterupt()를 적절히 사용하면 프로그램의 응답성을 높이고 보다 효율적으로 실행이 가능하게 할 수 있음

```java
public class ThreadExYieldInterrupt {

    public static void main(String[] args) {
        ThreadExYieldInterrupt_1 th1 = new ThreadExYieldInterrupt_1("*");
        ThreadExYieldInterrupt_1 th2 = new ThreadExYieldInterrupt_1("**");
        ThreadExYieldInterrupt_1 th3 = new ThreadExYieldInterrupt_1("***");

        th1.start();
        th2.start();
        th3.start();

        try {
            Thread.sleep(2000);
            th1.suspend();
            Thread.sleep(2000);
            th2.suspend();
            Thread.sleep(3000);
            th1.resume();

            Thread.sleep(3000);
            th1.stop();
            th2.stop();

            Thread.sleep(2000);
            th3.stop();
        } catch (InterruptedException e){

        }
    }
}

class ThreadExYieldInterrupt_1 implements Runnable {
    boolean suspended = false;
    boolean stopped = false;

    Thread th;

    ThreadExYieldInterrupt_1(String name){
        th = new Thread(this, name); //Thread(Runnable r, String name)
    }

    public void run(){
        String name = th.getName();

        while (!stopped) {
            if (!suspended) {
                System.out.println(name);
                try{
                    Thread.sleep(1000);
                } catch(InterruptedException e){
                    System.out.println(name + " - interrupted");
                }
            } else {
                Thread.yield();
            }
        }
        System.out.println(name + " - stopped");
    }

    public void suspend(){
        suspended = true;
        th.interrupt();
        System.out.println(th.getName() + " - interrupt() by suspend()");
    }

    public void stop(){
        stopped = true;
        th.interrupt();
        System.out.println(th.getName() + " - interrupt() by stop()");
    }

    public void resume() {
        suspended=false;
    }

    public void start(){
        th.start();
    }
}

/*
*
***
**
***
*
**
* - interrupt() by suspend()
* - interrupted
***
**
***
**
** - interrupt() by suspend()
** - interrupted
***
***
***
*
***
*
***
*
***
* - interrupt() by stop()
* - interrupted
* - stopped
** - interrupt() by stop()
** - stopped
***
***
*** - interrupt() by stop()
*** - interrupted
*** - stopped
*/
```

### join() - 다른 쓰레드의 작업을 기다림

- 시간을 지저애하지 않으면 해당 쓰레드가 작업을 모두 마칠 때까지 기다리게 됨

```java
try{
  th1.join(); //현재 실행중인 쓰레드가 쓰레드 th1의 작업이 끝날때까지 기다림
} cath(InterruptedException e) {}
```

