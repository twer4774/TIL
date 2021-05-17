# Hiberante의 ddl-auto

Spring JPA 에서 Hibernate를 이용하여 DDL을 생성하여 Data Table을 자동으로 생성할 수 있습니다.

## DDL이란?

데이터 정의어(Data Defination Language, DDL)

데이터베이스의 테이블의 생성, 변경, 삭제를 담당하는 명령어입니다.

- 대표적으로 CREATE, ALTER, DROP, RENAME, TRUNCATE가 있습니다.



## Hibernate의 ddl-auto

Spring JPA에서  application.yml(또는 application.properties)에 JPA 관련 설정 중 ddl을 자동으로 설정 할 수 있는 기능이 있습니다.

```yml
spring:
	jpa:
		hibernate:
			ddl-auto: update
```

- hibernate란 jpa를 구현하여 사용하기 편리하도록 만든 구현체입니다.

- ddl-auto의 옵션
  - none
  - update : 테이블의 내용이 변경된 경우 자동으로 ddl실행
  - create : 프로그램 시작 시 create 
  - create-drop : 프로그램 시작 시 create, 종료 시 drop
  - validate : 테이블 내용이 변경되면 변경 내용을 출력하고 프로그램 종료
- 스프링 부트 프로젝트에서 테스트 데이터베이스로 사용되는 H2는 기본적으로 create-drop을 사용하기 때문에 프로그램을 재시작하면 작업한 내용이 사라집니다.
  - ddl-auto 내용을 update한다면, 프로그램을 재시작하더라도 데이터가 사라지지 않습니다.

