# SQL - INSERT, DELETE, UPDATE

### INSERT 기본 명령

```sql
INSERT INTO 테이블명 VALUES(값 1, 값 2)
INSERT INTO sampleTable VALUES (1, 'ABC', '2020-08-07')
```

#### DELETE 기본 명령

- 주의 : WHERE 절을 생략하면 모든 데이터가 지워진다

```sql
DELETE FROM 테이블명 WHERE 조건식
```

- 물리삭제와 논리삭제
  - 물리삭제 : DELETE 명령을 사용해 직접 데이터 삭제 - 개인정보 유출 우려가 있는경우 유용
  - 논리삭제 : UPDATE 명령이용. 삭제플래그를 위한 열을 하나 더 생성 후 삭제요청 시 데이터를 삭제하지 않고 삭제플래그를 변경함(=> 서비스에서 삭제된 데이터 또한 중요한 정보가 된다) - 통계자료를 위해 필요

### UPDATE 기본 명령

- 주의 : WHERE 절을 생략하면 모든 데이터가 갱신된다

```sql
UPDATE 테이블명 SET 열1 = 값1, 열2 = 값2, ... WHERE 조건식
```

