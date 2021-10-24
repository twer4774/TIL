# Docker Compose로 Mysql 컨테이너 생성

### docker-compose.yml

```yml
version: '3'
services:
    mysql:
      image: mysql:5.7
      container_name: feed_service_mysql
      ports:
        - "3400:3306"
      environment:
        - MYSQL_ROOT_PASSWORD=
        - MYSQL_DATABASE=sns_feed
        - MYSQL_USER=sns_feed
        - MYSQL_PASSWORD=1234
      command:
        - --character-set-server=utf8mb4
        - --collation-server=utf8mb4_unicode_ci
      healthcheck:
        test: ["CMD", "mysqladmin" ,"ping", "-h", "localhost"]
        timeout: 10s
        retries: 10
      restart: always
      volumes:
          - /Users/Shared/data/mysql-test:/var/lib/mysql
```

### 참고: 위의 동작이 실행되지 않을 경우.

- MYSQL_USER와 MYSQL_PASSWORD를 사용하기 위해 새로운 User를 만들어 준다.
- workbench를 이용해 docker의 mysql로 접속한 뒤 다음 명령을 실행한다.

```sql
create user 'sns_feed'@'%' identified by '1234';
grant all privileges on *.* to 'sns_feed'@'%';
flush privileges;
```

### docker-compose 실행

- docker-compose up

### yml

- application.yml

```yaml
server.port: 3000

spring:
  profiles:
    include: mysql
```

- application-mysql.yml

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3400/sns_feed?allowPublicKeyRetrieval=true&useSSL=false&useUnicode=true&serverTimezone=Asia/Seoul
    username: sns_feed
    password: 1234
    database-platform: org.hibernate.dialect.MySQL5InnoDBDialect
    driver-class-name: com.mysql.cj.jdbc.Driver

  jackson:
    property-naming-strategy: SNAKE_CASE

  jpa:
    hibernate:
      ddl-auto: update
      dialect: org.hibernate.dialect.MySQL5InnoDBDialect
    show-sql: true
```

### 테스트

- FeedEntity

```java
@Entity
@Getter
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Table(name = "feed")
public class Feed {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;

    private String content;

    private Long userId;
}
```

- FeedRepository

```java
public interface FeedRepository extends JpaRepository<Feed, Long> {
}
```

- FeedrepositoryTest

```java
@SpringBootTest
class FeedRepositoryTest {

    @Autowired
    private FeedRepository feedRepository;


    @Test
    public void create(){

        Feed feed = Feed.builder()
                .id(1L)
                .title("testTitle")
                .content("testContent")
                .userId(1L)
                .build();

        System.out.println(feed);
        feedRepository.save(feed);

    }
}
```

