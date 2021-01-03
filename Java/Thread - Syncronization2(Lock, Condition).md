# Thread - Syncronization2(Lock, Condition)

- synchorized블럭 외에 'java.util.concurrent.locks'패키지가 제공하는 lock클래스들을 이용하는 방법이 있음
- 같은 메서드 내에서만 lock을 걸 수 있는 제약을 벗어나기 위한 방법으로 사용됨
- lock클래스의 종류

```
ReentrantLock 재진입이 가능한 lock
ReentrantReadWriteLock 읽기에는 공유적이고, 쓰기에는 배타적인 lock
stampedLock ReetrantReadWriteLock에 낙관적인 lock의 기능 추가
```

```java
private ReentrantLock lock = new ReentrantLock(); //lock을 생성

//lock으로 condition 생성
private Condition forCook = lock.newCondition();
private Condition forCust = lock.newCondition();

//wiat(), notify() 대신 Condition의 await(), signal()을 사용
```

```java
import java.util.ArrayList;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class ThreadExReentrant {
    public static void main(String[] args) throws Exception{
        Table table = new Table();

        new Thread(new Cook(table), "COOK1").start();
        new Thread(new Customer(table, "donut"), "CUST1").start();
        new Thread(new Customer(table, "burger"), "CUST2").start();

        Thread.sleep(2000);
        System.exit(0);

    }

}

class Customer implements Runnable {
    private Table table;
    private String food;

    Customer(Table table, String food) {
        this.table = table;
        this.food = food;
    }

    public void run(){
        while(true){
            try{
                Thread.sleep(100);
            } catch (InterruptedException ex){

            }

            String name = Thread.currentThread().getName();
            table.remove(food);
            System.out.println(name + " ate a " + food);
        }//while
    }
}


class Cook implements Runnable {
    private Table table;

    Cook(Table table) { this.table = table; }

    public void run(){
        while(true){
            int idx = (int) (Math.random() * table.dishNum());
            table.add(table.dishNames[idx]);
            try{Thread.sleep(10);} catch (InterruptedException e) {}
        }//while
    }
}

class Table{
    String[] dishNames = { "donut", "donut", "burger"}; //donut의 확률을 높임
    final int MAX_FOOD = 6;
    private ArrayList<String> dishes = new ArrayList<>();

    private ReentrantLock lock = new ReentrantLock();
    private Condition forCook = lock.newCondition();
    private Condition forCust = lock.newCondition();

    public void add(String dish){
        lock.lock();

        try{
            while (dishes.size() >= MAX_FOOD) {
                String name = Thread.currentThread().getName();
                System.out.println(name+" is waiting.");

                try{
                    forCook.await(); //wait();
                    Thread.sleep(500);
                } catch (InterruptedException ex) {}
            }
            dishes.add(dish);
            forCust.signal(); //notify();
            System.out.println("Dishes:" + dishes.toString());
        } finally {
                lock.unlock();
        }
    } //add

    public void remove(String dishName){
        lock.lock();
        String name = Thread.currentThread().getName();

        try{
            while(dishes.size()==0){
                System.out.println(name + " is waiting.");
                try {
                    forCust.await();
                    Thread.sleep(500);
                } catch (InterruptedException e){}
            } //while

            while(true){
                for (int i = 0; i < dishes.size(); i++) {
                    if(dishName.equals(dishes.get(i))){
                        dishes.remove(i);
                        forCook.signal(); //잠자고 있는 COOK을 깨움
                        return;
                    }
                } //for

                try{
                    System.out.println(name+" is waiting.");
                    forCust.await();
                    Thread.sleep(500);
                } catch(InterruptedException e){}
            } //while
        } finally {
            lock.unlock();
        }
    } //remove

    public int dishNum() { return dishNames.length; }
}
```

