# SpringBoot Redis 연동 - Cache

## Cache 이유

- 한 번 읽은 데이터를 Cache로 저장하여 불필요한 서버호출을 줄인다.
- 빠른 출력이 가능하다.
- 단점으로는 서버가 다운되면 없어지는 휘발성이다.
- Cache의 대상이 되는 정보들
  - 단순한 정보
  - 빈번하게 호출되는 동일한 정보
  - 검색어, 카테고리 별 상품 수, 방문자 수, 조회수, 추천수 등

## Redis Cache 서버

사용자 - 레디스 캐시 서버 - MySQL 서버

- 위의 구조로 연결되며, 레디스 캐시 서버로 데이터를 요청하여 데이터가 없다면 MySQL로 요청을 보낸다.

## 캐시 어노테이션

- @Cacheable : 캐시가 있으면 캐시 정보를 가져오고, 없으면 등록한다.
- @CachePut : 무조건 캐시에 저장한다.
- @CacheEvict : 캐시를 삭제한다.

## 실습

- 목표 : Redis를 Cache 서버로 만들어서 MySQL 서버의 요청 부하를 줄인다.

### Redis 서버는 Docker로 구동한다.

```
docker pull redis
docker network create redis-net

#dockerRedis라는 이름의 컨테이너를 redis-net 네트워크에 붙여 실행한다.
docker run --name dockerRedis -p 6379:6379 --network redis-net -d redis redis-server --appendonly yes

#redis-cli로 dockerRedis에 접속한다.
docker run -it --network redis-net --rm redis redis-cli -h dockerRedis
```

### 의존성

```groovy
//Redis, MySQL 연결 의존성
implementation 'org.springframework.session:spring-session-data-redis'
implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
runtimeOnly 'mysql:mysql-connector-java'

//웹 관련 의존성
implementation 'org.springframework.boot:spring-boot-starter-mustache'
implementation 'org.springframework.boot:spring-boot-starter-web'

testImplementation 'org.springframework.boot:spring-boot-starter-test'
```

### yml

```yml
spring:
  redis:
    host: localhost
    password:
    port: 6379
    cache:
      type: redis
    pool:
      max-idle: 8
      min-idle: 0
      max-active: 8
      max-wait: 1

  #MySQL 설정
  datasource:
    url: jdbc:mysql://localhost:3306/testdb?allowPublicKeyRetrieval=true&useSSL=false&useUnicode=true&serverTimezone=Asia/Seoul
    username: root
    password:
    database-platform: org.hibernate.dialect.MySQL5InnoDBDialect
    driver-class-name: com.mysql.cj.jdbc.Driver

    jackson:
      property-naming-strategy: SNAKE_CASE

  jpa:
    hibernate:
      ddl-auto: update #배포시 NONE으로 변경
    database-platform: org.hibernate.dialect.MySQL5Dialect
    show_sql: true

```

### 설정

- RedisConfig : Redis와 연관된 설정

```java
package walter.unit.common.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.connection.RedisStandaloneConfiguration;
import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

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
    public RedisTemplate<String, Object> redisTemplate(){
        RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(redisConnectionFactory());
        redisTemplate.setKeySerializer(new StringRedisSerializer());
//        redisTemplate.setValueSerializer(new StringRedisSerializer());
        redisTemplate.setValueSerializer(new GenericJackson2JsonRedisSerializer()); //json객체로 변환
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

- CacheConfig : Cache 처리에 관한 설정 => Redis로 캐시처리할 수 있도록 연결한다.

```java
package walter.unit.cacheexample.config;

import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.cache.CacheManager;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.cache.RedisCacheConfiguration;
import org.springframework.data.redis.cache.RedisCacheManager;
import org.springframework.data.redis.connection.RedisConfiguration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.repository.configuration.EnableRedisRepositories;
import org.springframework.data.redis.serializer.GenericJackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.RedisSerializationContext;
import org.springframework.data.redis.serializer.StringRedisSerializer;

import java.time.Duration;

@RequiredArgsConstructor
@Configuration
public class CacheConfig {

    private final RedisConnectionFactory redisConnectionFactory;
    private final ObjectMapper objectMapper;

