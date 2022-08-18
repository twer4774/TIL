# 스프링 클라우드 설명
[[02. 스프링 클라우드 게이트웨이]] (깃:[https://github.com/twer4774/TIL/blob/master/Spring/SpringCloud/02.%20%EC%8A%A4%ED%94%84%EB%A7%81%20%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%20%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B4.md])
- 사용 이유
	- API의 단일 진입점 역할
	- 인증/인가, LB, 로깅, Circuit Breaker 역할
	- Non-Blocking 방식 (Zuul2도 Non-Blocking)
- 흐름
	- GatewayClient : 경로와 일치하는지 판단
	- [Predicate] Gayeway Handler Mapping 
	- [Predicate] Gateway WebHnadler :  요청과 관련된 필터체인을 통해 요청을 전송
	- Filter : 프록시 요청이 보내지기 전후에 나누어 로직 수행
	- Proxy Filter : 프록시 요청이 처리될때 수행
	- Proxied Service

# 프록시 이용법
## Spring Cloud Gateway
- 게이트웨이 서버
- gralde
``` groovy
plugins {  
   id 'org.springframework.boot' version '2.7.2'  
   id 'io.spring.dependency-management' version '1.0.12.RELEASE'  
   id 'java'  
}  
  
group = 'walter.unit'  
version = '0.0.1-SNAPSHOT'  
sourceCompatibility = '11'  
  
configurations {  
   compileOnly {  
      extendsFrom annotationProcessor  
   }  
}  
  
repositories {  
   mavenCentral()  
}  
  
ext {  
   set('springCloudVersion', "2021.0.3")  
}  
  
dependencies {  
   implementation 'org.springframework.boot:spring-boot-starter-webflux'  
   implementation 'org.springframework.cloud:spring-cloud-starter-gateway'  
   compileOnly 'org.projectlombok:lombok'  
   annotationProcessor 'org.projectlombok:lombok'  
   testImplementation 'org.springframework.boot:spring-boot-starter-test'  
   testImplementation 'io.projectreactor:reactor-test'  
}  
  
dependencyManagement {  
   imports {  
      mavenBom "org.springframework.cloud:spring-cloud-dependencies:${springCloudVersion}"  
   }  
}  
  
tasks.named('test') {  
   useJUnitPlatform()  
}
```
- application.yml
``` yaml
server.port: 7090  
spring:  
  application:  
    name: spring-clound-gateway  
  config:  
    import: api-gw.yml
```
- api-gw.yml
	-  Header값에 따라 라우팅 되도록 설정
		- test : test1만 통과하며 이외의 값은 에러를 발생시킬 예정(밑에 공통 에러처리)
``` yaml
spring:  
  cloud:  
    gateway:  
      httpclinet:  
        connect-timeout: 500  
        response-timeou: 1000  
      routes:  
        - id: app1  
          uri: http://localhost:8080  
          predicates:  
            - Path=/index/**
            - Header=test, test1
``` 
## Spring Boot Server (App1)
- 기본 API 서버
``` java
@GetMapping("/{id}")  
public ResponseEntity index(@RequestHeader String test, @PathVariable String id){  
    if (test==null) {  
        throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Not Found");  
    }  
    try {  
        return ResponseEntity.ok().body("index" + id);  
    } catch(NoSuchElementException e){  
        throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Not Found");  
    }  
}
```


# 공통 에러처리
- Controller Advice를 이용해서 에러를 처리할 수 없다.
	- Netty 기반의 WebFlux로 동작하기 때문
	- ErrorWEbExceptionHandler를 이용한다.
- GWErrorResponse
``` java
@Getter  
public class GWErrorResponse {  
  
    private String errorMessage;  
    private LocalDateTime localDateTime;  
    private Map<String, Object> erroInfo = new HashMap<>();  
  
    public GWErrorResponse(String errorMessage, LocalDateTime localDateTime) {  
        this.errorMessage = errorMessage;  
        this.localDateTime = localDateTime;  
    }  
  
    public static GWErrorResponse defaultError(String errorMessage){  
        return new GWErrorResponse(errorMessage, LocalDateTime.now());  
    }  
}
```
- GlobalExceptionHandler
``` java
@Slf4j  
@Order(-1)  
@RequiredArgsConstructor  
public class GlobalExceptionHandler implements ErrorWebExceptionHandler {  
  
    private final ObjectMapper objectMapper;  
  
    @Override  
    public Mono<Void> handle(ServerWebExchange exchange, Throwable ex) {  
        ServerHttpResponse response = exchange.getResponse();  
  
        if (response.isCommitted()) {  
            return Mono.error(ex);  
        }  
  
        // Header  
        response.getHeaders().setContentType(MediaType.APPLICATION_JSON);  
        if (ex instanceof ResponseStatusException) {  
            response.setStatusCode(((ResponseStatusException) ex).getStatus());  
        }  
        return response.writeWith(Mono.fromSupplier(() -> {  
            DataBufferFactory bufferFactory = response.bufferFactory();  
            try {  
                GWErrorResponse gwErrorResponse = GWErrorResponse.defaultError(ex.getMessage());  
                byte[] errorResponse = objectMapper.writeValueAsBytes(gwErrorResponse);  
  
                return bufferFactory.wrap(errorResponse);  
            } catch (Exception e) {  
                log.error("error", e);  
                return bufferFactory.wrap(new byte[0]);  
            }  
        }));  
    }  
}
```

# 테스트
- SpringCloudGateway 서버 실행 (포트번호 7090)
- App1 서버 실행 (포트번호 8080)
- 웹브라우저에서 localhot:7090/test/aa 실행
	- Header에 test : test1을 넣는다. 다른 값을 넣으면 에러 발생
	- App1로 라우팅되는지 확인