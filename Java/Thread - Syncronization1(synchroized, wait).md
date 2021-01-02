# Thread - Syncronization1(synchroized, wait)

- 여러 쓰레드가 같은 프로세스 내의 자원을 공유하면 작업에 영향을 주기 때문에 동기화 필요
- 한 쓰레드가 특정 작업을 마치기 전까지 다른 쓰레드에 의해 영향을 받지 않도록 하는 것이 필요
  - 임계 영역(critical section) : 공유 데이터를 사용하는 코드 영역을 임계 영역으로 지정
  - 잠금(lock) : 공유 데이터(객체)가 가지고 있는 lock을 획득한 단 하나의 쓰레드만 이 영역 내의 코드를 수행할 수 있게 함

- synchronized를 이용한 동기화와 locks, atomic을 통한 동기화 구현 방법이 있음

## synchronized를 이용한 동기화

- synchronized 키워드를 이용하여 임계 영역 설정
  - 임계영역을 설정하면 lock을 자동으로 획득과 반납을 함

```java
//1. 메서드 전체를 임계 영역으로 지정
public synchronized void calcSum(){
  ...
}

//2. 특정 영역을 임계 영역으로 지정
synchronized(객체의 참조변수){
  ...
}
```

- 모든 객체는 lock을 하나씩 가지고 있으며, 해당 객체의 lock을 가지고 있는 쓰레드만 임꼐 영역의 코드를 수행할 수 있음
- 다른 쓰레드 들은 lock을 얻을 때까지 기다리게 됨
- 효율적은 프로그램을 위해 일부에서만 synchronized하는 것이 좋음(임계 영역을 최소화)

```java
public class ThreadExCriticalSecion {

    public static void main(String[] args) {
        Runnable r = new RunnableExCriticalSection();

        new Thread(r).start();
        new Thread(r).start();
    }


}

class Account {
    private int balance = 1000;

    public int getBalance(){
        return balance;
    }

    //synchronized를 넣어야 두 쓰레드 간의 임계 영역이 생성되어 -가 찍히는 것을 방지 할 수 있음
    public synchronized void  withdraw(int money){

            if (balance >= money) {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                }
                balance -= money;
            }

    } //withdraw
}

class RunnableExCriticalSection implements Runnable {
    Account acc = new Account();

    public void run() {
        while(acc.getBalance() > 0){
            //100, 200, 300 중의 한 값음 임의로 선택해서 출금
            int money = (int)(Math.random() * 3 + 1) * 100;
            acc.withdraw(money);
            System.out.println("balance:" + acc.getBalance());
        }
    }
}
/*
balance:700
balance:500
balance:200
balance:0
balance:0
*/
```

## wait()과 notify()

- 특정 쓰레드가 객체의 락을 가진 상태로 오랜 시간 보내지 않도록 하는 것도 중요
- 다른 쓰레드들의 작업의 원활을 보장하기 위해 wait()와 notify() 필요
  - wait(): 임계 영역의 코드를 수행하다가 더 이상 진행할 상황이 아니면  wait()를 호출하여 쓰레드가 락을 반납하고 기다림
  - notify(): 나중에 작업을 진행할 수 있는 상황이 되면 notify()를 호출하여 중단했던 쓰데르가 다시 락을 얻어 작업을 진행

```
wait(), notify(), notifyAll()
- Object에 정의
- 동기화 블록내에서만 사용할 수 있음
- 보다 효율적인 동기화를 가능하게 함
```

### 식당에서의 wait(), notify()

- 식당에서 음식(Dish)을 만들어서 Table에 추가(add)하는 요리사(Cook)와 테이블의 음식 소비(remove)하는 손님(Customer)을 쓰레드로 구현 => 요리사와 손님을 쓰레드로 구현
- Table의 add와 remove에 synchronized 추가
- wait()를 이용하여 테이블 객체의 lock을 풀었다가 손님이 원하는 음식이 추가되면 notify()로 다시 lock을 얻어 나머지 작업 수행

```java
import java.util.ArrayList;

public class ThreadWait {
    public static void main(String[] args) throws Exception{
        Table table = new Table(); //여러 쓰레드가 공유하는 객체

        new Thread(new Cook(table), "COOK1").start();
        new Thread(new Customer(table, "donut"), "CUST1").start();
        new Thread(new Customer(table, "burger"), "CUST2").start();

        Thread.sleep(100); //0.1초 후에 강제종료
        System.exit(0);

    }

}

class Table {
    String[] dishNames = {"donut", "donut", "burger"}; //donut이 더 자주 나옴
    final int MAX_FOOD = 6; //테이블에 놓을 수 있는 최대 음식의 개수

    private ArrayList<String> dishes = new ArrayList<>();

    public synchronized void add(String dish){
        while(dishes.size() >= MAX_FOOD){
            String name = Thread.currentThread().getName();
            System.out.println(name + " is waiting.");
            
            try{
                wait(); //COOK쓰레드를 기다리게 함
                Thread.sleep(500);
            } catch (InterruptedException e){}
        }
        
        dishes.add(dish);
        notify(); //기다리고 있는 CUST를 깨움
        System.out.println("Dishes:" + dishes.toString());
    }

    public void remove(String dishName){
        synchronized (this) {
            
            String name = Thread.currentThread().getName();
            
            while(dishes.size()==0){
                System.out.println(name+ " is waiting.");
                try{
                    wait(); //CUST쓰레드를 기다리게 함
                    Thread.sleep(500);
                } catch (InterruptedException e) {}
            }
            
            while(true){
                for (int i = 0; i < dishes.size(); i++) {
                    if (dishName.equals(dishes.get(i))) {
                        dishes.remove(i);
                        notify(); //잠자고 있는 COOK을 깨움
                        return;
                    }
                } //for
                
                try{
                    System.out.println(name +" is waiting.");
                    wait(); //원하는 음식이 없는 CUST쓰레드를 기다리게 ㅏㅎㅁ
                    Thread.sleep(500);
                } catch(InterruptedException e) {}
            } //while(true)
            
        } //synchronized
    }
    public int dishNum() { return dishNames.length; }
}


//음식을 테이블에서 제거하는 Customer(손님)
class Customer implements Runnable {

    private Table table;
    private String food;

    Customer(Table table, String food){
        this.table = table;
        this.food = food;
    }

    public void run() {
     while(true){
         try{ Thread.sleep(100); } catch (InterruptedException e) { }
         String name = Thread.currentThread().getName();

         table.remove(food);
         System.out.println(name + " ate a " + food);
     }//while
    }
    boolean eatFood() { return table.remove(food); }
}


//음식을 테이블에 추가하는 Cook(요리사)
class Cook implements Runnable {

    private Table table;

    Cook(Table table) {
        this.table = table;
    }

    public void run() {
        while(true){
            //임의의 요리를 하나 선택해서 table에 추가
            int idx = (int)(Math.random()*table.dishNum());
            table.add(table.dishNames[idx]);

            try{
                Thread.sleep(10);
            } catch (InterruptedException e){

            }
        }
    }
}
```

