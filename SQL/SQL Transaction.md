# SQL Transaction

```sql
START TRANSACTION
COMMIT
ROLLBACK
```

### 롤백과 커밋

- 몇 단계로 처리를 나누어 SQL 명령을 실행하는 경우 트랜잭션을 자주 사용

- 트랜잭션을 이용해 데이터를 추가한다면 에러가 발생해도 트랜잭션을 롤백해서 종료 할 수 있음

  - 롤백하면 트랜잭션 내에서 행해진 모든 변경사항을 없던것으로 할 수 잇음

- 커밋 : 아무런 에러가 발생하지 않는다면 변경사항을 적용하고 트랜잭션을 종료

- 자동커밋 : 트랜잭션을 사용해서 데이터를 추가할 때는 자동커밋을 꺼야함 - 명시적으로 트랜잭션시작(START TRANSACTION)

- ```sql
  #트랜잭션 시작
  #MySQL
  START TRANSACTION
  #SQL Sever, PostgreSQL
  BEGIN TRANSACTION
  
  #트랜잭션 내에서 실행한 명령을 적용한 후 종료
  COMMIT
  
  #트랜잭션 내에서 실행한 명령을 파기한 후 종료
  ROLLBACK
  ```

  

### 예

```sql
#트랜잭션을 사용하지 않는 발주처리
INSERT INTO 주문 VALUES(4, '2002-01-03', 1);
INSERT INTO 주문상품 VALUES(4, '0003', 1);
INSERT INTO 주문상품 VALUES(4, '0005', 2); #여기서 에러 발생시 DELETE를 이용해 위의 데이터를 지워야함

#트랜잭션을 사용한 발주처리
START TRANSACTION;
INSERT INTO 주문 VALUES(4, '2002-01-03', 1);
INSERT INTO 주문상품 VALUES(4, '0003', 1);
INSERT INTO 주문상품 VALUES(4, '0005', 2);
COMMIT;
```

