# Spring Master - Intro

## 스프링 프레임워크

- 자바 기반 애플리케이션을 위한 포괄적인 프로그래밍 및 구성 모델 제공  => 프로그래머는 비즈니스 로직에 집중할 수 있음

### EJB 

- EJB란?
  - Enterprise Java Bean
  - 애플리케이션의 업무 로직을 가지고 있는 서버 애플리케이션
  - 주로 JSP는 화면처리, EJB는 업무 로직 처리
  - 서버를 관리하고 문제를 처리함으로써 효율성을 증대를 목적으로 사용
- EJB의 종류
  - Session Bean : DB 연동이 필요 없음
  - Entity Bean : 데이터베이스의 데이터를 관리하는 객체
  - Message-Driven Bean : JMS로 빈을 날려줌
- 장점
  - 정형화된 비즈니스 계층 제공
  - 선언적인 트랜잭션 관리 제공
  - 다양한 클라이언트에 대한 지원 가능
  - 분산기능 제공
  - 비즈니스 객체를 여러 서버에 분산시키는것이 가능
- 단점
  - 실행속도가 느림
    - 분산환경 지원을 위해 객체를 직렬화 하는 과정이 필요하기 때문에 느려짐
  - 개발과 배포가 번거로움
  - 단위테스팅 힘듦
    - EJB 컨테이너가 종속적이기 때문에 개발 후 EJB 컨텡이너에 배포한 다음 테스트 진행 필요
  - 복잡한 API
  - EJB 컨테이너에 종속적이기 때문에 이식성이 떨어짐

### 스프링 프레임워크

EJB가 지닌 단점들을 개선하여 스프링 프레임워크가 인기가 많아지게 되었습니다.

#### 단순화된 단위 테스팅

- 의존성 주입으로 단위 테스팅을 단순화 시켰습니다.
  - 단위테스트를 단순화 하면? => 생산성 향상. 결함이 일찍 발견됨. 지속적인 통합 빌드에서 자동화된 단위테스트 가능합니다.

#### 복잡한 코드 감소

- DB Connect, Exception, Transaction, Logging 등의 복잡한 코드를 줄였습니다.
- Prepared Statement와 스프링을 이용한 Query 실행 비교 예

```java
//Prepared Statement 이용
PreparedStatement st = null;
try{
  st = conn.prepareStatement(INSERT_TODO_QUERY);
  st.setString(1, bean.getDescription());
  st.setBoolean(2, bean.isDone());
  st.execute();
} catch (SQLException e){
  logger.error("Failed : " + INSERT_TODO_QUERY, e);
} finally {
  if (st ! = null){
    try {
      st.close();
    } catch (SQLException e){
      //Pass
    }
  }
}

//Spring 이용 => 매우 간단히 해결
jdbcTemplate.update(INSERT_TODO_QUERY, bean.getDescription(), bean.isDone());
```

- 스프링 프레임워크가 코드를 줄일 수 있는 원리

  - JDBC(Java Database Connectivity)는 checked 예외를 대부분 unchecked로 변환하여 컴파일 시점에서의 예외를 없앨 수 있습니다.

  - 중앙 집중식 AOP를 이용하여 예외를 관리합니다.

  - Checked, Unchecked 간단히 정리한 표

    | 구분          | Checked Exception                      | Unchecked Exception                         |
    | ------------- | -------------------------------------- | ------------------------------------------- |
    | 확인 시점     | 컴파일 시점                            | 런타임 시점                                 |
    | 처리 여부     | 반드시 예외처리 필요                   | 명시적으로 하지 않아도 됨                   |
    | 트랜잭션 처리 | 예외 발생 시 rollback 하지 않음        | 예외 발생시 rollback 필요                   |
    | 종류          | IOException, CalssNotFoundException 등 | NullPointerException, ClassCastException 등 |

#### 아키텍처의 유연성

