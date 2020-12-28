# Thread - priority

- 쓰레드가 가지고 있는 속성
  - 우선순위의 값에 따라 쓰레드가 얻는 실행시간이 달라짐
  - 작업의 중요도에 따라 쓰레드의 우선순위를 서로 다르게 지정하여 특정 쓰레드가 더 많은 작업시간을 갖도록 할 수 있음
- 숫자가 높을수록 더 높은 우선순위

```java
void setPriority(int newPriority) //쓰레드의 우선순위를 지정한 값으로 변경
int getPriority() //쓰레드의 우선순위 반환
  
public static final int MAX_PRIORITY = 10 //최대 우선순위
public static final int MIN_PRIORITY = 1 //최소 우선순위
public static final int NORM_PRIORITY = 5 //보통 우선순위
```

### 쓰레드 우선순위 지정

```java
package JavaStandard;

public class ThreadExPriority {
    public static void main(String[] args) {
        ThreadExPriority_1 th1 = new ThreadExPriority_1();
        ThreadExPriority_2 th2 = new ThreadExPriority_2();

        th2.setPriority(7);

        System.out.println("Priority of th2(-) : " + th1.getPriority());
        System.out.println("Priority of th2(|) : " + th2.getPriority());

        th1.start();
        th2.start();
    }

}

class ThreadExPriority_1 extends Thread{
    public void run(){
        for (int i = 0; i < 300; i++) {
            System.out.print("-");
          //우선순위가 높아지면 한 번에 작업이 끝날 수 있기 때문에 아무일도 하지 않는 반복작업을 추가함
            for (int x = 0; x < 10000000; x++) {

            }
        }
    }
}

class ThreadExPriority_2 extends Thread{
    public void run(){
        for (int i = 0; i < 300; i++) {
            System.out.print("|");
          //우선순위가 높아지면 한 번에 작업이 끝날 수 있기 때문에 아무일도 하지 않는 반복작업을 추가함
            for (int x = 0; x < 10000000; x++) {

            }
        }
    }
}

/*
Priority of th2(-) : 5
Priority of th2(|) : 7
-||-|||||||||||||||------- ... --- //th2의 작업이 먼저 종료됨(우선순위가 높은게 먼저 종료됨)
*/
```

