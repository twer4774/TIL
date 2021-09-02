# Spring AOP

- Aspect Oriented Programming. 관점 지향 프로그래밍
- 메소드 단위로 설정 가능하다.
  - Filter와 Interceptor와 달리 메소드 전후 지점에 자유롭게 설정 가능하다.
  - Filter와 Interceptor는 주소로 대상을 구분하지만, AOP는 주소, 파라미터, 어노테이션 등 다양한 방법으로 대상을 지정할 수 있다.
- OOP를 보완하기 위해 나온 개념
  - OOP를 활용할 때 중복을 줄일 수 없는 부분을 줄이기 위해 종단면에서 바라보고 처리하도록 설정한다.
- 대표적으로 로깅, 트랜잭션, 에러 처리에 사용된다.
- AOP의 Advice와 HandlerInterceptor의 차이
  - Advice는 파라미터로 JoinPoint나 ProceedingJoinPoint를 활용한다.
  - HandlerInterceptor는 Filter와 유사하게 HttpServletRequest, HttpServletResponse를 파라미터로 활용한다.
- 주요 어노테이션
  - @Aspect : AOP를 정의하는 클래스에 사용한다.
  - @Pointut : AOP를 적용시킬 지점을 설정한다.
  - @Before : 대상 메소드의 수행 전에 실행할 동작을 정의한다.
  - @After : 대상 메소드의 수행 후에 실해할 동작을 정의한다.
  - @Around : 대상 메소드의 수행 전,후 실행할 동작을 정의한다.
  - @After-returning : 대상 메소드의 **정상적인 수행 후** 실행할 동작을 정의한다.
  - @After-throwing : 예외 발생 후 실행할 동작을 정의한다.
- Controller 처리 이후 주로 비지니스 로직에서 실행된다.

## 프록시 패턴

- Spring AOP는 프록시 패턴을 이용한다.
  - 개방폐쇄 원칙과 의존역전 원칙을 따른다.
- 프록시 패턴의 장점 : 기존 코드를 변경하지 않고, 기능을 추가할 수 있다.

### 예제

```java
public interface IBrower{
  Html show();
}

public class Html {
  private Stirng url;
  public Html(String url){
    this.url = url;
  }
}

public class Browser implements IBrowser{
  private String url;
  public Browser(String url){
    this.url = url;
  }
  @Override
  public Html show(){
    System.out.println("browser loading html from : " + url);
		return new Html(url);
  }
}

//프록시 객체
public class BrowserProxy implements IBrowser{
  private String url;
  private Html html;
  
  public BrowserProxy(String url){
    this.url = url;
  }
  
  @Override
  public Html show(){
    if(html == null){
      this.html = new Html(url);
      System.out.println("BrowserProxy loading html from : " + url);
    }
    System.out.println("BrowserProxy use cache html : "+ url);
    return null;
  }
}

//Main
public static void main(String[] agrs){
  BrowserProxy browser = new Browser(Proxy("www.naver.com"));
  browser.show();
  browser.show();
  browser.show();
  browser.show();
  browser.show();
}

/*
결과
BrowserProxy loading html from :www.naver.com
BrowserProxy use cache html :www.naver.com
BrowserProxy use cache html :www.naver.com
BrowserProxy use cache html :www.naver.com
BrowserProxy use cache html :www.naver.com
BrowserProxy use cache html :www.naver.com
*/
```

## AOP 예제

### 목표 : Encoding 된 문자열을 AOP에서 Decoding 시킨다.

### 의존성

```
implementation 'org.springframework.boot:spring-boot-starter-aop'
```

### 커스텀 어노테이션 작성

```java
@Target({ElementType.TYPE, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
public @interface Decode {
}
```

### AOP 설정

```java
@Aspect
@Component
public class DecodeAop {


    //point cut : Aop를 적용하는 지점 설정 - 조건식은 인터넷에서 찾아야 한다.
    @Pointcut("execution(* walter.unit.aop.controller..*.*(..))")
    private void cut(){}

    @Pointcut("@annotation(walter.unit.aop.annotation.Decode)")
    private void enabledDecode(){}

    @Before("cut() && enabledDecode()")
    public void before(JoinPoint joinPoint) throws UnsupportedEncodingException {
        Object[] args = joinPoint.getArgs();

        for (Object arg : args){
            if(arg instanceof User){
                User user = User.class.cast(arg);
                String base64Name = user.getName();
                String name = new String(Base64.getDecoder().decode(base64Name), "UTF-8");

                user.setName(name);
            }
        }
    }

//아래의 주석은 Decode된 문자열을 다시 원래의 Encode로 Client에서 쓰일 때 이용된다.
  
//    @AfterReturning(value = "cut() && enabledDecode()", returning = "returnObj")
//    public void afterReturn(JoinPoint joinPoint, Object returnObj) {
//        if (returnObj instanceof User) {
//            User user = User.class.cast(returnObj);
//            String name = user.getName();
//            String base64Name = Base64.getEncoder().encodeToString(name.getBytes());
//
//            user.setName(base64Name);
//        }
//    }
}
```

### Controller

```java
@RestController
@RequestMapping("/api")
public class AopController {

    @Decode
    @PostMapping("/decode")
    public User decode(@RequestBody User user) {
        System.out.println("decode");
        System.out.println(user);
        return user;
    }
}
```

### 테스트

- Encoding 된 문자열 필요 : https://www.base64encode.org/
  - walter를 encode 시키면 d2FsdGVy가 나온다.

- http://localhost:8080/api/decode

  - body => {"name" : "d2FsdGVy", "age" : 12}

- 결과

  - {

    "name": "walter",

    "age": "12"

    }