# Lamda Expression(람다식)

- 자바를 객체지향 언어이자 함수형 언어로 만들어 줌

- 람다식

  - 메서드를 하나의 식으로 표현하여 간략하면서도 명확한 식으로 표현
  - 메서드를 람다식으로 표현하면 메서드의 이름과 반환값이 없어지므로, 람다식을 익명함수(anonymous function)이라고도 함

  ```java
  int[] arr = new int[5];
  Arrays.setAll(arr, (i) -> (int)(Math.random()*5)+1);
  ```

## 람다식 작성

- 메서드에서 이름과 반환타입을 제거하고 매개변수 선언부와 몸통 사이({})에 ->를 추가

```java
(매개변수 선언){
	문장  
}

(int a, int b) -> {
  return a > b ? a : b;
}

//식의 연산결과가 자동 반환 되므로 return 생략 가능
(int a, int b) -> a > b ? a : b

//타입 추론이 가능하므로 타입 생략 가능
(a, b) -> a > b ? a : b
```

## 함수형 인터페이스(Functional Interface)

```java
interface MyFunction {
  public abstract int max(int a, int b);
}

MyFunction f = new MyFunction() {
  public int max(int a, int b){
    return a > ? a : b;
  };
}
int big = f.max(5, 3); //익명 객체의 메서드 호출
```

### 함수형 인터페이스 타입의 매개변수와 반환타입

```java
@FunctionalInterface
interface MyFunction{
  void myMethod(); //추상 메서드
}
```

- 메서드의 매개변수가 MyFunction타입이면 이 메서드를 호출할 때 람다식을 참조하는 참조변수를 매개변수로 지정해야 함

```java
void aMethod(MyFunction f){ //매개변수의 타입이 함수형 인터페이스
  f.myMethod(); //MyFunction에 정의된 메서드 호출
}
...
MyFunction f = () -> System.out.println("myMethod()");
aMethod(f);

//또는 참조변수 없이 아래와 같이 직접 람다식을 매개변수로 지정하는 것도 가능
aMethod(() -> System.out.println("myMethod()"); //람다식을 매개변수로 지
```

```java
@FunctionalInterface
interface MyFunction{
    void run(); //public abstract void run();
}

public class LambdaEx {
    static void execute(MyFunction f) { //매개변수의 타입이 MyFunction인 메서드
        f.run();
    }

    static MyFunction getMyFunction(){ //반환 타입이 MyFunction인 메서드
        MyFunction f = () -> System.out.println("f3.run()");
        return f;
    }

    public static void main(String[] args) {
        //람다식으로 MyFunction의 run()구현
        MyFunction f1 = () -> System.out.println("f1.run()");

        MyFunction f2 = new MyFunction() { //익명 클래스로 run() 구현
            @Override
            public void run() {
                System.out.println("f2.run()");
            }
        };

        MyFunction f3 = getMyFunction();

        f1.run();
        f2.run();
        f3.run();

        execute(f1); //매개변수로 이용
        execute(() -> System.out.println("run()"));
    }
}
/*
f1.run()
f2.run()
f3.run()
f1.run()
run()
*/
```

## java.util.function패키지

- 일반적으로 자주 쓰이는 형식의 메서드를 함수형 인터페이스로 미리 정의해 놓음

| 함수형 인터페이스  | 메서드            | 설명                                                         |
| ------------------ | ----------------- | ------------------------------------------------------------ |
| java.lang.Runnable | void run()        | 매개변수도 없고, 반환값도 없음                               |
| Supplier<T>        | T get()           | 매개변수는 없고, 반환값만 있음                               |
| Consumer<T>        | void accept(T t)  | Supplier와 반대로 매개변수만 있고, 반환값이 없음             |
| Function<T, R>     | R apply(T t)      | 일반적인 함수, 하나의 매개변수를 받아서 결과 반환            |
| Predicate<T>       | boolean test(T t) | 조건식을 표현하는데 사용. 매개변수는 하나, 반환 타입은 boolean |

### 조건식의 표현에 사용되는 Predicate

- boolean으로 반환

```java
Predicate<String> isEmptyStr = s -> s.length()==0;
String s = "";

if(isEmptyStr.test(S))
  System.out.println("This is an empty String.");
```

### 매개변수가 두 개인 함수형 인터페이스

- 접두사에 'Bi'가 붙음

| 함수형 인터페이스 | 메서드                 | 설명                                                      |
| ----------------- | ---------------------- | --------------------------------------------------------- |
| BiConsumer<T,U>   | void accept(T t, U u)  | 두개의 매개변수만 있고, 반환값이 없음                     |
| BiPredicate<T,U>  | boolean test(T t, U u) | 조건식을 표현하는데 사용. 매개변수는 둘, 반환값음 boolean |
| BiFunction<T,U,R> | R apply(T t, U u)      | 두 개의 매개변수를 받아서 하나의 결과를 반환              |

### 컬렉션 프레임워크와 함수형 인터페이스

| 인터페이스 | 메서드                                         | 설명                             |
| ---------- | ---------------------------------------------- | -------------------------------- |
| Collection | boolean removeIf(Predicate<E> filter)          | 조건에 맞는 요소 삭제            |
| List       | void replaceAll(UnaryOperator<E> operator)     | 모든 요소를 변환하여 대체        |
| Iterable   | void forEach(Consumer<T> action)               | 모든 요소에 작업 action을 수행   |
| Map        | V compute(K key, BiFunction<K,V,V> f)          | 지정된 키의 값에 작업 f 수행     |
|            | V computeIfAbsent(K key, Function<K,V> f)      | 키가 없으면, 작업 f 수행 후 추가 |
|            | V computeIfPresent(K key, BiFunction<K,V,V> f) | 지정된 키가 있을 때, 작업 f 수행 |
|            | V merge(K key, V value, BiFunction<V,V,V> f)   | 모든 요소에 병합작업 f수행       |
|            | void forEach(BiConsumer<K,V> action)           | 모든 요소에 작업 action을 수행   |
|            | void replaceAll(BiFunction<K,V,V> f)           | 모든 요소에 치환작업 f 수행      |

```java
import java.util.*;

class LambdaEx{
  pubic static void main(String[] args) {
    ArrayList<Integer> list = new ArrayList<>();
    for(int i=0; i<10; i++){
      list.add(i);
    }
      
    //list의 모든 요소 출력
    list.forEach(i->System.out.print(i+","));
    System.out.println();

    //list에서 2또는 3의 배수 제거
    list.removeIf(x-> x%2==0 || x%3==0);
    System.out.println(list);

    list.replaceAll(i->i*10); //list의 모든 요소에 *10
    System.out.println(list);

    Map<String, String> map = new HashMap<>();
    map.put("1", "1");
    map.put("2", "2");
    map.put("3", "3");
    map.put("4", "4");

    //map의 모든 요소를 {k,v}의 형식으로 출력
    map.forEach((k,v) -> System.out.print("{"+k+","+v+"},"));
    System.out.println();
  }
}
/*
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
[1, 5, 7]
[10, 50, 70]
{1,1}, {2,2}, {3,3}, {4,4},
*/
```

## 메서드 참조

```java
Function<String, Integer> f = (String s) -> Integer.parseInt(s);
```

### 생성자의 메서드 참조

```java
Supplier<MyClass> s = () -> new MyClass(); //람다식
Supplier<MyClass> s = MyClass::new; //메서드 참조
```