    @Bean(name = "redisCacheManager")
    public CacheManager redisCacheManager(){
        RedisCacheConfiguration redisCacheConfiguration = RedisCacheConfiguration.defaultCacheConfig()
                .serializeKeysWith(RedisSerializationContext.SerializationPair.fromSerializer(new StringRedisSerializer()))
                .serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(new GenericJackson2JsonRedisSerializer()))
                .entryTtl(Duration.ofSeconds(30)); //TTL 적용도 가능하다. (데이터 유효기간 설정)

        RedisCacheManager redisCacheManager = RedisCacheManager.RedisCacheManagerBuilder.fromConnectionFactory(redisConnectionFactory) //Connect 적용하고
                .cacheDefaults(redisCacheConfiguration).build(); //캐쉬설정과 관련된 것을 여기에 적용.
        return redisCacheManager;
    }
}
```

- JpaConfig : Jpa 설정

```java
@Configuration
@EnableJpaAuditing
public class JpaConfig {

}
```

### Model

- Post 엔티티
  - Redis는 HashMap 형식으로 저장되므로, Serializable 하는것이 안전하다.

```java
@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Post implements Serializable{

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private String content;
    private Boolean readOnly; //수정가능여부
}
```

- PostResponse 응답 객체

```java
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class PostResponse {
    private Long id;
    private String title;
    private String content;
    private Boolean readOnly; //수정가능여부
}
```

- PostRepository

```java
public interface PostRepository extends JpaRepository<Post, Long> {

    List<Post> findByReadOnly(boolean readOnly);
}
```

### Service

- Cachable 처리를 한다.

```java
@Transactional
@RequiredArgsConstructor
@Service
public class PostService {

    private final PostRepository postRepository;

      /**
     * readOnly의 boolean 값에 따라 불러오는 post 목록
     * @param readOnly
     * @return
     */
    @Cacheable(value = "readOnly", key = "#readOnly", cacheManager = "redisCacheManager")
    public List<PostResponse> onlyReadPost(boolean readOnly) {

        return postRepository.findByReadOnly(readOnly)
                .stream().map(post -> {
                   return PostResponse.builder()
                            .id(post.getId())
                            .title(post.getTitle())
                            .content(post.getContent())
                            .readOnly(post.getReadOnly())
                            .build();
                }).collect(Collectors.toList())
                ;
    }
  
  

      /**
     * post의 id 값으로 불러오는 post
     * @param id
     * @return
     */
    @Cacheable(value = "getPost", key = "#id", cacheManager = "redisCacheManager")
    public PostResponse getPost(Long id) {
        return postRepository.findById(id)
                .map(post -> {
                    return PostResponse.builder()
                            .id(post.getId())
                            .title(post.getTitle())
                            .content(post.getContent())
                            .readOnly(post.getReadOnly())
                            .build();
                }).get();
    }
}
```

### Controller

```java
@RequiredArgsConstructor
@Controller
@RequestMapping("")
public class PostController {

    private final PostService postService;

    @GetMapping("")
    public ResponseEntity<?> index(@PathParam("readOnly") String readOnly){
        boolean onlyBoolean = readOnly.equals("true");
        return ResponseEntity.ok().body(postService.onlyReadPost(onlyBoolean));
    }

  //post.mustache로 화면을 출력한다.
    @GetMapping("/{id}")
    public String getPost(Model model, @PathVariable("id") Long id){
        model.addAttribute("post", postService.getPost(id));
        return "post";
    }
}
```

### View

- resources/templates/post.mustache

```html
<html>
<body>
    {{#post}}
        title : {{title}} <br>
        content: {{content}} <br>
        readOnly : {{readOnly}}
    {{/post}}
</body>
</html>
```

### 메인

```java
@EnableCaching
@SpringBootApplication
public class CacheExampleApplication {

    public static void main(String[] args) {
        SpringApplication.run(CacheExampleApplication.class, args);
    }
}
```

### 테스트

- 먼저, repository test를 이용하여 MySQL에 post 데이터들을 저장한다.

```java
@SpringBootTest
class PostRepositoryTest {

    @Autowired
    private PostRepository postRepository;

    @Test
    public void create(){
        for (int i = 0; i < 10; i++) {
            Post post = Post.builder()
                    .title("title " + i)
                    .content("content " + i)
                    .readOnly(true)
                    .build();

            postRepository.save(post);
        }
    }
}
```

- http://localhost:8080/2 입력 후 여러번 다시 실행해도 hibernate의 sql문이 실행되지 않는다.(TTL 시간 이후 다시 실행하면 실행된다.)
- redis-cli에서 get getPost::2으로 값 확인