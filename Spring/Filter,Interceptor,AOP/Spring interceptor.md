# Spring interceptor

- Spring 영역 안에서 Controller가 실행 되기 전, 후 처리에 대한 기능들을 적용한다.
- Spring 영역 안에서 동작하므로, Spring Context 영역에 접근할 수 있다. => Spring Bean 객체에 접근 가능하다.
- 여러 개의 Interceptor 정의가 가능하다.
  - 로그인 체크, 권한 체크, 실행시간 계산 등의 기능을 처리한다.
- Interceptor의 실행 메소드
  - preHandler() : Controller 실행 전
  - postHandler() : Controller 실행 후, View Rendering 실행 전
  - afterCompletion() : View Rendering 후
- Filter와 Interceptor 차이 설명 
  - https://supawer0728.github.io/2018/04/04/spring-filter-interceptor/
  - https://www.leafcats.com/39 => 필터와 인터셉터를 이용한 로그인 로직
  - 가장 큰 차이 : httpRequest를 조작할 수 있는가, 예외처리 시점

## Reids Session과 Intercepter

목표 : Session에서 User를 확인하고, User 정보에 따라 권한을 체크한다.



## Spring Redis Session

### Docker를 이용하여 Reids 서버 구동

- 도커를 재시작했을 때, redis-cli에 다시 접속 : docker exec -it dockerRedis redis-cli

```
docker pull redis
docker network create redis-net

#dockerRedis라는 이름의 컨테이너를 redis-net 네트워크에 붙여 실행한다.
docker run --name dockerRedis -p 6379:6379 --network redis-net -d redis redis-server --appendonly yes

#redis-cli로 dockerRedis에 접속한다.
docker run -it --network redis-net --rm redis redis-cli -h dockerRedis
```

### SpringBoot

- 의존성 추가 	
  - implementation 'org.springframework.boot:spring-boot-starter-data-redis'
  - implementation 'org.springframework.session:spring-session-data-redis'

- redis 연결 설정

```yml
spring:
  redis:
    host: localhost
    password:
    port: 6379
    pool:
      max-idle: 8
      min-idle: 0
      max-active: 8
      max-wait: 1
  session:
    timout: 600
    store-type: redis
    redis:
      flush-mode: on-save
```

- RedisConfig : Redis 관련 설정

```java
@Configuration
public class RedisConfig {

    @Value("${spring.redis.host}")
    private String host;

    @Value("${spring.redis.port")
    private int port;

    @Bean
    public RedisConnectionFactory redisConnectionFactory(){
        RedisStandaloneConfiguration redisStandaloneConfiguration = new RedisStandaloneConfiguration();
        redisStandaloneConfiguration.setHostName(host);
        redisStandaloneConfiguration.setPort(port);
        LettuceConnectionFactory connectionFactory = new LettuceConnectionFactory(redisStandaloneConfiguration);
        return connectionFactory;
    }

    @Bean
    public StringRedisTemplate stringRedisTemplate(){
        StringRedisTemplate stringRedisTemplate = new StringRedisTemplate();
        stringRedisTemplate.setKeySerializer(new StringRedisSerializer());
        stringRedisTemplate.setValueSerializer(new StringRedisSerializer());
        stringRedisTemplate.setConnectionFactory(redisConnectionFactory());
        return stringRedisTemplate;
    }
}
```

- controller

```java
@RestController
public class RedisController {
    @GetMapping("/redis-session")
    public ResponseEntity redisSession(HttpSession httpSession){
        return ResponseEntity.ok().body("session : " + httpSession);
    }
}
```

- 테스트
  - 목표 : localhost:8080/redis-session 접속 후 dockerRedis에서 key값 확인
  - 터미널에서 redis-cli 접속 : docker exec -it dockerRedis redis-cli
    - [redis-cli] flushall : 모든 데이터 삭제
    - [browser] http://localhost:8080/redis-session 접속
    - [redis-cli] keys * : 모든 키 값 출력



## 커스텀 어노테이션과 Intercepter 구현 

목표 : 커스텀 어노테이션을 만들고, Interceptor에서 어노테이션 여부를 확인한다.

### 커스텀 어노테이션 생성

```java
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.TYPE, ElementType.METHOD})
public @interface Auth {

}
```

### Controller

