# Spring Boot 프로젝트 Docker로 만들기

- https://hub.docker.com/_/openjdk?tab=tags&page=1&ordering=last_updated

## Spring Boot 어플리케이션 jar 파일 생성

### Spring Boot 어플리케이션 생성

- start.spring.io에서 간단한 웹 어플리케이션을 생성한다.

### jar 파일 생성

- Gradle을 이용하면 build - bootJar를 실행한다.

- dockerdemo/build/libs 경로에  dockerdemo-0.0.1-SNAPSHOT.jar 파일이 생성된다.

### JDK와 JRE의 차이

- JRE는 자바 어플리케이션을 실행시키는 도구에 대한 묶음
- JDK는 자바 어플리케이션 개발 도구에 대한 묶음

## Dockerfile 만들기

- Dockerfile이란?
  - 기본이 되는 이미지를 사용하여 개발한 어플리케이션을 기본 이미지에 레이어 형식으로 추가한다.

```dockerfile
#기본이 되는 이미지
FROM openjdk:11.0.12-jre-slim-buster
COPY /build/libs/dockerdemo-*-SNAPSHOT.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

## Docker 이미지 만들기

- docker build -t dockerdemo .
  - 마지막에 . 넣어야 한다.
- docker images로 이미지 생성 확인

## Docker 이미지 실행

- docker run -d -p 8081:8080 dockerdemo
  - 앞의 8081은 외부 포트 => 내가 웹브라우저에서 접속할 포트번호
  - 뒤의 8080은 도커 내부에서 실행하는 포트 번호 

## docker-compose.yml

- 여러 container를 관리하는 환경 설정
  - Spring Boot와 연관된 컨테이너(ex. mysql)를 함께 실행 시킬 수 있도록 한다.