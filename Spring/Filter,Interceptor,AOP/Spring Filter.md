# Spring Filter

- Dispatcher Servlet 영역(Spring 영역)에 들어가기 전, 후 처리에 대한 기능들을 적용한다.
  - Filter의 doFilter를 기준으로 전, 후 처리를 적용한다.
- 대표적으로 인코딩 변환 처리, XSS(Cross Site Script) 방어 처리
- Filter의 실행 메소드
  - init() : 필터 인스턴스 초기화
  - doFilter() : 실제 처리 로직
  - destory() : 필터 인스턴스 종료
- Spring Security 프로젝트는 필터를 이용하여 인증 처리를 한다.
  - Authentication Filter

## 필터의 실행 과정

### HttpServletRequest, HttpServletResponse

- Servlet을 실행하게 되면 요청과 응답이 ServletRequest, ServletResponse로 이루어 진다.
- 웹 애플리케이션은 HTTP 프로토콜을 따르기 때문에 ServletRequest, ServletResponse를 HTTP 프로토콜로 응답할 수 있도록 랩핑해주면 더 편리하게 사용할 수 있다.
  - ContentCachingRequestWrapper, ContentCachingResponseWrapper로 래핑하는 이유
    - https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/util/ContentCachingRequestWrapper.html
    - Filter에서 Http 프로토콜을 이용한 정보를 사용하기 위해서는 캐시 처리가 필요하다.
    - HttpServletRequest, HttpServlertResponse의 inputStream, reader를 캐시하여 해당 정보를 여러 번 이용할 수 있게 한다.
      - Http 프로토콜은 무상태, 비연결성임을 생각하자

### doFilter

- Filter의 전, 후 처리 과정의 기준이 되는 메소드
- filter에 어떠한 요청과 응답을 사용할 지 정한다.

## 실습

### 객체 정의

```java
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class User {

    private String name;
    private int age;
}
```

### filter 정의

```java
@Slf4j
@WebFilter(urlPatterns = "/api/filter") //필터를 적용할 uri를 설정한다.
public class SampleFilter implements Filter {

    //필터의 핵심. request와 response를 이용하여 요청과 응답을 처리한다.
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {

        //전처리 과정 - HttpServletRequest와 HttpServletResponse를 캐시 가능하도록 래핑해준다.
        ContentCachingRequestWrapper httpServletRequest = new ContentCachingRequestWrapper((HttpServletRequest) request);
        ContentCachingResponseWrapper httpServletResponse = new ContentCachingResponseWrapper((HttpServletResponse) response);


        //전, 후 처리의 기준이되는 메소드
        //filter의 동작에 httpServletRequest, httpServletResponse를 이용한다.
        chain.doFilter(httpServletRequest, httpServletResponse);


        //후 처리 과정

        //request 요청으로 어떤 uri가 들어왔는지 확인
        String uri = httpServletRequest.getRequestURI();

        //request 내용 확인
        String reqContent = new String(httpServletRequest.getContentAsByteArray());
        log.info("uri : {}, request : {}", uri, reqContent);


        // response 내용 상태 정보, 내용 확인
        int httpStatus = httpServletResponse.getStatus();
        String resContent = new String(httpServletResponse.getContentAsByteArray());

        //주의 : response를 클라이언트에서 볼 수 있도록 하려면 response를 복사해야 한다. response를 콘솔에 보여주면 내용이 사라진다.
        httpServletResponse.copyBodyToResponse();

        log.info("status: {}, response {}", httpStatus, resContent);
    }

}
```

### controller

```java
@Slf4j
@RestController
public class FilterController {

    //Filter가 적용되지 않는 uri
    @PostMapping("/api/non-filter")
    public String nonFilter(@RequestBody User user){
        log.info("user : {}", user);

        return "non-filter";
    }

    //Filter가 적용되는 uri
    @PostMapping("/api/filter")
    public String usingFilter(@RequestBody User user){
        log.info("user : {}", user);

        return "filter";
    }

}
```

### main

```java
@ServletComponentScan
@SpringBootApplication
public class FilterApplication {

    public static void main(String[] args) {
        SpringApplication.run(FilterApplication.class, args);
    }
}
```

### 테스트

- body

  ```json
  {
    "name" : "walter",
    "age" : 10
  }
  ```

- http://localhost:8080/api/non-filter 로 post 메소드를 이용하여 body의 값을 넣고 보낸다.
- http://localhost:8080/api/filter 로 post 메소드를 이용하여 body의 값을 넣고 보낸다.

- 결과
  - http://localhost:8080/api/non-filter 는 필터를 거치지 않는다.
  - http://localhost:8080/api/filter 는 필터를 거쳐 아래와 같이 로그가 콘솔에 출력된다.

```
2021-08-09 11:53:40.498  INFO 9435 --- [nio-8080-exec-1] walter.unit.filter.filter.SampleFilter   : uri : /api/filter, request : {
  "name" : "walter",
  "age" : 10
}
2021-08-09 11:53:40.502  INFO 9435 --- [nio-8080-exec-1] walter.unit.filter.filter.SampleFilter   : status: 200, response filter
```

## Spring Security에서의 Filter

- Spring Security에서 인증을 위한 가장 먼저 진행되는 부분이 Filter Chain을 거치는 부분이다.
- Http Request로 요청이 들어오면 Filter를 거쳐서 인증부분을 확인한다.
- 스프링 시큐리티 아키텍처 구조는 아래 url에서 확인 가능하다.
  - https://twer.tistory.com/entry/Security-%EC%8A%A4%ED%94%84%EB%A7%81-%EC%8B%9C%ED%81%90%EB%A6%AC%ED%8B%B0%EC%9D%98-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98%EA%B5%AC%EC%A1%B0-%EB%B0%8F-%ED%9D%90%EB%A6%84?category=470655

### Spring Security의 Filter 부분

- 의존성 : implementation 'org.springframework.boot:spring-boot-starter-security'

- Spring Security를 적용하려고 하면 Config 설정이 필요한데, 이때 WebSecurityConfigurerAdapter의 cofnigure를 재정의하여 사용하면 편하다.

  ```java
  @Configuration
  public class SecurityConfig extends WebSecurityConfigurerAdapter {
  
      @Override
      protected void configure(HttpSecurity http) throws Exception {
          
      }
  }
  ```

- configure 메소드의 HttpSecurity 파라미터를 내부적으로 보면

  - DefaultSecurityFilterChain과 SecurityBuilder\<DefaultSecurityFilterChain>를 이용하여 Filter가 동작하고 있음을 짐작할 수 있다.

```java
public final class HttpSecurity extends AbstractConfiguredSecurityBuilder<DefaultSecurityFilterChain, HttpSecurity>
		implements SecurityBuilder<DefaultSecurityFilterChain>, HttpSecurityBuilder<HttpSecurity> {

	private final RequestMatcherConfigurer requestMatcherConfigurer;

	private List<OrderedFilter> filters = new ArrayList<>();
 ...
}
```