```java
@Controller
public class InterceptorController {

    @Auth
    @GetMapping("/auth")
    public ResponseEntity auth(){
        return ResponseEntity.ok().body("auth 어노테이션 존재");
    }

    @GetMapping("/non-auth")
    public ResponseEntity nonAuth(){
        return ResponseEntity.ok().body("auth 어노테이션 없음");
    }
}
```

### Interceptor 구현

```java
@Slf4j
@Component
public class AuthInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        //어노테이션 체크 - Controller에 @Auth 어노테이션이 있는지 확인

        boolean hasAnnotation = checkAnnotation(handler, Auth.class);

        if(hasAnnotation){
            log.info("Auth 어노테이션 확인");
            return true;
        }

        log.info("Auth 어노테이션이 없다.");
        return false;
    }

    private boolean checkAnnotation(Object handler, Class<Auth> authClass) {
        //js. html 타입인 view 과련 파일들은 통과한다.(view 관련 요청 = ResourceHttpRequestHandler)
        if (handler instanceof ResourceHttpRequestHandler) {
            return true;
        }

        HandlerMethod handlerMethod = (HandlerMethod) handler;

        //Auth anntotation이 있는 경우
        if (null != handlerMethod.getMethodAnnotation(authClass) || null != handlerMethod.getBeanType().getAnnotation(authClass)) {
            return true;
        }

        //annotation이 없는 경우
        return false;
    }

}

```

### Interceptor 설정

```java
@RequiredArgsConstructor
@Configuration
public class InterceptorConfig implements WebMvcConfigurer {

    private final AuthInterceptor authInterceptor;

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(authInterceptor);
    }
}
```

### 테스트

- http://localhost:8080/auth로 접속하여 로그 확인

  ![image-20210827143921749](/Users/wonik/Library/Application Support/typora-user-images/image-20210827143921749.png)

- http://localhost:8080/non-auth로 접속하여 로그 확인

  ![image-20210827143936547](/Users/wonik/Library/Application Support/typora-user-images/image-20210827143936547.png)



## Interceptor에서 Session 정보로 유저권한 체크

### 모델 추가

- User

```java
@Getter
@NoArgsConstructor
@AllArgsConstructor
public class User {

    private String name;

    private int age;
}
```

- SessionMember : 세션 이용에서 직렬화/역직렬화를 위해 User의 Dto 역할을 하는 클래스를 따로 둔다.

```java
@Data
@NoArgsConstructor
@AllArgsConstructor
public class SessionMember implements Serializable {

    private String name;

    private int age;
}
```

### 커스텀 어노테이션 추가

```java
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.TYPE, ElementType.METHOD})
public @interface Auth {

}
```

### 인터셉터 추가

```java
@Slf4j
@Component
public class SessionAuthInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        //어노테이션 체크 - Controller에 @Auth 어노테이션이 있는지 확인

        boolean hasAnnotation = checkAnnotation(handler, Auth.class);

        if (hasAnnotation) {

            //어노테이션이 있으면서, User의 정보가 맞다면 true 반환
            //request에서 session 받아오기
            HttpSession session = request.getSession();
            SessionMember sessionMember = (SessionMember) session.getAttribute("sessionMember");//sessionMember객체로 저장된 객체 반환
            String userName = sessionMember.getName();
            Integer userAge = sessionMember.getAge();

            log.info("userName, userAge : {}, {}", userName, userAge);

            //User의 정보는 DB에서 불러오지만, 여기서는 간단히 하기 위해 임의의 값으로 확인
            // walter와 20이 세션정보에 있을 때 권한이 있는것으로 가정

            if (userName.equals("walter") && userAge.equals(20)) {
                return true;
            }

            throw new AuthException();
        }

        //Auth를 실패하더라도 Controller를 실행하기 위해서는 true로 설정해야한다. ex)/session/add의 경우 walter/20 이 아닌 다른 값이 들어가도 실행되어야 한다.
        return true;
    }


    private boolean checkAnnotation(Object handler, Class<Auth> authClass) {
        //js. html 타입인 view 과련 파일들은 통과한다.(view 관련 요청 = ResourceHttpRequestHandler)
        if (handler instanceof ResourceHttpRequestHandler) {
            return true;
        }

        HandlerMethod handlerMethod = (HandlerMethod) handler;

        //Auth anntotation이 있는 경우
        if (null != handlerMethod.getMethodAnnotation(authClass) || null != handlerMethod.getBeanType().getAnnotation(authClass)) {
            return true;
        }

        //annotation이 없는 경우
        return false;
    }

}
```

