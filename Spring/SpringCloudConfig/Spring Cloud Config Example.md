# Spring Cloud Config

- 분산 시스템에서 환경설정을 외부로 분리하여 관리하는 기능을 제공한다.
- Config Server를 사용하여 모든 환경(개발, 테스트, 프로덕션)에 대한 어플리케이션들의 속성을 한 곳에서 관리할 수 있다.
  - 기본 값은 git이며, git repository에서 관리한다.
  - ConfigServer가 실행되는 native환경(서버가 실행되는 컴퓨터)으로 설정 할 수도 있다.
- https://github.com/spring-cloud/spring-cloud-release/wiki/Spring-Cloud-2020.0-Release-Notes#breaking-changes
  - 예전에는 bootstrap.yml를 이용하여 application.yml 이전에 환경설정을 추가했지만, 2020 릴리즈부터 application.yml에서 모두 관리할 수 있다.

### 장점

- 중앙집중 관리로 분산 처리환경에서 설정 관리가 용이하다.
- 운영중에 서버 빌드 및 배포 없이 환경설정 변경 가능하다.

### 기능

- Spring Cloud Config Server
  - 환경설정(YAML파일)을 위한 HTTP, 리소스 기반 API
  - 속성 값 암호화 및 암호해독(대칭 또는 비대칭)
  - @EnableConfigServer 어노테이션을 사용하여 쉽게 Spring Boot 어플리케이션에 적용가능
- Config Client
  - Config Server로부터 Spring 환경 초기화
  - 속성 값 암호화 및 암호 해독(대칭 또는 비대칭)

## 실습

- spring boot version 2.5.4 버전은 Spring Cloud와 연동되지 않았다.

- ```
  Description:
  
  Your project setup is incompatible with our requirements due to following reasons:
  
  - Spring Boot [2.5.4] is not compatible with this Spring Cloud release train
  ```

  ```
  id 'org.springframework.boot' version '2.4.8'
  ```

### Spring Cloud Config Server

1. build.gradle

```groovy
plugins {
    id 'org.springframework.boot' version '2.4.8'
    id 'io.spring.dependency-management' version '1.0.11.RELEASE'
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

dependencies {
    implementation 'org.springframework.cloud:spring-cloud-config-server'
    compileOnly 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}

//추가하지 않으면 @EnableConfigServer 어노테이션을 찾을 수 없다.
dependencyManagement {
    imports {
        mavenBom ("org.springframework.cloud:spring-cloud-dependencies:2020.0.1")
    }
}

test {
    useJUnitPlatform()
}

```

2. @EnableConfigServer 어노테이션 추가

```java
@SpringBootApplication
@EnableConfigServer
public class ConfigServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConfigServerApplication.class, args);
    }
}
```

3. yml 파일
   - 기본적으로 git repository로 연결되어 설정파일을 불러온다.
   - active: native를 이용하면, config server에 있는 설정파일을 불러오는 것으로 변경 가능하다.

```yaml
server.port: 8888

spring:
  application:
    name: config-server
  profiles:
    active: native
  cloud:
    config:
      server:
        native:
          search-locations: classpath:/config

management:
  endpoints:
    web:
      exposure:
        include: ['refresh', 'beans', 'evn']
```

4. 설정 파일들 (/resources/config/..)

```yaml
#example-default.yml
example:
  name: defaultName
  type: default
  
#example-dev.yml
example:
  name: devName
  type: dev

#example-prod.yml
example:
  name: prodName
  type: prod
```

5. 테스트

- https://localhost:8888/example/dev
- https://localhost:8888/example/prod

6. Git repository로 설정 파일 다루기
   - yml의 설정을 바꾼다.

```yaml
server.port: 8888

spring:
  application:
    name: config-server
  profiles:
    active: native
#  cloud:
#    config:
#      server:
#        native:
#          search-locations: classpath:/config


# github에 설정 파일 저장
  cloud:
    config:
      server:
        git:
          uri: https://github.com/twer4774/TIL/tree/master/Spring/SpringCloud/SpringCloud/spring-cloud-config-git-repository

management:
  endpoints:
    web:
      exposure:
        include: ['refresh', 'beans', 'evn']
```

### Client

https://github.com/spring-cloud/spring-cloud-release/wiki/Spring-Cloud-2020.0-Release-Notes#breaking-changes

- 예전에는 bootstrap.yml를 이용하여 application.yml 이전에 환경설정을 추가했지만, 2020 릴리즈부터 application.yml에서 모두 관리할 수 있다.

  ```
  spring:
    config:
      import: configserver:http://localhost:8888
  ```

  

1. build.gradle

```groovy
plugins {
    id 'org.springframework.boot' version '2.4.8'
    id 'io.spring.dependency-management' version '1.0.11.RELEASE'
    id 'java'
}

version 'unspecified'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springframework.boot:spring-boot-starter-actuator'
    implementation 'org.springframework.cloud:spring-cloud-config-client'

    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.7.0'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.7.0'
}

dependencyManagement {
    imports {
        mavenBom ("org.springframework.cloud:spring-cloud-dependencies:2020.0.1")
    }
}

test {
    useJUnitPlatform()
}
```

2. application.yml

```yaml
server.port: 9093

spring:
  config:
    import: configserver:http://localhost:8888
  application:
    name: example
  profiles:
    active: dev #환경 선택

management:
  endpoints:
    web:
      exposure:
        include: ['refresh','beans','env']
```

3. controller

```java
@RefreshScope
@RestController
public class SimpleController {

    @Value("${example.name}")
    private String name;

    @Value("${example.type}")
    private String type;

    @GetMapping("")
    public String simple(){
        return "name: " + name + " / type: " + type;
    }
}
```

4. application

```java
@SpringBootApplication
public class OnlyControllerApplication {
    public static void main(String[] args) {
        SpringApplication.run(OnlyControllerApplication.class, args);
    }
}
```



### 테스트 : 2가지 테스트 진행

#### 1. 개발 환경 변경 - client에서만 yml 변경

- http://localhost:9093 접속 : 현재 dev이므로 dev에 관련된 내용 출력. 아무것도 넣지 않으면 default 출력
- client - application.yml에서 변경

```yaml
 profiles:
    active: prod #환경 선택
```

- http://localhost:9093 접속

#### 2. config-server에서 yml 변경 후 client에서 확인

- http://localhost:9093 접속
- 1번 테스트에서 현재 prod 환경으로 변경했으므로, config-server의 example-prod의 내용을 변경한다.

```yaml
#example-prod.yml
example:
  name: productName
  type: product
```

- config-server를 재실행 한다.
- [POST] 메소드로 http://localhost:9093/actuator/refresh를 보낸다.
  - post 메소드로 보내는 방법 
    - 크롬 확장 프로그램(https://chrome.google.com/webstore/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm/reviews?hl=ko)
    - 포스트맨 사용(https://www.postman.com/)

- http://localhost:9093 접속해 변경된 내용을 확인한다.

