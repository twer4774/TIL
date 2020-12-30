# Thread - threadGroup

- 보안상의 이유로 도이된 개념으로, 자신이 속한 쓰레드 그룹이나 하위 쓰레드 그룹은 변경할 수 있지만 다른 쓰레드 그룹의 쓰레드는 변경할 수 없음

| 메서드                                                       | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ThreadGroup(String name)                                     | 지정된 이름의 새로운 쓰레드 그룹 생성                        |
| ThreadGroup(ThreadGroup parent, String name)                 | 지정된 쓰레드 그룹에 포함되는 새로운 쓰레드 그룹을 생성      |
| int activeCount()                                            | 쓰레드 그룹에 포함된 활성상태에 있는 쓰레드의 수 반환        |
| int activeGroupCount()                                       | 쓰레드 그룹에 포함된 활성상태에 있는 쓰레드 그룹의 수 반환   |
| void checkAccess()                                           | 현재 실행중인 쓰레드가 쓰레드 그룹을 변경할 권한이 있는지 체크. 권한이 없다면 SecurityException 발생 |
| int enumerate(Thread[] list)<br />int enumerate(Thread[] list, boolean recurse)<br />int enumerate(ThreadGroup[] list)<br />int enumerate(ThreadGroup[] list, boolean recurse) | 쓰레드 그룹에 속한 쓰레드 또는 하위 쓰레드 그룹의 목록을 지정된 배열에 담고 그 개수를 반환<br />recusre 속성이 true이면 하위 쓰레드 그룹까지 배열에 담음 |
| int getMaxPriority()                                         |                                                              |
| String getName()                                             |                                                              |
| ThreadGroup getParent()                                      |                                                              |
| boolean isDaemon()                                           | 쓰레드 그룹이 데몬 쓰레드그룹인지 확인                       |
| boolean isDestoryed()                                        | 쓰레드 그룹이 삭제되었는지 확인                              |
| void list()                                                  | 쓰레드 그룹에 속한 쓰레드와 하위 쓰레드 그룹에 대한 정보 출력 |
| boolean parentOf(ThreadGroup g)                              | 지정된 ㅆ레드 그룹의 상위 쓰레드 그룹인지 확인               |
| void setDaemon(boolean daemon)                               | 쓰레드 그룹을 데몬 쓰레드 그룹으로 설정/해제                 |
| void setMaxPriority(int pri)                                 | 쓰레드 그룹의 최대 우선순위 설정                             |

### 쓰레드 그룹 예제

```java
public class ThreadExThreadGroup {
    public static void main(String[] args) {
        ThreadGroup main = Thread.currentThread().getThreadGroup();
        ThreadGroup grp1 = new ThreadGroup("Group1");
        ThreadGroup grp2 = new ThreadGroup("Group2");
        
        //ThreadGroup(ThreadGroup parent, String name)
        ThreadGroup subGrp1 = new ThreadGroup(grp1, "SubGroup1");
        
        grp1.setMaxPriority(3); //grp1의 최대 우선순위를 3으로 변경
        
        Runnable r = new Runnable(){
            public void run(){
                try{
                    //쓰레드 그룹의 정보를 출력하기 전에 쓰레드가 종료되는 것을 막기 위해 sleep 추가
                    Thread.sleep(1000); //쓰레드를 1초간 멈추게 함
                } catch(InterruptedException e){
                    
                }
            }
        }; //Runnable()
        
        //Thread(ThreadGroup tg, Runnable r, String name)
        new Thread(grp1, r, "th1").start();
        new Thread(subGrp1, r, "th2").start();
        new Thread(grp2, r, "th3").start();

        System.out.println(">>List of ThreadGroup : " + main.getName() + ", Active ThreadGroup: " + main.activeGroupCount()
        +", Active Thread: " + main.activeCount()
        );
        
        main.list();
    }
}

/*
>>List of ThreadGroup : main, Active ThreadGroup: 3, Active Thread: 4
java.lang.ThreadGroup[name=main,maxpri=10]
    Thread[main,5,main]
    java.lang.ThreadGroup[name=Group1,maxpri=3]
        Thread[th1,3,Group1]
        java.lang.ThreadGroup[name=SubGroup1,maxpri=3]
            Thread[th2,3,SubGroup1]
    java.lang.ThreadGroup[name=Group2,maxpri=10]
        Thread[th3,5,Group2]
*/
```