### 예외 처리 설정

- @RestControllerAdvice로 전역 예외처리 가능

```java
public class AuthException extends RuntimeException{

    public AuthException(){
        super(HttpStatus.UNAUTHORIZED.toString());
    }
}

@RestControllerAdvice
public class ExceptionAdviceHandler {

    @ResponseStatus(HttpStatus.UNAUTHORIZED)
    @ExceptionHandler(AuthException.class)
    public ResponseEntity authException(walter.unit.interceptor_reids_session.exception.AuthException e){
        return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("권한이 없습니다. " + e.getLocalizedMessage());
    }
}
```

### 인터셉터 설정

```java
@RequiredArgsConstructor
@Configuration
public class InterceptorConfig implements WebMvcConfigurer {

    private final SessionAuthInterceptor sessionAuthInterceptor;

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
			registry.addInterceptor(sessionAuthInterceptor).addPathPatterns("/session/*");
    }
}
```

### Controller

```java
@Slf4j
@Controller
public class SessionInterceptorController {

    @GetMapping("/session")
    public String index(){
        return "sessionAdd";
    }

    @PostMapping("/session/add")
    public ResponseEntity add(@RequestBody User user, HttpSession session){
        log.info("user: {}", user);
        SessionMember sessionMember = new SessionMember();
        sessionMember.setName(user.getName());
        sessionMember.setAge(user.getAge());

        session.setAttribute("sessionMember", sessionMember);

        return ResponseEntity.ok().body("session add");
    }

    @Auth
    @GetMapping("/session/auth")
    public String sessionAuth(HttpSession httpSession, Model model){
        model.addAttribute("userData", (SessionMember)httpSession.getAttribute("sessionMember"));
        return "sessionResult";
    }

    @GetMapping("/session/non-auth")
    public String sessionNonAuth(HttpSession httpSession) {
        return "sessionResult";
    }

    @GetMapping("/session/logout")
    public String logout(HttpSession httpSession){
        httpSession.invalidate();
        return "sessionAdd";
    }
}

```

### View

- Mustache 이용
- sessionAdd.mustache

```html
<html>

<head>
    <title> 세션 추가 페이지 </title>
</head>

<body>

<form>
    name : <input type="text" id="name">
    age : <input type="text" id="age">
    <input type="button" id="submitButton" value="추가">
</form>

</body>
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="/js/add.js"></script>
</html>
```

- sessionResult.mustache

```html
<html>

<head>
    <title> 세션 유저 정보 확인 페이지 </title>
</head>

<body>
{{#userData}}
    userName : {{name}} <br>
    userAge : {{age}}
{{/userData}}

<!-- userData가 없을 때 ex)/session/non-auth -->
{{^userData}}
    유저 정보가 없습니다.
{{/userData}}

</body>
</html>
```

- add.js

```js
var add = {

    init:function(){
             var _this = this;
    $('#submitButton').on('click', function(){
                _this.submit();
             });
    },

    submit:function(){
            var user = {
                 name : document.getElementById("name").value,
                 age : document.getElementById("age").value
            };

            $.ajax({
                  type: 'POST',
                  url: '/session/add',
                  dataType: 'text',
                  contentType:'application/json; charset=utf-8',
                  data: JSON.stringify(user),
                  success:function(data){
                       console.log("성공");
                       window.location.href="/session/auth";
                  },
                  error:function(e){
                    console.log("실패");
                    alert(e.status);
                  }

                });
            },
};

add.init();
```



### 테스트

- http://localhost:8080/session 에서 name, age 전송 => 로그인 로직을 단순화시켜 walter, 20을 넣으면 통과하도록 인터셉터 로직이 되어 있다.

  - [reids] flushall : 모든 데이터 지우기
  - [browser] name, age 폼 입력 후 추가

- http://localhost:8080/session/auth 접속 시

  - testuser / 10 => 예외 발생 => 로그 출력 및 화면 출력

  - walter / 20 => 성공 => 결과화면

- http://localhost:8080/session/logout 
  - redis에 key 출력 => 세션정보 삭제 확인
