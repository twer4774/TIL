# SpringBoot Redis 연동 - Simple, Session

## Redis

- MSA 방식으로 세션을 관리하여 인증서버를 구축하거나 cache 서버로 활용할 수 있다.

### redis-cli

- redis-server와 통신하기 위해 기본 제공되는 명령

### docker로 redis 설치하기

- docker network create : 다른 컨테이너와의 통신을 위한 네트워크 환경만들기
  - docker network inspect로 정보확인 가능

```
docker pull redis
docker network create redis-net

#dockerRedis라는 이름의 컨테이너를 redis-net 네트워크에 붙여 실행한다.
docker run --name dockerRedis -p 6379:6379 --network redis-net -d redis redis-server --appendonly yes

#redis-cli로 dockerRedis에 접속한다.
docker run -it --network redis-net --rm redis redis-cli -h dockerRedis
```

### redis 접근 명령어

- select 0 : 0번 데이터베이스 선택
  - DB의 개수는 redis.conf에 dabases로 정하며, Cluster는 노드 DB 0만 사용할 수 있다.
- keys * : 모든 키 출력
- del keyname : key 지우기
- set key value : key value 형태로 데이터 저장
- get key : key로 value 찾기

## Spring Boot Project

- 의존성 추가

```groovy
dependencies {
	implementation 'org.springframework.boot:spring-boot-starter-data-redis'
	implementation 'org.springframework.boot:spring-boot-starter-web'
	implementation 'org.springframework.boot:spring-boot-starter-mustache'

	compileOnly 'org.projectlombok:lombok:1.18.20'
	annotationProcessor 'org.projectlombok:lombok:1.18.20'

	testCompileOnly 'org.projectlombok:lombok:1.18.20'
	testAnnotationProcessor 'org.projectlombok:lombok:1.18.20'

	testImplementation 'org.springframework.boot:spring-boot-starter-test'
}
```

- yml

```yml
spring.redis:
  host: localhost
  password:
  port: 6379
  pool:
    max-idle: 8
    min-idle: 0
    max-active: 8
    max-wait: 1
```

- Config

```java
@Configuration
public class RedisConfig {

    @Bean
    public RedisConnectionFactory redisConnectionFactory(){
        LettuceConnectionFactory lettuceConnectionFactory = new LettuceConnectionFactory();
        return lettuceConnectionFactory;
    }

    @Bean
    public RedisTemplate<String, Object> redisTemplate(){
        RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(redisConnectionFactory());
        redisTemplate.setKeySerializer(new StringRedisSerializer());
        redisTemplate.setValueSerializer(new StringRedisSerializer());
        return redisTemplate;
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

- MVC

```java
//Response
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class RedisResponse {
    private String key;
    private String value;
}

//Service
@RequiredArgsConstructor
@Service
public class RedisSampleService {

    private final StringRedisTemplate redisTemplate;

    public RedisResponse getRedisStringValue(String key){

        ValueOperations<String, String> stringStringValueOperations = redisTemplate.opsForValue();
        System.out.println("Redis key : " + key);
        System.out.println("Redis value : " + stringStringValueOperations.get(key));

        return RedisResponse.builder()
                .key(key)
                .value(stringStringValueOperations.get(key))
                .build();
    }

}

//Controller
@RequiredArgsConstructor
@Controller
public class RedisSampleController {

    private final RedisSampleService redisSampleService;

    @GetMapping("")
    public String getRedis(Model model, @RequestParam String key){
        model.addAttribute("redisData", redisSampleService.getRedisStringValue(key));

        return "index";
    }
}
```

- index.mustache

```html
<html>
<head>
    <title>Redis Example</title>
</head>

<body>

{{#redisData}}
    key : {{key}}
    value : {{value}}
{{/redisData}}
</body>
</html>
```

- test 
  - redis에 set testKey testValue를 입력하여 데이터를 넣는다.
  - localhost:8080?key=testKey 입력시 인덱스 화면 출력해본다.

## Redis-Session

- 세션처리에 redis를 사용하는 이유
  - 단순히 key-value 구조이며, 적은 용량의 메모리를 요구하는 세션 정보를 저장하기 알맞다.
- docker reids-cli 다시 실행 : docker exec -it dockerRedis redis-cli

- 의존성

```groovy
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
implementation 'org.springframework.session:spring-session-data-redis'
```

- yml

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
    timeout: 600
    store-type: redis
    redis:
      flush-mode: on-save
#      namespace: spring:session
```

- 코드

```java
@Slf4j
@RequiredArgsConstructor
@Controller
@RequestMapping("/session")
public class SessionController {

    private final SessionService sessionService;

    @PostMapping("/add")
    @ResponseBody
    public ResponseEntity<?> addSession(@RequestBody RedisRequest request, HttpSession httpSession){
        sessionService.addSession(request);

        return ResponseEntity.ok().build();
    }
}

@Service
public class SessionService {

    private final StringRedisTemplate stringRedisTemplate;

    public void addSession(RedisRequest request) {
        ValueOperations<String, String> stringStringValueOperations = stringRedisTemplate.opsForValue();

        stringStringValueOperations.set(request.getKey(), request.getKey());

    }
}
```

### 테스트

- localhost:8080/seesion/add

  ```
  {
  "key" : "key",
  "value" : "value"
  }
  ```

- keys * 입력시 다음과 같은 session 정보가 나온다. => 추가가 잘 되었다는 것

```
1) "backup3"
2) "spring:session:sessions:6f4d03be-5dc4-4946-8c86-1a1544b6bdac"
3) "spring:session:expirations:1627539720000"
4) "spring:session:sessions:expires:6f4d03be-5dc4-4946-8c86-1a1544b6bdac"
5) "backup4"
6) "backup1"
7) "backup2"
8) "sessionTest"
```

### 응용 방법

- Spring Security와 OAuth2 연동하여 사용할 수 있다.
  - OAuth2(SNS 로그인)로 로그인하면 Session에 정보가 저장된다.