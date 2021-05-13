# ApplicationProperties(환경설정 프로퍼티 파일 설정)

- 스프링 부트 프로퍼티 파일은 설정 관련 및 기타 정적인 값을 키값 형식으로 관리

```properties
#src/main/resources/application.properties
server.port: 80
```

- 기존에는 위와 같이 properties를 사용했지만, 최근에는 YAML 파일을 더 많이 사용함
  - 프로퍼티 설정값의 깊이에 따라 들여쓰기를 해서 계층 구조를 훨씬 쉽게 파악 가능
  - 사용하려면 SnakeYAML라이브러리가 필요하지만 Spring Boot Starter에 이미 포함되어 있음
  - 위의 파일을 삭제하고 아래의 파일을 생성

```yaml
#src/main/resources/application.yml
server:
	port: 80
```

### 프로파일에 따른 환경 구성 분리

- 실제 서비스에서 개발시 로컬 DB, 개발 DB, 운영 DB의 설정값은 모두 다름
- 프로파일에 따라 프로퍼티를 다르게 설정해야 함

```yaml
#src/main/resources/application.yml
#Default 값
server:
  port: 80
---
spring:
  profiles: local
server:
  port: 8080
---
spring:
  profiles: dev
server:
  port: 8081
---
spring:
  profiles: real
server:
  port: 8082

```

- 위의 결과와 또 다른 방법
- application-{profile}.yml을 이용
  - application-dev.yml 파일과 같이 정의. application.yml에는 디폴트만 정

### 프로파일값 할당(dev)

- Run/Debug Congfiguration - Configuration - Active Profiles: dev
- Active Profiles가 없는 경우
  - Run/Debug Congfiguration - Configuration - VMOptions : -Dspring.profiles.active=dev