- 스프링 프레임워크는 모듈식으로 독립적인 구성을 가지고 있습니다.
- 웹 데이터에서 스프링 MVC 프레임 워크를 제공합니다.
- Spring Beans로 비즈니스 로직을 위한 경량 구현체를 제공합니다.
- 데이터 레이어에서 JDBC 모듈을 이용하여 JPA, Hibernate등과 연결이 가능합니다.
- AOP활용으로 Logging, Transaction, Security를 구현할 수 있습니다.

## 스프링 모듈

![image-20210309150702627](/Users/wonik/Library/Application Support/typora-user-images/image-20210309150702627.png)

### 스프링 코어 컨테이너 : 의존성 주입, IoC 컨테이너 및 ApplicationContext 기능

| 모듈              | 사용                                                         |
| ----------------- | ------------------------------------------------------------ |
| spring-core       | 다른 스프링 모듈이 사용하는 유틸리티                         |
| spring-beans      | 스프링 빈 지원, 스프링 코어와 함께 DI 제공. BeanFactory 구현 포함 |
| spring-context    | BeanFactory를 상속하는 ApplicationContext 구현. 리소스 코드 및 국제화 지원 |
| spring-expression | EL(JSP에서 표현언어)을 확장하고 Bean 속성(배열 및 컬렉션 포함) 및 접근 처리를 위한 언어 제공 |

### 횡단 관심 : 로깅과 보안 레이어 적용

| 모듈              | 사용                                                         |
| ----------------- | ------------------------------------------------------------ |
| spring-aop        | 메소드 인터셉트와 포인트 컷을 사용해 관점 지향 프로그래밍의 지원 제공 |
| spring-aspects    | AOP 프레임 워크인 AspectJ와의 통합 제공                      |
| spring-instrument | 기본적인 instrument 제공                                     |
| spring-test       | 단위 통합 테스팅에 대한 기본 지원 제공                       |

- 메소드 인터셉트 : 특정 URI 요청시 controller로 가는 요청을 가로채는 역할을 합니다.
- 포인트 컷 : 특정 조건에 의해 필터링된 횡단관심을 위한 조인 포인트
  - 조인포인트 : 클라이언트가 호출하는 모든 비즈니스 메소드

### 웹 : 스프링 MVC 프레임워크 등 웹 프레임워크 제공

| 모듈          | 사용                                                         |
| ------------- | ------------------------------------------------------------ |
| spring-web    | 멀티파트 파일 업로드와 같은 기본 웹 기능 제공. 다른 웹 프레임워크와 통합 제공 |
| spring-webmvc | 모든 기능을 갖춘 웹 MVC 제공                                 |

### 비즈니스 : 일반적인 비즈니스로직인 POJO로 구현

### 데이터 : DB 또는 외부 인터페이스와 통신

| 모듈        | 사용                                                    |
| ----------- | ------------------------------------------------------- |
| srping-jdbc | JDBC 추상화. RDB, NoSQL등의 연결에 일관된 연결방법 제공 |
| spring-orm  | ORM 프레임워크 및 스펙과의 통합 제공                    |
| spring-oxm  | XML 매핑 통합객체 제공                                  |
| spring-jms  | JMS 추상화                                              |

## 스프링 프로젝트

- 스픙부트 : 마이크로 서비스 및 웹 어플리케이션 개발에 이용
  - 프레임워크의 선택, 호환되는 프레임워크의 버전 결정
  - 외부화 구성을 위한 매커니즘
  - 상태점검 및 모니터링
  - 배포
- 스프링 클라우드 : 클라우드용 어플리케이션 개발. 분산 시스템의 일반적인 패턴을 위한 솔루션 제공
  - 구성 관리
  - 서비스 디스커버리
  - 서킷 브레이커 : MSA에서 특정 MSA 서비스의 장해로 인해 다른 MSA의 서비스 장해를 방지하기 위한 기술
  - 지능형 라우팅패턴
