# JAVA-Thread

- 구현방법에는 2가지 존재

- Thread클래스를 상속받는 방법

  - ```java
    class MyThread extends Thread{
      public void run() {
        //작업내용
      }
    }
    ```

- Runnable인터페이스를 구현하는 방법

  - Runnable인터페이스는 run()만 정의되어 있는 간단한 인터페이스.

  - ```java
    public interface Runnable {
      public abstract void run();
    }
    ```

  ```java
  class MyThread implements Runnable{
    public void run() {
      //작업내용
    }
  }
  ```

### Single Thread && Multi Thread

- Single Thread

- ```java
  /** 하나의 쓰레드로 작업을 처리할 경우 **/
  package Thread;
  public class ThreadEx4 {
      public static void main(String[] args) {
          long startTime = System.currentTimeMillis();
  
          for (int i = 0; i < 300; i++) {
              System.out.printf("%s", new String("-"));
          }//for
  
          System.out.print("소요시간1: " + (System.currentTimeMillis() - startTime));
  
          for (int i = 0; i < 300; i++) {
              System.out.printf("%s", new String("|"));
          }//for
  
          System.out.printf("소요시간2: " + (System.currentTimeMillis() - startTime));
      }//main
  }
  
  //결과
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------소요시간1: 71||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||소요시간2: 92
  
  ```

- MultiThread

```java
/** 두개의 쓰레드로 작업을 나눠서 처리할 경우 **/
package Thread;

public class ThreadEx5 {
    static long startTime = 0;

    public static void main(String[] args) {
        ThreadEx5_1 th1 = new ThreadEx5_1();
        th1.start();
        startTime = System.currentTimeMillis();

        for (int i = 0; i < 300; i++) {
            System.out.printf("%s", new String("-"));
        }//for

        System.out.print("소요시간1:" + (System.currentTimeMillis() - ThreadEx5.startTime));
    }//main
}

class ThreadEx5_1 extends Thread {
    public void run() {
        for (int i = 0; i < 300; i++) {
            System.out.printf("%s", new String("|"));
        }//for

        System.out.print("소요시간" + (System.currentTimeMillis() - ThreadEx5.startTime));
    }//run
}

//결과
||------------------------------------------------------------------------------------------------------------------------------------------------------------------------------||||||||||||||||||||||||||||||||||||||||||||||||||||||||||------------------------||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||---------------||||||||||||||||||||||||||||||-|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||--------------------|||||||||||||||||||||소요시간70------------------------------------------------------------------소요시간1:74

```

