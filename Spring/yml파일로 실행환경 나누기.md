# yml파일로 실행환경 나누기

- 로컬, 개발, 스테이징, 운영 환경 별로 각 설정파일들이 다를 수 있다.
  - 로컬 : localhost, 127.0.0.1과 같이 개발하는 환경
  - 개발 : 개발 서버를 따로 두어 테스트용 서버로 이용(잘 사용되지 않음). 개발자가 임의로, 수시로 코드 및 데이터베이스 테이블 변경가능
  - 스테이징 : 개발자 및 다른 팀 등 개발 팀 외에도 동작을 확인할 수 있는 환경. 스테이징서버에 올릴 수 있는 관리자를 두어 관리. 운영환경 전의 최종 테스트 환경
  - 운영 : 실제로 운영되는 환경
- 인텔리제이에서 실행환경을 지정하는 방법 3가지 : https://yangbox.tistory.com/44

## yml

- Spring boot 2.4버전 부터 active와 include를 deprecated 되었다.
  - spring boot 2.4 변경 내용 : https://tangoblog.tistory.com/13
- spring.profiles.group="" 과 같이 그룹으로 묶어 설정시키는 방법으로 바뀌었다.

```yaml
#application.yml
server:
    port: 8080
#spring boot 2.4 이전
#---
#spring:
#  profiles:
#    active: local

#---
#spring:
#  profiles:
#    active: dev

#spring boot 2.4 이후
spring:
  application:
    name: environment_profiles
  profiles:
    group:
      "local" : "local"
      "dev" : "dev"
---
spring:
  config:
    activate:
      on-profile: "local"

---
spring:
  config:
    actviate:
      on-profile: "dev"
    
#application-local.yml
spring:
  environment:
    name: "local"
#application-dev.yml
spring:
  environment:
    name: "dev"
```

## mustache

```html
<html>
<body>
    환경 : {{environment}}
</body>
</html>
```

## controller

```java
@Controller
public class EnvironmentController {

    @Value("${spring.environment.name}")
    private String environment;

    @GetMapping("")
    public String index(Model model){
        model.addAttribute("environment", environment);

        return "index";
    }
}
```

## 설정

- edit run/debug configurations
  - application 추가 - local, dev
    - build and run 등 설정 (모르면 main application을 한 번 실행하고 나면 configurations에 등록되므로 참고하여 똑같은 환경을 맞춘다.)
    - Program Arguments : --spring.profiles.active=local 
      - 위의 실행환경을 설정하는 3가지 방법 링크에 들어가서 자세한 내용 확인. 이 방법이 우선순위가 가장 높다고 한다.
- 동일한 방법으로 dev도 만들어주면 각 실행환경에 맞게 구동할 수 있다.



## Jar파일로 만들기

- gradle/bootJar 등으로 실행
- application의 기본 값으로 jar 파일이 실행되며, 특정 profile을 활성화 시키기 위해서는 -Dspring.profiles.active= 값을 넣는다.

```
java -jar -Dspring.profiles.active=local {$jarFileNames}.jar
```