- 스프링 데이터 : RDB와 NoSQL 액세스에 일관적인 방식 제공
  - 메소드 이름에 쿼리 지정 = > 레포지토리 및 객체 매핑에 대한 추상화 제공
    - ex) findById();
  - 간단한 스프링 이티그레이션
  - 스프링 MVC컨트롤러와의 통합
  - 고급 자동 감사기능 - 생성자, 생성일, 마지막 수정자, 마지막 수정일
- 스프링 배치 : 대용량 데이터 처리
  - 작업의 시작, 재시작, 중지
  - Chunk 단위 프로세싱
  - 단계 재시도 및 Skip 기능
  - 웹 기반 관리 인터페이스
- 스프링 시큐리티 : 인증 및 권한 부여
  - 간소화된 인증 및 권한 부여
  - 스프링 MVC와 서브릿 API와의 통합
  - 공통보안 공격방지(사이트 위조요청 (CSRF) 및 세션 고정)
  - SAML 및 LDAP와 통합할 수 있는 모듈
- 스프링 HATEOAS : 클라이언트로 부터 서버 분리
  - 다양한 링크를 제공하여 클라이언트와 서버를 분리합니다.
    - 기존 REST API의 단점을 보완한 것으로, 서버에서 엔드포인트 바뀌면 클라이언트에서 엔드포인트 요청 작업을 할 필요 없이 연관된 다양한 엔드포인트 링크를 제공하여 클라이언트와 서버를 분리합니다.
  - 링크가 깨지는 것을 줄이기 위해 서비스를 제공하는 링크 정의를 단순화
  - JAXB(xml기반) 및 JSON 통합 지원

## 스프링 프레임워크 5.0의 새로운 기능(2021.3 기준 현재 5.3버전)

- 4년만에 스프링 4에서 5로 버전업한 것 처럼 버전이 빠르게 올라가지는 않습니다.

### 새로운 기능

- BaseLine 업그레이드 : JDK8과 자바EE 7으로 최소버전을 업그레이드하였습니다. 이전 버전은 지원하지 않습니다.

  - 자바EE 7 스펙
    - Servlet 3.1
    - JMS 2.0
    - JPA 2.1
    - JAX-RS 2.0
    - BeanValidation 1.1

- 리액티브 프로그래밍 지원 : 이벤트에 반응하는 어플리케이션을 구현하는 데 초점을 맞춘 프로그래밍 스타일 제공

  - 리액티브 스트림 : 이랙티브 API를 정의하려는 언어 중립적 시도
  - 리액터 : 스프링 피보탈 팀이 제공하는 리액티브 스트림의 자바 구현
  - 스프링 웹 플러스 : 웹 어플리케이션 개발, 스프링 MVC와 비슷한 프로그래밍 모델 제공

- 함수형 웹 프레임워크 : 함수형 프로그래밍 스타일로 엔드포인트 제공

  ```java
  RouterFunction<String> route = route(GET("/hello"), request -> Response.ok().body(fromObject("hello")));
  ```

- Jigsaw(직소)를 사용한 자바모듈성

  - 자바8이 나오기 이전 까지 자바는 모듈식이 아니었습니다. 모듈식이 아니었던 자바는 아래의 문제점들을 겪게 되었고, 모듈화를 통해 외부에서 호출할 수 있는 API로 문제들을 해결해 나갔습니다.
    - 문제점
      - 플랫폼 무거움 : IoT, Node.js 등 경량플랫폼을 사용하면서 플랫폼이 무거워지는 것을 해결할 필요성을 느낌
      - JAR Hell 
        - 자바 클래스 로더가 클래스를 찾으면, 발견된 첫 번째 클래스가 로드되는 문제점이 존재했습니다.
        - 애플리케이션에 필요한 클래스가 여러 JAR에 있다면? => 특정 JAR를 로드하도록 지정하지 못했습니다.