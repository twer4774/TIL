# Thread - daemonThread

- 일반 쓰레드의 작업을 돕는 보조적인 역할 수행
- 일바 쓰레드가 모두 종료되면 데몬 쓰레드는 강제적으로 자동 종료 됨
- 가비지 컬렉터, 워드프로세서의 자동저장, 화면자동갱신 등이 데몬 쓰레드
- 데몬쓰레드는 무한루프와 조건문을 이용해 실행 후 대기하고 있다가 특정 조건이 만족되면 작업을 수행하고 다시 대기하도록 작성 됨

```
boolean isDaemon() //쓰레드가 데몬 쓰레드인지 확인

void setDaemon(boolean on) //쓰레드를 데몬 쓰레드로 또는 사용자 쓰레드로 변경
```

### 데몬쓰레드 예제

```java
/**
 * 3초 마다 autoSave 값을 확인하여 자동저장하는 프로그램
 */
public class ThreadExDaemonThread implements Runnable{
    static boolean autoSave = false;

    public static void main(String[] args) {
        Thread t = new Thread(new ThreadExDaemonThread());
        t.setDaemon(true); //이 부분이 없으면 종료되지 않음
        t.start();

        for (int i = 1; i < 10; i++) {
            try{
                Thread.sleep(1000);
            } catch (InterruptedException e){

            }

            System.out.println(i);

            //5초가 지났으면 autoSave값을 true로 변경
            if(i==5){
                autoSave = true;
            }
        } //for
        System.out.println("프로그램을 종료합니다.");
    } //main

    public void run() {
        while(true){
            try{
                Thread.sleep(3 * 1000); //3초마다
            } catch(InterruptedException e){}

            //autoSave의 값이 true이면 autoSave()호출
            if(autoSave){
                autoSave();
            }
        }
    }

    public void autoSave(){
        System.out.println("작업이 자동저장되었습니다.");
    }
}
/*
1
2
3
4
5
작업이 자동저장되었습니다.
6
7
8
작업이 자동저장되었습니다.
9
프로그램을 종료합니다.
*/
```

