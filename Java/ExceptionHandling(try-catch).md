# Exception Handling(try-catch)

- Error의 종류

  - compile error : 컴파일시에 발생
  - runtime error : 실행시에 발생
  - logical error : 실행은 되지만 의도와 다르게 동작
    - ex) 창고의 재고에 음수가 표시됨. 게임에서 맞아도 피가 닳지 않음

- Runtime에 발생할 수 있는 오류를 error와 exception으로 구분

  - error : OutOfMemoryError(메모리 부족), StackOverflowError(스택오버플로우)
    - 발생하면 프로그램 코드에서 복구할 수 없는 심각한 오류
  - exception : 발생하더라도 프로그램코드에서 수습될 수 있는 비교적 덜 심각한 오류

  ### Exception

- RuntimeException : 주로 프로그래머의 실수에 의해 발생될 수 있는 예외들

  - ArithmeticException (산술연산예외)
  - ClassCastException
  - NullPointerException
  - IndexOutOfBoundsException
  - ...

- IOException

- ClassNotFoundException 등 종류가 다양

=> Runtime Exception과 아닌 것들 두 분류로 분리하여 기억할 것

## 예외 처리 (try - catch)

- 프로그램 실행 시 발생할 수 있는 예기치 모한 예외의 발생에 대비한 코드를 작성
- 예외의 발생으로 인한 비정상 종료를 막고 정상적인 실행상태를 유지할 수 있도록 하는 것

```java
try{
  //예외가 발생할 가능성이 있는 문장들
} catch (Exception1 e1){
  //Exception1이 발생할 경우 처리하기 위한 문장
}
```

```java
class ExceptionEx{
  public static void main(String args[]){
    int number = 100;
    int result = 0;
    
    for(int i=0; i<10; i++){
      try{
        result = number / (int)(Math.random() * 10);
        System.out.println(result);
      } catch (ArithmeticException e){
        System.out.println("0"); //0으로 나누면 ArithmeticException발생
      }
    }
  }
}
```

### printStackTrace()와 getMessage()

- 발생한 예외에 대한 정보
  - printStackTrace() : 예외발생 당시의 호출스택(Call Stack)에 있었던 메서드의 정보와 예외 메시지를 화면에 출력
    - 어떤 예외인지 ex)ArithmeticException / by zero 로 표시
  - getMessage() : 발생한 예외 클래스의 인스턴스에 저장된 메시지를 얻을 수 있음
    - by zero로 메시지만 출력됨

### 멀티 catch블럭

- |을 이용하여 하나의 catch블럭으로 합칠 수 있음
  - 단, 조상과 자손관계일 경우에는 컴파일에러가 발생하므로 사용하지 않음 - 조상과 자손관계라면 불필요한 코드를 제거하라는 의미에서 에러가 발생하는 것임

```java
try{
  ...
} catch (ExceptionA | ExceptionB e){
  e.printStackTrace();
}
```

### 예외 선언하기

- try-cath문 이외에 메서드에 선언하는 방법 throws
- 예외를 처리하는 것은 반드시 try-catch문 이용
  - 선언과 처리는 다른 것임을 기억할 것

```java
void method() throws Exception1, Exception2 ...{
  //메서드 내용
}
```

```java
class ExceptionEx1{
  public static void main(String[] args) throws Exception{
    method1(); //같은 클래스내의 static 멤버이므로 직접 호출가능
  }
  
  static void method1() throws Exception{
    try{
      throw new Exception();
    } catch (Exception e){
      System.out.println("method1메서드에서 예외가 처리되었습니다.");
      e.printStackTrace();
    }
  }
}

class ExceptionEx2{
  public static void.main(String[] args){
    try{
      method1();
    } catch (Exeption e){
      System.out.println("main메서드에서 예외가 처리되었습니다.");
      e.printStackTrace();
    }
  }
  
  static void method1() throws Exception{
    throw new Exception();
  }
}
```

- ExceptionEx2 처럼 예외를 처리하는 것이 좋음(둘다 써도 되긴함)
  - ExceptionEx1은 main메서드에서 예외가 발생한 것을 모르게 됨
  - ExceptionEx2는 method1()을 호출 할때 예외가 발생한것으로 간주되어 처리를 할 수 있게 됨

### Finally

- try-catch문과 함께 예외의 발생여부에 상관없이 실행되는 코드를 포함 시키는 블럭

```java
try{
  
} catch(Exception e){
  
} finally{
  
}
```

## 사용자정의 예외 만들기

- 프로그래머가 새로운 예외 클래스를 정의하여 사용할 수 있음
- 보통은 Exception클래스로부터 상속받는 클래스를 만듦

```java
class MyException extends Exception{
  Myexception(String msg){ //문자열을 매개변수로 받는 생성자
    super(msg); //조상인 Exception클래스의 생성자 호출
  }
}
```

