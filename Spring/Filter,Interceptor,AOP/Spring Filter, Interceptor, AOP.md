# Spring Filter, Interceptor, AOP

- 참고
  - https://velog.io/@sa833591/Spring-Filter-Interceptor-AOP-%EC%B0%A8%EC%9D%B4-yvmv4k96
  - https://goddaehee.tistory.com/154

- 인증, 보안, 로깅, 인코딩 처리 등 애플리케이션 비지니스 로직외에 공통적으로 사용되는 기능을 따로 만들어 사용한다.
  - 로그인 관련(세션체크) 처리
  - 권한 체크
  - XSS(Cross Site Script) 방어
  - 로그
  - 페이지 인코딩

## Filter

- Dispatcher Servlet 영역(Spring 영역)에 들어가기 전, 후 처리에 대한 기능들을 적용한다.
  - Filter의 doFilter를 기준으로 전, 후 처리를 적용한다.
- 대표적으로 인코딩 변환 처리, XSS(Cross Site Script) 방어 처리
- Filter의 실행 메소드
  - init() : 필터 인스턴스 초기화
  - doFilter() : 실제 처리 로직
  - destory() : 필터 인스턴스 종료
- Spring Security 프로젝트는 필터를 이용하여 인증 처리를 한다.
  - Authentication Filter

## Interceptor

- Spring 영역 안에서 Controller가 실행 되기 전, 후 처리에 대한 기능들을 적용한다.
- Spring 영역 안에서 동작하므로, Spring Context 영역에 접근할 수 있다. => Spring Bean 객체에 접근 가능하다.
- 여러 개의 Interceptor 정의가 가능하다.
  - 로그인 체크, 권한 체크, 실행시간 계산 등의 기능을 처리한다.
- Interceptor의 실행 메소드
  - preHandler() : Controller 실행 전
  - postHandler() : Controller 실행 후, View Rendering 실행 전
  - afterCompletion() : View Rendering 후

## AOP

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