# Spring Security Disable

- build.gradle에서는 Spring Security 의존성을 추가했지만, 아직 인증단계를 개발하지 않은 경우 Application에서 exclude를 이용해 Security 기능을 꺼둘 수 있다.

```java
@SpringBootApplication(exclude = SecurityAutoConfiguration.class)
public class FeedApplication {

    public static void main(String[] args) {
        SpringApplication.run(FeedApplication.class, args);
    }
}
```

